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

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

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
