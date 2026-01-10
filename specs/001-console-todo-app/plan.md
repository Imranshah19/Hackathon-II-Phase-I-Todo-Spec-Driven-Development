# Implementation Plan: In-Memory Console Todo App

**Branch**: `001-console-todo-app` | **Date**: 2026-01-10 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-console-todo-app/spec.md`

## Summary

Build an in-memory Python console todo application supporting 5 core operations (Add, View, Update, Mark Complete, Delete) with a menu-driven CLI interface. The application stores tasks in memory using a dictionary keyed by auto-incrementing task IDs. All user inputs are validated before processing, with clear error messages for invalid operations.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (standard library only)
**Storage**: In-memory dictionary (dict[int, Task])
**Testing**: pytest
**Target Platform**: Cross-platform console (Windows, macOS, Linux)
**Project Type**: Single project (CLI application)
**Performance Goals**: <2 seconds startup; instant response for all operations
**Constraints**: No external dependencies; no persistent storage; single-user
**Scale/Scope**: Single-user, unlimited tasks (memory-bound)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Checkpoint | Status |
|-----------|-----------|--------|
| I. Reliability | Feature maintains existing phase functionality; acceptance criteria defined | [x] |
| II. Maintainability | Modular design; single responsibility; documented interfaces | [x] |
| III. Security & Privacy | No hardcoded secrets; data encryption plan (if applicable) | [x] N/A for Phase I |
| IV. Reproducibility | Dependencies declared; setup documented; deterministic builds | [x] |
| V. Scalability | Stateless services where possible; multi-user data model (Phase II+) | [x] N/A for Phase I |

## Project Structure

### Documentation (this feature)

```text
specs/001-console-todo-app/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (CLI interface contract)
│   └── cli-interface.md
├── checklists/
│   └── requirements.md  # Spec validation checklist
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── main.py              # Application entry point
├── models/
│   ├── __init__.py
│   └── task.py          # Task dataclass
├── services/
│   ├── __init__.py
│   └── task_manager.py  # TaskManager class with CRUD operations
├── cli/
│   ├── __init__.py
│   ├── menu.py          # Menu display and navigation
│   └── handlers.py      # Command handlers for each operation
└── utils/
    ├── __init__.py
    └── validators.py    # Input validation functions

tests/
├── __init__.py
├── unit/
│   ├── __init__.py
│   ├── test_task.py
│   ├── test_task_manager.py
│   └── test_validators.py
└── integration/
    ├── __init__.py
    └── test_cli_workflow.py
```

**Structure Decision**: Single project structure selected as this is a standalone CLI application with no frontend/backend separation. The modular layout (models, services, cli, utils) supports the Maintainability principle and enables clean separation of concerns for future phases.

## Architecture Decisions

### AD-001: In-Memory Storage with Dictionary

**Decision**: Use `dict[int, Task]` for task storage with auto-incrementing integer keys.

**Rationale**:
- O(1) lookup by ID for update/delete/mark complete operations
- Simple iteration for view all tasks
- Auto-increment counter ensures unique IDs
- No external dependencies required

**Alternatives Considered**:
- List with linear search: Rejected due to O(n) lookups
- SQLite in-memory: Rejected as over-engineered for Phase I requirements

### AD-002: Dataclass for Task Model

**Decision**: Use Python `@dataclass` for the Task model with type hints.

**Rationale**:
- Clean, concise syntax for data containers
- Built-in `__init__`, `__repr__`, `__eq__`
- Type hints support IDE autocompletion and static analysis
- Easy to extend for Phase II (add fields like `created_at`, `user_id`)

### AD-003: Menu-Driven CLI with Numbered Options

**Decision**: Implement numbered menu options (1-6) rather than command parsing.

**Rationale**:
- Simpler for first-time users
- No need for argument parsing libraries
- Matches spec requirement for "intuitive prompts"
- Standard input/output works across all platforms

## Module Specifications

### Task Model (`src/models/task.py`)

```python
@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
```

**Responsibilities**:
- Represent a single todo item
- Immutable ID after creation
- Mutable title and completion status

### TaskManager (`src/services/task_manager.py`)

**Responsibilities**:
- Maintain in-memory task storage
- Generate unique task IDs
- Perform CRUD operations
- Return operation results with success/failure indicators

**Methods**:
- `add_task(title: str) -> Task`: Create and store new task
- `get_task(task_id: int) -> Task | None`: Retrieve task by ID
- `get_all_tasks() -> list[Task]`: Return all tasks
- `update_task(task_id: int, new_title: str) -> bool`: Update task title
- `mark_complete(task_id: int) -> bool`: Mark task as complete
- `delete_task(task_id: int) -> bool`: Remove task from storage

### CLI Module (`src/cli/`)

**Responsibilities**:
- Display menu options
- Capture and validate user input
- Route commands to TaskManager
- Display operation results and error messages

### Validators (`src/utils/validators.py`)

**Responsibilities**:
- Validate task titles (non-empty, not whitespace-only, ≤200 chars)
- Validate task IDs (positive integers)
- Return validation results with error messages

## Complexity Tracking

> No violations identified. Design follows constitution principles.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Input encoding issues with special characters | Low | Low | Use UTF-8 encoding; test with Unicode input |
| Memory exhaustion with many tasks | Low | Medium | Document memory constraints; add optional task limit |
| Platform-specific terminal behavior | Medium | Low | Test on Windows, macOS, Linux; use standard I/O |
