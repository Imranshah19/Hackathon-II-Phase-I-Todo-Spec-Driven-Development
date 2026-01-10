"""Unit tests for TaskManager service."""

import pytest
from src.services.task_manager import TaskManager
from src.models.task import Task


class TestGetAllTasks:
    """Tests for get_all_tasks method (User Story 1)."""

    def test_get_all_tasks_empty(self):
        """get_all_tasks should return empty list when no tasks exist."""
        manager = TaskManager()

        result = manager.get_all_tasks()

        assert result == []
        assert isinstance(result, list)

    def test_get_all_tasks_returns_tasks_ordered_by_id(self):
        """get_all_tasks should return tasks ordered by ID."""
        manager = TaskManager()
        # Add tasks (implementation will be in T028)
        manager._tasks[1] = Task(id=1, title="First task")
        manager._tasks[3] = Task(id=3, title="Third task")
        manager._tasks[2] = Task(id=2, title="Second task")

        result = manager.get_all_tasks()

        assert len(result) == 3
        assert result[0].id == 1
        assert result[1].id == 2
        assert result[2].id == 3


class TestAddTask:
    """Tests for add_task method (User Story 2)."""

    def test_add_task_creates_task_with_auto_increment_id(self):
        """add_task should create task with auto-incrementing ID."""
        manager = TaskManager()

        task1 = manager.add_task("First task")
        task2 = manager.add_task("Second task")

        assert task1.id == 1
        assert task2.id == 2
        assert task1.title == "First task"
        assert task2.title == "Second task"
        assert task1.completed is False
        assert task2.completed is False

    def test_add_task_rejects_empty_title(self):
        """add_task should raise ValueError for empty title."""
        manager = TaskManager()

        with pytest.raises(ValueError) as exc_info:
            manager.add_task("")

        assert "cannot be empty" in str(exc_info.value)

    def test_add_task_rejects_title_over_200_chars(self):
        """add_task should raise ValueError for title exceeding 200 characters."""
        manager = TaskManager()
        long_title = "x" * 201

        with pytest.raises(ValueError) as exc_info:
            manager.add_task(long_title)

        assert "exceeds maximum length" in str(exc_info.value)


class TestMarkComplete:
    """Tests for mark_complete method (User Story 3)."""

    def test_mark_complete_changes_task_status(self):
        """mark_complete should change task completed status to True."""
        manager = TaskManager()
        task = manager.add_task("Test task")

        result = manager.mark_complete(task.id)

        assert result is True
        assert task.completed is True

    def test_mark_complete_returns_false_for_nonexistent_id(self):
        """mark_complete should return False for non-existent task ID."""
        manager = TaskManager()

        result = manager.mark_complete(999)

        assert result is False

    def test_mark_complete_handles_already_complete_task(self):
        """mark_complete should return False if task already complete."""
        manager = TaskManager()
        task = manager.add_task("Test task")
        manager.mark_complete(task.id)  # First mark

        result = manager.mark_complete(task.id)  # Second mark

        assert result is False
        assert task.completed is True


class TestUpdateTask:
    """Tests for update_task method (User Story 4)."""

    def test_update_task_changes_title(self):
        """update_task should change the task title."""
        manager = TaskManager()
        task = manager.add_task("Original title")

        result = manager.update_task(task.id, "New title")

        assert result is True
        assert task.title == "New title"

    def test_update_task_returns_false_for_nonexistent_id(self):
        """update_task should return False for non-existent task ID."""
        manager = TaskManager()

        result = manager.update_task(999, "New title")

        assert result is False

    def test_update_task_rejects_empty_new_title(self):
        """update_task should raise ValueError for empty new title."""
        manager = TaskManager()
        task = manager.add_task("Original title")

        with pytest.raises(ValueError) as exc_info:
            manager.update_task(task.id, "")

        assert "cannot be empty" in str(exc_info.value)
        assert task.title == "Original title"  # Title unchanged


class TestDeleteTask:
    """Tests for delete_task method (User Story 5)."""

    def test_delete_task_removes_task_from_storage(self):
        """delete_task should remove task and return the deleted task."""
        manager = TaskManager()
        task = manager.add_task("Task to delete")

        deleted = manager.delete_task(task.id)

        assert deleted is not None
        assert deleted.id == task.id
        assert deleted.title == "Task to delete"
        assert manager.get_task(task.id) is None

    def test_delete_task_returns_none_for_nonexistent_id(self):
        """delete_task should return None for non-existent task ID."""
        manager = TaskManager()

        result = manager.delete_task(999)

        assert result is None
