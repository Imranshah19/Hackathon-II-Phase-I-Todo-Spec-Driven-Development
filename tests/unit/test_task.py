"""Unit tests for the Task dataclass."""

import pytest
from src.models.task import Task


class TestTask:
    """Tests for Task dataclass."""

    def test_task_creation_with_defaults(self):
        """Task should have completed=False by default."""
        task = Task(id=1, title="Test task")

        assert task.id == 1
        assert task.title == "Test task"
        assert task.completed is False

    def test_task_creation_with_completed(self):
        """Task should accept completed parameter."""
        task = Task(id=2, title="Completed task", completed=True)

        assert task.id == 2
        assert task.title == "Completed task"
        assert task.completed is True

    def test_task_equality(self):
        """Tasks with same attributes should be equal."""
        task1 = Task(id=1, title="Same task", completed=False)
        task2 = Task(id=1, title="Same task", completed=False)

        assert task1 == task2

    def test_task_inequality_different_id(self):
        """Tasks with different IDs should not be equal."""
        task1 = Task(id=1, title="Same title")
        task2 = Task(id=2, title="Same title")

        assert task1 != task2

    def test_task_repr(self):
        """Task should have useful string representation."""
        task = Task(id=1, title="Test", completed=True)

        repr_str = repr(task)
        assert "Task" in repr_str
        assert "1" in repr_str
        assert "Test" in repr_str

    def test_task_title_modification(self):
        """Task title should be modifiable."""
        task = Task(id=1, title="Original")
        task.title = "Modified"

        assert task.title == "Modified"

    def test_task_completed_modification(self):
        """Task completed status should be modifiable."""
        task = Task(id=1, title="Test")
        task.completed = True

        assert task.completed is True
