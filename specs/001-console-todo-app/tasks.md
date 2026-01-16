# Tasks: In-Memory Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/cli-interface.md

**Tests**: Tests ARE included per Constitution Phase I standards ("Basic unit tests for core functionality").

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3, US4, US5, US6)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths follow plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure per plan.md in src/
- [x] T002 [P] Create src/__init__.py with package docstring
- [x] T003 [P] Create src/models/__init__.py
- [x] T004 [P] Create src/services/__init__.py
- [x] T005 [P] Create src/cli/__init__.py
- [x] T006 [P] Create src/utils/__init__.py
- [x] T007 [P] Create tests/__init__.py
- [x] T008 [P] Create tests/unit/__init__.py
- [x] T009 [P] Create tests/integration/__init__.py
- [x] T010 Create pyproject.toml with pytest configuration and Python 3.13+ requirement
- [x] T011 Create requirements-dev.txt with pytest dependency

**Checkpoint**: Project structure ready for implementation

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T012 Create Task dataclass in src/models/task.py with id, title, completed fields
- [x] T013 Create TaskManager class skeleton in src/services/task_manager.py with __init__ and storage dict
- [x] T014 [P] Create validate_title function in src/utils/validators.py (non-empty, max 200 chars)
- [x] T015 [P] Create validate_task_id function in src/utils/validators.py (positive integer)
- [x] T016 [P] Create tests/unit/test_task.py with Task dataclass tests
- [x] T017 [P] Create tests/unit/test_validators.py with validation function tests

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - View All Tasks (Priority: P1)

**Goal**: Users can view all tasks with ID, title, and completion status

**Independent Test**: Launch app, select "View Tasks", verify task list displays correctly (or "No tasks found" message)

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T018 [P] [US1] Create test for get_all_tasks() returning empty list in tests/unit/test_task_manager.py
- [x] T019 [P] [US1] Create test for get_all_tasks() returning tasks ordered by ID in tests/unit/test_task_manager.py

### Implementation for User Story 1

- [x] T020 [US1] Implement get_all_tasks() method in src/services/task_manager.py
- [x] T021 [US1] Create display_menu() function in src/cli/menu.py showing 6 options
- [x] T022 [US1] Create format_task_list() function in src/cli/menu.py with [ ]/[x] status indicators
- [x] T023 [US1] Create handle_view_tasks() function in src/cli/handlers.py
- [x] T024 [US1] Verify tests T018-T019 pass

**Checkpoint**: User Story 1 complete - can view tasks (empty list or with tasks)

---

## Phase 4: User Story 2 - Add New Task (Priority: P1)

**Goal**: Users can add tasks with validated titles, receiving confirmation with task ID

**Independent Test**: Add a task, view task list, verify new task appears with correct ID

### Tests for User Story 2

- [x] T025 [P] [US2] Create test for add_task() creating task with auto-increment ID in tests/unit/test_task_manager.py
- [x] T026 [P] [US2] Create test for add_task() rejecting empty title in tests/unit/test_task_manager.py
- [x] T027 [P] [US2] Create test for add_task() rejecting title over 200 chars in tests/unit/test_task_manager.py

### Implementation for User Story 2

- [x] T028 [US2] Implement add_task(title) method in src/services/task_manager.py with ID generation
- [x] T029 [US2] Create prompt_for_title() function in src/cli/menu.py
- [x] T030 [US2] Create handle_add_task() function in src/cli/handlers.py with validation
- [x] T031 [US2] Verify tests T025-T027 pass

**Checkpoint**: User Stories 1 AND 2 complete - can add and view tasks

---

## Phase 5: User Story 3 - Mark Task Complete (Priority: P2)

**Goal**: Users can mark tasks complete by ID, with proper error handling for invalid IDs

**Independent Test**: Add task, mark complete, view tasks to verify [x] status

### Tests for User Story 3

- [x] T032 [P] [US3] Create test for mark_complete() changing task status in tests/unit/test_task_manager.py
- [x] T033 [P] [US3] Create test for mark_complete() returning False for non-existent ID in tests/unit/test_task_manager.py
- [x] T034 [P] [US3] Create test for mark_complete() handling already-complete task in tests/unit/test_task_manager.py

### Implementation for User Story 3

- [x] T035 [US3] Implement get_task(task_id) method in src/services/task_manager.py
- [x] T036 [US3] Implement mark_complete(task_id) method in src/services/task_manager.py
- [x] T037 [US3] Create prompt_for_task_id() function in src/cli/menu.py with validation
- [x] T038 [US3] Create handle_mark_complete() function in src/cli/handlers.py
- [x] T039 [US3] Verify tests T032-T034 pass

**Checkpoint**: User Stories 1, 2, AND 3 complete - can add, view, and mark complete

---

## Phase 6: User Story 4 - Update Task Title (Priority: P2)

**Goal**: Users can update task titles by ID with validation

**Independent Test**: Add task, update title, view tasks to verify new title

### Tests for User Story 4

- [x] T040 [P] [US4] Create test for update_task() changing title in tests/unit/test_task_manager.py
- [x] T041 [P] [US4] Create test for update_task() returning False for non-existent ID in tests/unit/test_task_manager.py
- [x] T042 [P] [US4] Create test for update_task() rejecting empty new title in tests/unit/test_task_manager.py

