# PawPal+ Project Reflection

## 1. System Design

Add/manage a pet — register a pet with its name, type, and care constraints (e.g., medication schedule, dietary needs)
Log a care task — record completed or upcoming tasks (walks, feeding, meds, grooming, enrichment)
View today's plan — see a prioritized daily schedule with explanations for why each task was chosen/ordered

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design included four classes: Pet, CareTask, Owner, and DailyPlanner.

- Pet holds basic information about an animal (name, species, age, weight) and can produce a human-readable summary of itself.
- CareTask represents a single care activity (e.g., walk, feeding, meds) with a type, duration, priority level, and completion status. It can mark itself complete and check whether it is due today.
- Owner stores the user's name, daily time budget, and preferences. It manages a list of pets and is responsible for adding and retrieving them.
- DailyPlanner is the central scheduling object. It takes an owner and their tasks and is responsible for generating a prioritized daily plan, explaining the reasoning behind it, and reporting which tasks have been completed.


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, the design changed after reviewing the initial skeleton. The most significant change was to CareTask: in the original design it had no link to a specific Pet and no date information, meaning the planner had no way to know which task belonged to which animal or whether a task was actually due. Two fields were added — pet: Pet to establish the ownership relationship, and scheduled_date: date so is_due_today() has real data to compare against.

The second change was replacing priority: str with a Priority enum. The string approach allowed silent bugs (e.g., "High" vs "high") that would break any sorting logic in generate_plan(). Using an enum makes invalid priorities a hard error at the point of creation rather than a subtle runtime failure.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers two main constraints: time budget (the owner's total available minutes for the day) and task priority (high, medium, or low). Tasks are sorted by priority first, then greedily added to the plan as long as they fit within the remaining time. Duplicate tasks and time overflows are flagged as warnings via conflict detection.

Priority was treated as the most important constraint because a pet missing medication or feeding is a worse outcome than missing enrichment or grooming. Time budget came second since the owner's day is finite and the scheduler must make hard cuts. Owner preferences were acknowledged in the design but left as a future improvement — they are stored on the Owner object but not yet factored into sorting logic.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The scheduler uses a greedy first-fit strategy: it sorts tasks by priority and adds each one if it fits within the remaining time budget, stopping as soon as a task doesn't fit rather than searching for a smaller task that might still squeeze in. A more optimal algorithm (like 0/1 knapsack) could pack the day more efficiently, but it would be significantly more complex to read and debug. For a daily pet care planner — where simplicity and predictability matter more than squeezing out every last minute — the greedy approach is a reasonable tradeoff.

When asked to simplify `generate_plan()`, AI suggested collapsing the accumulation loop into a single `itertools.accumulate` expression. That version was more concise but harder to read at a glance. The explicit `for` loop was kept because it reads like plain English ("for each task, if it fits, add it") and is easier to modify if the scheduling rules change later.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI primarily for design brainstorming and code refactoring. During the initial design phase, I asked for suggestions on how to structure the classes and their relationships, which helped me identify key responsibilities and data flows. For example, I prompted: "How would you design a pet care scheduling system in Python? What classes and methods would you include?"

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One moment was when AI suggested using `itertools.accumulate` to simplify the scheduling loop in `generate_plan()`. While the code was more concise, it was less readable and harder to understand at a glance. I evaluated this suggestion by considering the tradeoff between conciseness and clarity. Since the scheduling logic is a critical part of the system and may need future modifications, I prioritized readability and maintainability over brevity, ultimately deciding to keep the explicit `for` loop.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested several key behaviors of the scheduling system:
- Sorting: I verified that tasks are returned in ascending duration order and that completed and future-dated tasks are excluded from today's plan.
- Recurrence: I tested that completing a `daily` task spawns a new task for tomorrow, that `weekly` tasks schedule 7 days out, and that `once` tasks do not recur.
- Conflict detection: I checked that duplicate task types on the same day trigger a warning, that tasks that overflow the time budget trigger a budget warning, and that a clean schedule produces no warnings.
- Edge cases: I tested that a pet with zero tasks returns an empty list and a correct summary, and that an owner with no pets generates an empty plan without errors.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am fairly confident that the core scheduling behaviors are working correctly, as all 12 tests pass against the current implementation. The tests cover priority sorting, time-budget enforcement, recurring task generation, and conflict detection, which are the main functionalities of the system.
If I had more time, I would test additional edge cases such as:
- Handling of invalid inputs (e.g., negative durations, empty strings for task types).
- Tasks that are scheduled for the past or far future to ensure they are correctly excluded from today's plan.
- Interactions between multiple pets with overlapping tasks to verify that the planner aggregates and sorts them correctly across all pets.


---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am most satisfied with the overall design and implementation of the scheduling logic in `DailyPlanner`. The system successfully prioritizes tasks based on their importance and fits them within the owner's time budget, while also providing clear explanations for the generated plan. The conflict detection mechanism is also a strong point, as it proactively identifies issues that could arise from duplicate tasks or time overflows, helping owners manage their pet care more effectively.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the handling of owner preferences in the scheduling logic. Currently, preferences are stored but not factored into the task prioritization or sorting. I would redesign the `generate_plan()` method to consider these preferences, allowing owners to specify certain tasks as "must do" or "can skip" based on their personal priorities and constraints. Additionally, I would implement input validation at the system boundaries to prevent invalid data from causing issues downstream.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important takeaway is that while AI can provide valuable suggestions for design and code improvements, it is crucial to apply human judgment when evaluating those suggestions. Not every AI-generated idea will be the best fit for the specific context of the project, and it's important to consider tradeoffs such as readability, maintainability, and the specific needs of the users when deciding whether to implement an AI suggestion. This project reinforced the importance of balancing AI assistance with critical thinking to create a system that is both functional and user-friendly.
