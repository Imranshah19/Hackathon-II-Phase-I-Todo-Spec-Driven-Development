"""Menu display and input functions for the CLI."""

from src.models.task import Task

MENU_OPTIONS = """=== Todo App ===
1. Add Task
2. View Tasks
3. Update Task
4. Mark Complete
5. Delete Task
6. Exit

Enter choice (1-6): """


def display_menu() -> None:
    """Display the main menu options."""
    print(MENU_OPTIONS, end="")


def format_task_list(tasks: list[Task]) -> str:
    """Format a list of tasks for display.

    Args:
        tasks: List of Task objects to format.

    Returns:
        Formatted string showing all tasks with status indicators.
    """
    if not tasks:
        return "No tasks found. Add a task to get started!"

    lines = ["=== Your Tasks ==="]
    completed_count = 0

    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        lines.append(f"{status} {task.id}. {task.title}")
        if task.completed:
            completed_count += 1

    lines.append("==================")
    lines.append(f"Total: {len(tasks)} tasks ({completed_count} completed)")

    return "\n".join(lines)


def prompt_for_title() -> str:
    """Prompt user to enter a task title.

    Returns:
        The entered title string (may be empty/invalid).
    """
    return input("Enter task title: ")


def prompt_for_task_id(action: str) -> str:
    """Prompt user to enter a task ID.

    Args:
        action: The action being performed (e.g., 'update', 'delete', 'mark complete').

    Returns:
        The entered ID string (may be invalid).
    """
    return input(f"Enter task ID to {action}: ")
