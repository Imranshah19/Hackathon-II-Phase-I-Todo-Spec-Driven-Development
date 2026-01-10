"""Task management service for CRUD operations."""

from src.models.task import Task
from src.utils.validators import validate_title, validate_task_id


class TaskManager:
    """Manages in-memory task storage and operations.

    Attributes:
        _tasks: Dictionary mapping task IDs to Task objects.
        _next_id: Counter for generating unique task IDs.
    """

    def __init__(self) -> None:
        """Initialize an empty task manager."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def get_all_tasks(self) -> list[Task]:
        """Return all tasks ordered by ID.

        Returns:
            List of all tasks sorted by ID, empty list if no tasks exist.
        """
        return sorted(self._tasks.values(), key=lambda task: task.id)

    def add_task(self, title: str) -> Task:
        """Create a new task with the given title.

        Args:
            title: Task description (1-200 chars, not empty).

        Returns:
            The newly created Task with assigned ID.

        Raises:
            ValueError: If title is empty or exceeds 200 characters.
        """
        is_valid, error = validate_title(title)
        if not is_valid:
            raise ValueError(error)

        task = Task(id=self._next_id, title=title)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Task | None:
        """Retrieve a task by ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            The Task if found, None otherwise.
        """
        return self._tasks.get(task_id)

    def mark_complete(self, task_id: int) -> bool:
        """Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete.

        Returns:
            True if task was marked complete, False if task not found
            or already complete.
        """
        task = self.get_task(task_id)
        if task is None:
            return False
        if task.completed:
            return False
        task.completed = True
        return True

    def update_task(self, task_id: int, new_title: str) -> bool:
        """Update the title of an existing task.

        Args:
            task_id: The ID of the task to update.
            new_title: The new title (1-200 chars, not empty).

        Returns:
            True if task was updated, False if task not found.

        Raises:
            ValueError: If new_title is empty or exceeds 200 characters.
        """
        is_valid, error = validate_title(new_title)
        if not is_valid:
            raise ValueError(error)

        task = self.get_task(task_id)
        if task is None:
            return False

        task.title = new_title
        return True

    def delete_task(self, task_id: int) -> Task | None:
        """Delete a task by ID.

        Args:
            task_id: The ID of the task to delete.

        Returns:
            The deleted Task if found, None otherwise.
        """
        return self._tasks.pop(task_id, None)
