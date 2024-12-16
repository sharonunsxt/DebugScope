# DebugScope

**DebugScope** is a lightweight EXE Debugger for Windows. It allows you to debug executable files by attaching to their processes, logging events, and managing execution flow.

## Features

- **Attach to EXE processes**: Attach to any running or newly launched executable file for debugging.
- **Event Logging**: View live logs of debugging events like thread creation and memory allocation.
- **Detachment**: Safely detach from the process when debugging is complete.
- **GUI Interface**: A simple, user-friendly graphical interface for managing debugging sessions.

## Installation

1. Ensure you have Python installed (3.8 or later).
2. Install the following dependencies using pip:
   - `pydbg` (a lightweight Python debugging library).
   - `tkinter` (comes pre-installed with Python for most installations).
3. Save the script as `DebugScope.py`.

## Usage

1. Launch the program: Double-click the Python file or run it from the terminal using `python DebugScope.py`.
2. Use the **Browse** button to select an executable file (.exe) to debug.
3. Click **Attach** to start debugging the selected file.
4. View the logs and process activity in the provided log window.
5. Click **Detach** to safely stop debugging.

---

## License

This project is licensed under the MIT License.

## Support

For issues or feature requests, please create an issue in the project repository.
