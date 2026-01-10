"""Input validation functions for the todo application."""

MAX_TITLE_LENGTH = 200


def validate_title(title: str) -> tuple[bool, str]:
    """Validate a task title.

    Args:
        title: The title to validate.

    Returns:
        A tuple of (is_valid, error_message).
        If valid, error_message is empty string.
    """
    if not title or not title.strip():
        return False, "Task title cannot be empty"

    if len(title) > MAX_TITLE_LENGTH:
        return False, f"Task title exceeds maximum length ({MAX_TITLE_LENGTH} characters)"

    return True, ""


def validate_task_id(task_id_str: str) -> tuple[bool, int | None, str]:
    """Validate and parse a task ID string.

    Args:
        task_id_str: The task ID string to validate.

    Returns:
        A tuple of (is_valid, parsed_id, error_message).
        If valid, parsed_id is the integer ID and error_message is empty.
        If invalid, parsed_id is None.
    """
    try:
        task_id = int(task_id_str)
    except ValueError:
        return False, None, "Invalid task ID: must be a number"

    if task_id < 1:
        return False, None, "Invalid task ID: must be a positive number"

    return True, task_id, ""
