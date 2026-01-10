# Data Model: In-Memory Console Todo App

**Date**: 2026-01-10
**Feature**: 001-console-todo-app

## Entity Overview

```text
┌─────────────────────────────────────┐
│              Task                   │
├─────────────────────────────────────┤
│ id: int (PK, auto-increment)        │
│ title: str (1-200 chars)            │
│ completed: bool (default: False)    │
└─────────────────────────────────────┘
```

## Entities

### Task

Represents a single todo item in the application.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | `int` | Primary key, auto-increment, ≥1 | Unique identifier assigned by system |
| `title` | `str` | Not empty, 1-200 characters | User-provided task description |
| `completed` | `bool` | Default: `False` | Whether task is marked complete |

**Business Rules**:
- ID is immutable after creation
- ID starts at 1 and increments by 1 for each new task
- IDs are never reused after task deletion
- Title can be updated after creation
- Completed status can only transition from `False` → `True` (marking complete is one-way)

**Python Implementation**:

```python
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
```

## State Diagram

```text
                    ┌──────────────┐
     add_task()     │              │
    ────────────────►   PENDING    │
                    │ (completed=  │
                    │    False)    │
                    └──────┬───────┘
                           │
                           │ mark_complete()
                           ▼
                    ┌──────────────┐
                    │              │
                    │  COMPLETED   │
                    │ (completed=  │
                    │    True)     │
                    └──────────────┘
```

**Notes**:
- Tasks can be deleted from any state
- Tasks can be updated (title) in any state
- No "uncomplete" operation in Phase I (one-way transition)

## Storage Model

### In-Memory Storage

```python
class TaskManager:
    """Manages in-memory task storage and operations.

    Attributes:
        _tasks: Dictionary mapping task IDs to Task objects.
        _next_id: Counter for generating unique task IDs.
    """
    _tasks: dict[int, Task]
    _next_id: int  # Starts at 1
```

**Memory Layout**:

```text
TaskManager
├── _tasks: {
│       1: Task(id=1, title="Buy groceries", completed=False),
│       2: Task(id=2, title="Call mom", completed=True),
│       3: Task(id=3, title="Finish report", completed=False)
│   }
└── _next_id: 4
```

## Validation Rules

### Task Title Validation

| Rule | Implementation | Error Message |
|------|----------------|---------------|
| Not empty | `len(title.strip()) > 0` | "Task title cannot be empty" |
| Not whitespace-only | `title.strip() != ""` | "Task title cannot be empty" |
| Maximum length | `len(title) <= 200` | "Task title exceeds maximum length (200 characters)" |
| Printable characters | All printable chars accepted | N/A |

### Task ID Validation

| Rule | Implementation | Error Message |
|------|----------------|---------------|
| Is integer | `isinstance(input, int)` or parseable | "Invalid task ID: must be a number" |
| Is positive | `id >= 1` | "Invalid task ID: must be a positive number" |
| Exists in storage | `id in _tasks` | "Task not found" |

## CRUD Operations

### Create (Add Task)

```python
def add_task(self, title: str) -> Task:
    """Create a new task with the given title.

    Args:
        title: Task description (1-200 chars, not empty).

    Returns:
        The newly created Task with assigned ID.

    Raises:
        ValueError: If title is empty or exceeds 200 characters.
    """
```

### Read (View Tasks)

```python
def get_all_tasks(self) -> list[Task]:
    """Return all tasks ordered by ID.

    Returns:
        List of all tasks, empty list if no tasks exist.
    """

def get_task(self, task_id: int) -> Task | None:
    """Retrieve a task by ID.

    Args:
        task_id: The ID of the task to retrieve.

    Returns:
        The Task if found, None otherwise.
    """
```

### Update (Update Task Title)

```python
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
```

### Update (Mark Complete)

```python
def mark_complete(self, task_id: int) -> bool:
    """Mark a task as complete.

    Args:
        task_id: The ID of the task to mark complete.

    Returns:
        True if task was marked complete, False if task not found
        or already complete.
    """
```

### Delete (Delete Task)

```python
def delete_task(self, task_id: int) -> Task | None:
    """Delete a task by ID.

    Args:
        task_id: The ID of the task to delete.

    Returns:
        The deleted Task if found, None otherwise.
    """
```

## Future Extensions (Phase II+)

The data model is designed to accommodate future requirements:

| Phase | Extension | Model Change |
|-------|-----------|--------------|
| II | Persistence | Add `created_at`, `updated_at` timestamps |
| II | Multi-user | Add `user_id` foreign key |
| II | Database | Add SQLModel/SQLAlchemy ORM decorators |
| III | AI features | Add `priority`, `due_date`, `tags` fields |
