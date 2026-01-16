# CLI Interface Contract: In-Memory Console Todo App

**Date**: 2026-01-10
**Feature**: 001-console-todo-app

## Overview

This document defines the command-line interface contract for the todo application. The interface is menu-driven with numbered options.

## Application Flow

```text
┌─────────────────────────────────────────────────────────────┐
│                      Application Start                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       Display Menu                           │
│  === Todo App ===                                            │
│  1. Add Task                                                 │
│  2. View Tasks                                               │
│  3. Update Task                                              │
│  4. Mark Complete                                            │
│  5. Delete Task                                              │
│  6. Exit                                                     │
│                                                              │
│  Enter choice (1-6):                                         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Process User Input                        │
│  - Validate input is 1-6                                     │
│  - Route to appropriate handler                              │
│  - Display result or error                                   │
│  - Return to menu (unless Exit)                              │
└─────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │    Choice = 6?    │
                    └─────────┬─────────┘
                       No │         │ Yes
                          ▼         ▼
                    [Return to    [Exit with
                      Menu]       goodbye msg]
```

## Menu Contract

### Main Menu Display

**Input**: None
**Output**:
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

### Menu Input Validation

| Input | Valid | Response |
|-------|-------|----------|
| `1` | Yes | Route to Add Task |
| `2` | Yes | Route to View Tasks |
| `3` | Yes | Route to Update Task |
| `4` | Yes | Route to Mark Complete |
| `5` | Yes | Route to Delete Task |
| `6` | Yes | Exit application |
| Empty | No | "Invalid option: please enter a number 1-6" |
| Non-numeric | No | "Invalid option: please enter a number 1-6" |
| `0`, `7`, etc. | No | "Invalid option: please enter a number 1-6" |

## Operation Contracts

### 1. Add Task

**Flow**:
```text
Enter choice (1-6): 1
Enter task title: <user input>
```

**Success Response**:
```text
Task added successfully! (ID: <id>)
```

**Error Responses**:
| Condition | Response |
|-----------|----------|
| Empty title | "Error: Task title cannot be empty" |
| Whitespace-only title | "Error: Task title cannot be empty" |
| Title > 200 chars | "Error: Task title exceeds maximum length (200 characters)" |

### 2. View Tasks

**Flow**:
```text
Enter choice (1-6): 2
```

**Success Response (tasks exist)**:
```text
=== Your Tasks ===
[ ] 1. Buy groceries
[x] 2. Call mom
[ ] 3. Finish report
==================
Total: 3 tasks (1 completed)
```

**Success Response (no tasks)**:
```text
No tasks found. Add a task to get started!
```

**Display Format**:
- `[ ]` = Incomplete task
- `[x]` = Completed task
- Format: `[status] <id>. <title>`

### 3. Update Task

**Flow**:
```text
Enter choice (1-6): 3
Enter task ID to update: <user input>
Enter new title: <user input>
```

**Success Response**:
```text
Task updated successfully!
ID: <id>
New title: <new_title>
```

**Error Responses**:
| Condition | Response |
|-----------|----------|
| Invalid ID format | "Error: Invalid task ID: must be a number" |
| Negative/zero ID | "Error: Invalid task ID: must be a positive number" |
| Task not found | "Error: Task not found" |
| Empty new title | "Error: Task title cannot be empty" |
| New title > 200 chars | "Error: Task title exceeds maximum length (200 characters)" |

### 4. Mark Complete

**Flow**:
```text
Enter choice (1-6): 4
Enter task ID to mark complete: <user input>
```

**Success Response**:
```text
Task marked as complete!
ID: <id>
Title: <title>
```

**Already Complete Response**:
```text
Task is already complete.
ID: <id>
Title: <title>
```

**Error Responses**:
| Condition | Response |
|-----------|----------|
| Invalid ID format | "Error: Invalid task ID: must be a number" |
| Negative/zero ID | "Error: Invalid task ID: must be a positive number" |
| Task not found | "Error: Task not found" |

### 5. Delete Task

**Flow**:
```text
Enter choice (1-6): 5
Enter task ID to delete: <user input>
```

**Success Response**:
```text
Task deleted successfully!
Deleted: <title>
```

**Error Responses**:
| Condition | Response |
|-----------|----------|
| Invalid ID format | "Error: Invalid task ID: must be a number" |
| Negative/zero ID | "Error: Invalid task ID: must be a positive number" |
| Task not found | "Error: Task not found" |

### 6. Exit

**Flow**:
```text
Enter choice (1-6): 6
```

**Response**:
```text
Goodbye! Your tasks have not been saved.
```

**Behavior**: Application terminates with exit code 0.

## Input/Output Specifications

### Standard Streams

| Stream | Usage |
|--------|-------|
| stdin | All user input |
| stdout | Menu, prompts, success messages |
| stderr | Error messages (prefixed with "Error:") |

### Character Encoding

- UTF-8 encoding for all I/O
- Task titles may contain any printable Unicode characters
- Newlines: `\n` (cross-platform handled by Python)

### Prompt Format

All prompts end with `: ` (colon + space) to indicate waiting for input.

## Error Handling Contract

### Error Message Format

```text
Error: <specific error message>
```

### Recovery Behavior

- After any error, return to main menu
- Never crash on invalid input
- Always display helpful error message before returning to menu

## Testing Contract

### Input Simulation

For automated testing, the CLI should accept input from stdin:

```bash
echo -e "1\nBuy groceries\n2\n6" | python -m src.main
```

### Expected Test Scenarios

| Test | Input Sequence | Expected Output Contains |
|------|----------------|-------------------------|
| Add and view | `1`, `Test task`, `2`, `6` | "Task added", "Test task" |
| Invalid menu | `7`, `6` | "Invalid option" |
| Empty title | `1`, ``, `6` | "cannot be empty" |
| Task not found | `4`, `999`, `6` | "not found" |
| Mark complete | `1`, `Task`, `4`, `1`, `2`, `6` | "[x] 1. Task" |
