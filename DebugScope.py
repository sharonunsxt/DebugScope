import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess
import threading

# Debugger Backend
class Debugger:
    def __init__(self):
        self.process = None
        self.debugging = False

    def attach_process(self, process_path):
        try:
            self.process = subprocess.Popen(process_path, creationflags=subprocess.DEBUG_PROCESS)
            self.debugging = True
            return f"Attached to process: {os.path.basename(process_path)}"
        except Exception as e:
            return f"Failed to attach: {e}"

    def detach_process(self):
        if self.process:
            self.process.terminate()
            self.debugging = False
            return "Detached and stopped debugging."
        return "No process attached."

# GUI Frontend
class DebugScopeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DebugScope - EXE Debugger")
        self.debugger = Debugger()

        # File Selector
        self.file_label = tk.Label(root, text="Select an Executable:")
        self.file_label.pack(pady=5)

        self.file_entry = tk.Entry(root, width=50)
        self.file_entry.pack(pady=5)

        self.file_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.file_button.pack(pady=5)

        # Action Buttons
        self.attach_button = tk.Button(root, text="Attach", command=self.attach_to_process)
        self.attach_button.pack(pady=5)

        self.detach_button = tk.Button(root, text="Detach", command=self.detach_from_process)
        self.detach_button.pack(pady=5)

        # Debugging Log
        self.log_label = tk.Label(root, text="Debugging Log:")
        self.log_label.pack(pady=5)

        self.log_text = tk.Text(root, height=15, width=80)
        self.log_text.pack(pady=5)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Executable files", "*.exe"), ("All files", "*.*")]
        )
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

    def attach_to_process(self):
        process_path = self.file_entry.get()
        if not process_path or not os.path.isfile(process_path):
            messagebox.showerror("Error", "Please select a valid executable file.")
            return

        log_message = self.debugger.attach_process(process_path)
        self.log(log_message)

    def detach_from_process(self):
        log_message = self.debugger.detach_process()
        self.log(log_message)

    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = DebugScopeApp(root)
    root.mainloop()
