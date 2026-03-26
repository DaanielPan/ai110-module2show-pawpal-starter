from datetime import date
from pawpal_system import CareTask, Pet, Owner, DailyPlanner, Priority

# Create owner
owner = Owner(name="Daniel", available_time_minutes=90)

# Create pets
buddy = Pet(name="Buddy", species="Dog", age=3, weight=12.5)
luna = Pet(name="Luna", species="Cat", age=5, weight=4.2)

# Add tasks to Buddy
buddy.add_task(CareTask("Morning Walk", 30, Priority.HIGH, date.today()))
buddy.add_task(CareTask("Feeding", 10, Priority.HIGH, date.today()))

# Add tasks to Luna
luna.add_task(CareTask("Grooming", 20, Priority.MEDIUM, date.today()))
luna.add_task(CareTask("Playtime / Enrichment", 15, Priority.LOW, date.today()))

# Register pets with owner
owner.add_pet(buddy)
owner.add_pet(luna)

# Run planner
planner = DailyPlanner(owner)

print("=== PawPal+ ===")
for pet in owner.get_pets():
    print(pet.get_summary())

print()
print(planner.explain_plan())
