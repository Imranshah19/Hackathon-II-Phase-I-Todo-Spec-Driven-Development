"""Command handlers for CLI operations."""

import sys
from src.services.task_manager import TaskManager
from src.cli.menu import format_task_list, prompt_for_title, prompt_for_task_id
from src.utils.validators import validate_title, validate_task_id


def handle_view_tasks(manager: TaskManager) -> None:
    """Handle the View Tasks operation.

    Args:
        manager: The TaskManager instance.
    """
    tasks = manager.get_all_tasks()
    print(format_task_list(tasks))


def handle_add_task(manager: TaskManager) -> None:
    """Handle the Add Task operation.

    Args:
        manager: The TaskManager instance.
    """
    title = prompt_for_title()

    is_valid, error = validate_title(title)
    if not is_valid:
        print(f"Error: {error}", file=sys.stderr)
        return

    try:
        task = manager.add_task(title)
        print(f"Task added successfully! (ID: {task.id})")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)


def handle_mark_complete(manager: TaskManager) -> None:
    """Handle the Mark Complete operation.

    Args:
        manager: The TaskManager instance.
    """
    task_id_str = prompt_for_task_id("mark complete")

    is_valid, task_id, error = validate_task_id(task_id_str)
    if not is_valid:
        print(f"Error: {error}", file=sys.stderr)
        return

    task = manager.get_task(task_id)
    if task is None:
        print("Error: Task not found", file=sys.stderr)
        return

    if task.completed:
        print(f"Task is already complete.\nID: {task.id}\nTitle: {task.title}")
        return

    manager.mark_complete(task_id)
    print(f"Task marked as complete!\nID: {task.id}\nTitle: {task.title}")


def handle_update_task(manager: TaskManager) -> None:
    """Handle the Update Task operation.

    Args:
        manager: The TaskManager instance.
    """
    task_id_str = prompt_for_task_id("update")

    is_valid, task_id, error = validate_task_id(task_id_str)
    if not is_valid:
        print(f"Error: {error}", file=sys.stderr)
        return

    task = manager.get_task(task_id)
    if task is None:
        print("Error: Task not found", file=sys.stderr)
        return

    new_title = input("Enter new title: ")

    is_valid, error = validate_title(new_title)
    if not is_valid:
        print(f"Error: {error}", file=sys.stderr)
        return

    try:
        manager.update_task(task_id, new_title)
        print(f"Task updated successfully!\nID: {task.id}\nNew title: {new_title}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)


def handle_delete_task(manager: TaskManager) -> None:
    """Handle the Delete Task operation.

    Args:
        manager: The TaskManager instance.
    """
    task_id_str = prompt_for_task_id("delete")

    is_valid, task_id, error = validate_task_id(task_id_str)
    if not is_valid:
        print(f"Error: {error}", file=sys.stderr)
        return

    deleted = manager.delete_task(task_id)
    if deleted is None:
        print("Error: Task not found", file=sys.stderr)
        return

    print(f"Task deleted successfully!\nDeleted: {deleted.title}")


def handle_exit() -> None:
    """Handle the Exit operation."""
    print("Goodbye! Your tasks have not been saved.")
