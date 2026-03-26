from datetime import date
from pawpal_system import CareTask, Pet, Priority


def test_mark_complete():
    task = CareTask("Walk", 30, Priority.HIGH, date.today())
    task.mark_complete()
    assert task.is_completed is True


def test_pet_add_task():
    pet = Pet("Buddy", "Dog", 3, 12.5)
    task = CareTask("Walk", 30, Priority.HIGH, date.today())
    pet.add_task(task)
    assert len(pet.tasks) == 1
