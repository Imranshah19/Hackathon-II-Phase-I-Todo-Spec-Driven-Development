"""Unit tests for the Task dataclass."""

import pytest
from src.models.task import Task


class TestTask:
    """Tests for Task dataclass."""

    def test_task_creation_with_defaults(self):
        """Task should have status='pending' by default."""
        task = Task(id=1, title="Test task")

        assert task.id == 1
        assert task.title == "Test task"
        assert task.status == "pending"
        assert task.description == ""
        assert task.completed is False

    def test_task_creation_with_completed_status(self):
        """Task should accept status parameter."""
        task = Task(id=2, title="Completed task", status="completed")

        assert task.id == 2
        assert task.title == "Completed task"
        assert task.status == "completed"
        assert task.completed is True

    def test_task_creation_with_description(self):
        """Task should accept description parameter."""
        task = Task(id=1, title="Test task", description="A detailed description")

        assert task.description == "A detailed description"

    def test_task_equality(self):
        """Tasks with same attributes should be equal."""
        task1 = Task(id=1, title="Same task", status="pending")
        task2 = Task(id=1, title="Same task", status="pending")

        assert task1 == task2

    def test_task_inequality_different_id(self):
        """Tasks with different IDs should not be equal."""
        task1 = Task(id=1, title="Same title")
        task2 = Task(id=2, title="Same title")

        assert task1 != task2

    def test_task_repr(self):
        """Task should have useful string representation."""
        task = Task(id=1, title="Test", status="completed")

        repr_str = repr(task)
        assert "Task" in repr_str
        assert "1" in repr_str
        assert "Test" in repr_str

    def test_task_title_modification(self):
        """Task title should be modifiable."""
        task = Task(id=1, title="Original")
        task.title = "Modified"

        assert task.title == "Modified"

    def test_task_status_modification(self):
        """Task status should be modifiable."""
        task = Task(id=1, title="Test")
        task.status = "completed"

        assert task.status == "completed"
        assert task.completed is True

    def test_completed_property_reflects_status(self):
        """completed property should reflect status value."""
        task = Task(id=1, title="Test", status="pending")
        assert task.completed is False

        task.status = "completed"
        assert task.completed is True

        task.status = "pending"
        assert task.completed is False
