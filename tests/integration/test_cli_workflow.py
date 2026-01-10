"""Integration tests for CLI workflows."""

import pytest
from io import StringIO
from unittest.mock import patch

from src.services.task_manager import TaskManager
from src.cli.handlers import (
    handle_add_task,
    handle_view_tasks,
    handle_mark_complete,
    handle_update_task,
    handle_delete_task,
)


class TestAddViewWorkflow:
    """Integration tests for add-view workflow (T054)."""

    def test_add_task_then_view_shows_task(self, capsys):
        """Adding a task and viewing should show the task."""
        manager = TaskManager()

        # Add task
        with patch("builtins.input", return_value="Buy groceries"):
            handle_add_task(manager)

        # View tasks
        handle_view_tasks(manager)

        captured = capsys.readouterr()
        assert "Task added successfully!" in captured.out
        assert "Buy groceries" in captured.out
        assert "[ ] 1. Buy groceries" in captured.out

    def test_add_multiple_tasks_shows_all(self, capsys):
        """Adding multiple tasks should show all in order."""
        manager = TaskManager()

        # Add tasks
        with patch("builtins.input", side_effect=["First task", "Second task"]):
            handle_add_task(manager)
            handle_add_task(manager)

        # View tasks
        handle_view_tasks(manager)

        captured = capsys.readouterr()
        assert "[ ] 1. First task" in captured.out
        assert "[ ] 2. Second task" in captured.out
        assert "Total: 2 tasks" in captured.out


class TestMarkCompleteWorkflow:
    """Integration tests for mark-complete workflow (T055)."""

    def test_add_and_mark_complete_shows_status_change(self, capsys):
        """Adding a task and marking complete should show [x] status."""
        manager = TaskManager()

        # Add task
        with patch("builtins.input", return_value="Test task"):
            handle_add_task(manager)

        # Mark complete
        with patch("builtins.input", return_value="1"):
            handle_mark_complete(manager)

        # View tasks
        handle_view_tasks(manager)

        captured = capsys.readouterr()
        assert "Task marked as complete!" in captured.out
        assert "[x] 1. Test task" in captured.out
        assert "1 completed" in captured.out


class TestUpdateWorkflow:
    """Integration tests for update workflow (T056)."""

    def test_add_and_update_shows_new_title(self, capsys):
        """Adding a task and updating should show new title."""
        manager = TaskManager()

        # Add task
        with patch("builtins.input", return_value="Original title"):
            handle_add_task(manager)

        # Update task
        with patch("builtins.input", side_effect=["1", "Updated title"]):
            handle_update_task(manager)

        # View tasks
        handle_view_tasks(manager)

        captured = capsys.readouterr()
        assert "Task updated successfully!" in captured.out
        assert "Updated title" in captured.out
        assert "Original title" not in captured.out.split("Task updated")[1]


class TestDeleteWorkflow:
    """Integration tests for delete workflow (T057)."""

    def test_add_and_delete_removes_task(self, capsys):
        """Adding a task and deleting should remove from list."""
        manager = TaskManager()

        # Add task
        with patch("builtins.input", return_value="Task to delete"):
            handle_add_task(manager)

        # Delete task
        with patch("builtins.input", return_value="1"):
            handle_delete_task(manager)

        # View tasks
        handle_view_tasks(manager)

        captured = capsys.readouterr()
        assert "Task deleted successfully!" in captured.out
        assert "No tasks found" in captured.out


class TestInvalidInputHandling:
    """Integration tests for invalid input handling (T058)."""

    def test_empty_title_shows_error(self, capsys):
        """Empty title should show error without crashing."""
        manager = TaskManager()

        with patch("builtins.input", return_value=""):
            handle_add_task(manager)

        captured = capsys.readouterr()
        assert "cannot be empty" in captured.err

    def test_invalid_task_id_shows_error(self, capsys):
        """Invalid task ID should show error without crashing."""
        manager = TaskManager()

        with patch("builtins.input", return_value="abc"):
            handle_mark_complete(manager)

        captured = capsys.readouterr()
        assert "must be a number" in captured.err

    def test_nonexistent_task_id_shows_error(self, capsys):
        """Non-existent task ID should show error without crashing."""
        manager = TaskManager()

        with patch("builtins.input", return_value="999"):
            handle_mark_complete(manager)

        captured = capsys.readouterr()
        assert "Task not found" in captured.err

    def test_negative_task_id_shows_error(self, capsys):
        """Negative task ID should show error without crashing."""
        manager = TaskManager()

        with patch("builtins.input", return_value="-1"):
            handle_delete_task(manager)

        captured = capsys.readouterr()
        assert "must be a positive number" in captured.err
