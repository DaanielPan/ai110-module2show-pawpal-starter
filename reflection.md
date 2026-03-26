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

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