### Implementation for User Story 4

- [x] T043 [US4] Implement update_task(task_id, new_title) method in src/services/task_manager.py
- [x] T044 [US4] Create handle_update_task() function in src/cli/handlers.py
- [x] T045 [US4] Verify tests T040-T042 pass

**Checkpoint**: User Stories 1-4 complete - can add, view, mark complete, and update

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Users can delete tasks by ID with confirmation

**Independent Test**: Add task, delete task, view tasks to verify removal

### Tests for User Story 5

- [x] T046 [P] [US5] Create test for delete_task() removing task from storage in tests/unit/test_task_manager.py
- [x] T047 [P] [US5] Create test for delete_task() returning None for non-existent ID in tests/unit/test_task_manager.py

### Implementation for User Story 5

- [x] T048 [US5] Implement delete_task(task_id) method in src/services/task_manager.py
- [x] T049 [US5] Create handle_delete_task() function in src/cli/handlers.py
- [x] T050 [US5] Verify tests T046-T047 pass

**Checkpoint**: User Stories 1-5 complete - all CRUD operations work

---

## Phase 8: User Story 6 - Exit Application (Priority: P3)

**Goal**: Users can exit the application gracefully with goodbye message

**Independent Test**: Select Exit option, verify goodbye message and clean termination

### Implementation for User Story 6

- [x] T051 [US6] Create handle_exit() function in src/cli/handlers.py with goodbye message
- [x] T052 [US6] Create main application loop in src/main.py integrating all handlers
- [x] T053 [US6] Add menu choice validation and error handling in src/main.py

**Checkpoint**: All user stories complete - full application functional

---

## Phase 9: Polish & Integration Testing

**Purpose**: Integration tests and final validation

- [x] T054 [P] Create tests/integration/test_cli_workflow.py with add-view workflow test
- [x] T055 [P] Create integration test for mark-complete workflow in tests/integration/test_cli_workflow.py
- [x] T056 [P] Create integration test for update workflow in tests/integration/test_cli_workflow.py
- [x] T057 [P] Create integration test for delete workflow in tests/integration/test_cli_workflow.py
- [x] T058 [P] Create integration test for invalid input handling in tests/integration/test_cli_workflow.py
- [x] T059 Run full test suite with pytest and verify all tests pass
- [x] T060 Run quickstart.md validation (manual walkthrough)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational - provides view capability
- **User Story 2 (Phase 4)**: Depends on Foundational - can run parallel to US1
- **User Story 3 (Phase 5)**: Depends on Foundational - can run parallel to US1/US2
- **User Story 4 (Phase 6)**: Depends on Foundational - can run parallel
- **User Story 5 (Phase 7)**: Depends on Foundational - can run parallel
- **User Story 6 (Phase 8)**: Depends on US1-US5 handlers existing (integrates all)
- **Polish (Phase 9)**: Depends on all user stories complete

### User Story Dependencies

```text
Phase 1 (Setup)
     │
     ▼
Phase 2 (Foundational) ──────────────────────────────────┐
     │                                                    │
     ├──────────┬──────────┬──────────┬──────────┐       │
     ▼          ▼          ▼          ▼          ▼       │
   US1        US2        US3        US4        US5       │
  (View)     (Add)    (Complete) (Update)   (Delete)     │
     │          │          │          │          │       │
     └──────────┴──────────┴──────────┴──────────┘       │
                           │                              │
                           ▼                              │
                    US6 (Exit + Main Loop) ◄──────────────┘
                           │
                           ▼
                    Phase 9 (Polish)
```

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Implementation follows: tests → service methods → CLI handlers
- Story complete before moving to integration

### Parallel Opportunities

- **Setup Phase**: T002-T009 can all run in parallel
- **Foundational Phase**: T014-T017 can run in parallel (after T012-T013)
- **User Stories 1-5**: Can all start simultaneously after Foundational
- **Within each story**: Test tasks marked [P] can run in parallel

---

## Parallel Example: Setup Phase

```bash
# Launch all __init__.py creation tasks together:
Task: "Create src/__init__.py with package docstring"
Task: "Create src/models/__init__.py"
Task: "Create src/services/__init__.py"
Task: "Create src/cli/__init__.py"
Task: "Create src/utils/__init__.py"
Task: "Create tests/__init__.py"
Task: "Create tests/unit/__init__.py"
Task: "Create tests/integration/__init__.py"
```

---

## Parallel Example: User Stories (Multi-Developer)

```bash
# After Foundational completes, launch all P1 stories:
Developer A: User Story 1 (View)
Developer B: User Story 2 (Add)

# Or launch all stories for solo developer in priority order:
Phase 3 (US1) → Phase 4 (US2) → Phase 5 (US3) → Phase 6 (US4) → Phase 7 (US5)
```

---

## Implementation Strategy

### MVP First (User Stories 1 + 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (View)
4. Complete Phase 4: User Story 2 (Add)
5. **STOP and VALIDATE**: Test add + view workflow
6. Demo/deploy MVP if needed

### Full Implementation

1. Complete Setup + Foundational
2. Complete all User Stories in priority order (P1 → P2 → P3)
3. Complete Phase 8 (Main loop integration)
4. Complete Phase 9 (Polish + Integration tests)
5. Run full validation per quickstart.md

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story is independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
