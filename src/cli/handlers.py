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

    description = input("Enter description (optional, press Enter to skip): ")

    try:
        task = manager.add_task(title, description)
        print(f"Task added successfully! (ID: {task.id})")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)


def handle_toggle_status(manager: TaskManager) -> None:
    """Handle the Toggle Status operation (complete/incomplete).

    Args:
        manager: The TaskManager instance.
    """
    task_id_str = prompt_for_task_id("toggle status")

    is_valid, task_id, error = validate_task_id(task_id_str)
    if not is_valid:
        print(f"Error: {error}", file=sys.stderr)
        return

    task = manager.get_task(task_id)
    if task is None:
        print("Error: Task not found", file=sys.stderr)
        return

    success, new_status = manager.toggle_status(task_id)
    if success:
        print(f"Task status changed to '{new_status}'!\nID: {task.id}\nTitle: {task.title}")


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

    print(f"Current title: {task.title}")
    print(f"Current description: {task.description or '(none)'}")

    new_title = input("Enter new title (press Enter to keep current): ")
    new_description = input("Enter new description (press Enter to keep current): ")

    # Use None if user didn't enter anything (keep existing)
    title_to_update = new_title if new_title else None
    desc_to_update = new_description if new_description else None

    if title_to_update is not None:
        is_valid, error = validate_title(title_to_update)
        if not is_valid:
            print(f"Error: {error}", file=sys.stderr)
            return

    if title_to_update is None and desc_to_update is None:
        print("No changes made.")
        return

    try:
        manager.update_task(task_id, title_to_update, desc_to_update)
        print(f"Task updated successfully! (ID: {task.id})")
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
