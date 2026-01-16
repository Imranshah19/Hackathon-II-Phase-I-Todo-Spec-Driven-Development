"""Integration tests for CLI workflows."""

import pytest
from io import StringIO
from unittest.mock import patch

from src.services.task_manager import TaskManager
from src.cli.handlers import (
    handle_add_task,
    handle_view_tasks,
    handle_toggle_status,
    handle_update_task,
    handle_delete_task,
)


class TestAddViewWorkflow:
    """Integration tests for add-view workflow (T054)."""

    def test_add_task_then_view_shows_task(self, capsys):
        """Adding a task and viewing should show the task."""
        manager = TaskManager()

        # Add task (title + optional description)
        with patch("builtins.input", side_effect=["Buy groceries", ""]):
            handle_add_task(manager)

        # View tasks
        handle_view_tasks(manager)

        captured = capsys.readouterr()
        assert "Task added successfully!" in captured.out
        assert "Buy groceries" in captured.out
        assert "[1] Buy groceries — pending" in captured.out

    def test_add_multiple_tasks_shows_all(self, capsys):
        """Adding multiple tasks should show all in order."""
        manager = TaskManager()

        # Add tasks (each with title + optional description)
        with patch("builtins.input", side_effect=["First task", "", "Second task", ""]):
            handle_add_task(manager)
            handle_add_task(manager)

        # View tasks
        handle_view_tasks(manager)

        captured = capsys.readouterr()
        assert "[1] First task — pending" in captured.out
        assert "[2] Second task — pending" in captured.out
        assert "Total: 2 tasks" in captured.out


class TestToggleStatusWorkflow:
    """Integration tests for toggle-status workflow (T055)."""

    def test_add_and_toggle_complete_shows_status_change(self, capsys):
        """Adding a task and toggling complete should show completed status."""
        manager = TaskManager()

        # Add task (title + optional description)
        with patch("builtins.input", side_effect=["Test task", ""]):
            handle_add_task(manager)

        # Toggle to complete
        with patch("builtins.input", return_value="1"):
            handle_toggle_status(manager)

        # View tasks
        handle_view_tasks(manager)

        captured = capsys.readouterr()
        assert "Task status changed to 'completed'!" in captured.out
        assert "[1] Test task — completed" in captured.out
        assert "1 completed" in captured.out

    def test_toggle_back_to_pending(self, capsys):
        """Toggling a completed task should show pending status."""
        manager = TaskManager()

        # Add task (title + optional description)
        with patch("builtins.input", side_effect=["Test task", ""]):
            handle_add_task(manager)

        # Toggle to complete
        with patch("builtins.input", return_value="1"):
            handle_toggle_status(manager)

        # Toggle back to pending
        with patch("builtins.input", return_value="1"):
            handle_toggle_status(manager)

        # View tasks
        handle_view_tasks(manager)

        captured = capsys.readouterr()
        assert "Task status changed to 'pending'!" in captured.out
        assert "[1] Test task — pending" in captured.out


class TestUpdateWorkflow:
    """Integration tests for update workflow (T056)."""

    def test_add_and_update_shows_new_title(self, capsys):
        """Adding a task and updating should show new title."""
        manager = TaskManager()

        # Add task (title + optional description)
        with patch("builtins.input", side_effect=["Original title", ""]):
            handle_add_task(manager)

        # Update task (id, new_title, new_description)
        with patch("builtins.input", side_effect=["1", "Updated title", ""]):
            handle_update_task(manager)

        # View tasks
        handle_view_tasks(manager)

        captured = capsys.readouterr()
        assert "Task updated successfully!" in captured.out
        assert "Updated title" in captured.out

    def test_add_and_update_description(self, capsys):
        """Adding a task and updating description should show new description."""
        manager = TaskManager()

        # Add task (title + optional description)
        with patch("builtins.input", side_effect=["Test task", "Original description"]):
            handle_add_task(manager)

        # Update task (id, new_title='', new_description='Updated description')
        with patch("builtins.input", side_effect=["1", "", "Updated description"]):
            handle_update_task(manager)

        # View tasks
        handle_view_tasks(manager)

        captured = capsys.readouterr()
        assert "Task updated successfully!" in captured.out
        assert "Updated description" in captured.out


class TestDeleteWorkflow:
    """Integration tests for delete workflow (T057)."""

    def test_add_and_delete_removes_task(self, capsys):
        """Adding a task and deleting should remove from list."""
        manager = TaskManager()

        # Add task (title + optional description)
        with patch("builtins.input", side_effect=["Task to delete", ""]):
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
            handle_toggle_status(manager)

        captured = capsys.readouterr()
        assert "must be a number" in captured.err

    def test_nonexistent_task_id_shows_error(self, capsys):
        """Non-existent task ID should show error without crashing."""
        manager = TaskManager()

        with patch("builtins.input", return_value="999"):
            handle_toggle_status(manager)

        captured = capsys.readouterr()
        assert "Task not found" in captured.err

    def test_negative_task_id_shows_error(self, capsys):
        """Negative task ID should show error without crashing."""
        manager = TaskManager()

        with patch("builtins.input", return_value="-1"):
            handle_delete_task(manager)

        captured = capsys.readouterr()
        assert "must be a positive number" in captured.err
