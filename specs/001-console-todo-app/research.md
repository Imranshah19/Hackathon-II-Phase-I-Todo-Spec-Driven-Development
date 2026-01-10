# Research: In-Memory Console Todo App

**Date**: 2026-01-10
**Feature**: 001-console-todo-app
**Status**: Complete

## Research Summary

No NEEDS CLARIFICATION items were present in the specification. This document records technical decisions made during planning based on constitution requirements and best practices.

## Technical Decisions

### TD-001: Python Version Selection

**Decision**: Python 3.13+

**Rationale**:
- User constraint specified Python >= 3.13
- Constitution Phase I standard specifies "Python 3.x"
- Python 3.13 provides improved error messages and performance
- Dataclasses and type hints are mature in 3.13

**Alternatives Considered**:
- Python 3.11/3.12: Would satisfy spec but user explicitly requested 3.13+

### TD-002: No External Dependencies

**Decision**: Use only Python standard library

**Rationale**:
- Spec constraint: "No external databases or file storage"
- Constitution Reproducibility principle: Dependencies must be declared
- Simpler setup for users; no pip install required beyond Python
- All required functionality (I/O, data structures) available in stdlib

**Alternatives Considered**:
- Click/Typer for CLI: Rejected as over-engineered for menu-based interface
- Rich for terminal formatting: Optional enhancement for future; not required for MVP

### TD-003: Testing Framework

**Decision**: pytest

**Rationale**:
- Constitution Phase I standard explicitly specifies pytest
- Industry standard for Python testing
- Simple assertion syntax
- Excellent fixture support for test setup

**Alternatives Considered**:
- unittest: Built-in but more verbose; pytest preferred per constitution

### TD-004: In-Memory Data Structure

**Decision**: Dictionary with integer keys (`dict[int, Task]`)

**Rationale**:
- O(1) lookup for task operations by ID
- Natural fit for auto-incrementing integer IDs
- Simple to iterate for "view all" operation
- No external storage required per spec

**Alternatives Considered**:
- List with index: Fragile; deletion shifts indices
- OrderedDict: Unnecessary; insertion order preserved in Python 3.7+
- Named tuple storage: Less flexible than dataclass for future extensions

### TD-005: Task ID Generation

**Decision**: Auto-incrementing counter starting at 1

**Rationale**:
- Spec requires "unique numeric ID starting from 1, incrementing"
- Simple counter variable in TaskManager
- IDs never reused after deletion (per spec assumption)

**Implementation**:
```python
class TaskManager:
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str) -> Task:
        task = Task(id=self._next_id, title=title)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task
```

### TD-006: Input Validation Strategy

**Decision**: Centralized validators module with pure functions

**Rationale**:
- Constitution Maintainability: Single responsibility principle
- Easy to unit test in isolation
- Reusable across CLI handlers
- Clear separation from business logic

**Validation Rules**:
| Input | Rule | Error Message |
|-------|------|---------------|
| Task title | Non-empty, non-whitespace | "Task title cannot be empty" |
| Task title | ≤200 characters | "Task title exceeds maximum length (200 characters)" |
| Task ID | Positive integer | "Invalid task ID: must be a positive number" |
| Menu choice | Integer 1-6 | "Invalid option: please enter a number 1-6" |

### TD-007: CLI Menu Structure

**Decision**: Numbered menu with continuous loop until exit

**Rationale**:
- Spec requires intuitive prompts and clear messages
- Numbered options are universally understood
- Loop pattern common for interactive CLI apps
- Easy to test programmatically

**Menu Layout**:
```text
=== Todo App ===
1. Add Task
2. View Tasks
3. Update Task
4. Mark Complete
5. Delete Task
6. Exit

Enter choice (1-6):
```

## Best Practices Applied

### Python Code Style

- Follow PEP 8 naming conventions
- Use type hints on all function signatures
- Document public functions with docstrings
- Maximum line length: 88 characters (black formatter default)

### Project Organization

- Flat package structure for simplicity
- `__init__.py` files for proper package imports
- Separate test directory mirroring source structure
- Entry point in `main.py` for clarity

### Error Handling

- Never crash on invalid input
- Return meaningful error messages
- Use exceptions for exceptional cases only
- Validate at system boundary (CLI input)

## Open Questions

None. All technical decisions are resolved.

## References

- [Python 3.13 Release Notes](https://docs.python.org/3.13/whatsnew/3.13.html)
- [pytest Documentation](https://docs.pytest.org/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Python Dataclasses](https://docs.python.org/3/library/dataclasses.html)
