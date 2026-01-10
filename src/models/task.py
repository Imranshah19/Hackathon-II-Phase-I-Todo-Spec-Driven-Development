"""Task data model for the todo application."""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a single todo item.

    Attributes:
        id: Unique identifier assigned by TaskManager (immutable).
        title: User-provided task description (1-200 characters).
        completed: Whether the task is marked as complete.
    """

    id: int
    title: str
    completed: bool = False
