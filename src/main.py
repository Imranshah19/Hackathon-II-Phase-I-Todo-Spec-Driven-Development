"""Main entry point for the In-Memory Console Todo Application."""

import sys
from pathlib import Path

# Add project root to path for direct script execution
_project_root = Path(__file__).parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from src.services.task_manager import TaskManager
from src.cli.menu import display_menu
from src.cli.handlers import (
    handle_view_tasks,
    handle_add_task,
    handle_toggle_status,
    handle_update_task,
    handle_delete_task,
    handle_exit,
)


def main() -> None:
    """Run the main application loop."""
    manager = TaskManager()

    while True:
        print()  # Blank line before menu
        display_menu()

        try:
            choice = input().strip()
        except (EOFError, KeyboardInterrupt):
            print()
            handle_exit()
            break

        if choice == "1":
            handle_add_task(manager)
        elif choice == "2":
            handle_view_tasks(manager)
        elif choice == "3":
            handle_update_task(manager)
        elif choice == "4":
            handle_toggle_status(manager)
        elif choice == "5":
            handle_delete_task(manager)
        elif choice == "6":
            handle_exit()
            break
        else:
            print("Invalid option: please enter a number 1-6")


if __name__ == "__main__":
    main()
