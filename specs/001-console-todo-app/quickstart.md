# Quickstart: In-Memory Console Todo App

Get up and running with the todo app in under 2 minutes.

## Prerequisites

- Python 3.13 or higher
- Terminal/command prompt access

**Verify Python version**:
```bash
python --version
# Should output: Python 3.13.x or higher
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Hackathon-II-Phase-I-Todo-Spec-Driven-Development
```

### 2. (Optional) Create virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. No dependencies to install!

This application uses only the Python standard library. No `pip install` required.

## Running the Application

```bash
python -m src.main
```

You should see the main menu:

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

## Quick Tutorial

### Add your first task

1. Enter `1` at the menu
2. Type a task title (e.g., "Buy groceries")
3. Press Enter

```text
Enter choice (1-6): 1
Enter task title: Buy groceries
Task added successfully! (ID: 1)
```

### View your tasks

1. Enter `2` at the menu

```text
Enter choice (1-6): 2
=== Your Tasks ===
[ ] 1. Buy groceries
==================
Total: 1 tasks (0 completed)
```

### Mark a task complete

1. Enter `4` at the menu
2. Enter the task ID (e.g., `1`)

```text
Enter choice (1-6): 4
Enter task ID to mark complete: 1
Task marked as complete!
ID: 1
Title: Buy groceries
```

### Exit the application

1. Enter `6` at the menu

```text
Enter choice (1-6): 6
Goodbye! Your tasks have not been saved.
```

**Note**: All tasks are stored in memory only. When you exit, your tasks are not saved.

## Running Tests

```bash
# Install pytest (one-time)
pip install pytest

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/unit/test_task_manager.py
```

## Project Structure

```text
src/
├── main.py              # Entry point
├── models/
│   └── task.py          # Task data model
├── services/
│   └── task_manager.py  # Business logic
├── cli/
│   ├── menu.py          # Menu display
│   └── handlers.py      # Command handlers
└── utils/
    └── validators.py    # Input validation

tests/
├── unit/                # Unit tests
└── integration/         # Integration tests
```

## Troubleshooting

### "Python not found"

Ensure Python 3.13+ is installed and in your PATH:
```bash
# Check installation
python --version

# On some systems, use python3
python3 --version
```

### "Module not found" error

Run the application as a module from the repository root:
```bash
# Correct
python -m src.main

# Incorrect (may fail)
python src/main.py
```

### Tests fail with import errors

Ensure you're running pytest from the repository root:
```bash
cd Hackathon-II-Phase-I-Todo-Spec-Driven-Development
pytest
```

## What's Next?

This is Phase I of a multi-phase project:

- **Phase II**: Web application with persistent storage
- **Phase III**: AI-powered chatbot interface
- **Phase IV**: Kubernetes deployment
- **Phase V**: Cloud deployment with real-time features

See the [constitution](.specify/memory/constitution.md) for full project roadmap.
