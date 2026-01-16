"""Task data model for the todo application."""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a single todo item.

    Attributes:
        id: Unique identifier assigned by TaskManager (immutable).
        title: User-provided task title (1-200 characters).
        description: Optional task description.
        status: Task status - either "pending" or "completed".
    """

    id: int
    title: str
    description: str = ""
    status: str = "pending"

    @property
    def completed(self) -> bool:
        """Check if task is completed (for backwards compatibility)."""
        return self.status == "completed"
