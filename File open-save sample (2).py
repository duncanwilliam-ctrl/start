import tkinter as tk
from tkinter import filedialog


def select_file():
    """Open a file selection dialog and return the selected file path"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Select LIFELABS calendar file",
        filetypes=[
            ("Calendar Files", "*.ics"),
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("Image files", "*.jpg;*.jpeg;*.png;*.gif"),
        ]
    )

    root.destroy()
    return file_path


def select_multiple_files():
    """Open a file selection dialog for multiple files"""
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Select files",
        filetypes=[("All files", "*.*")]
    )

    root.destroy()
    return file_paths


def save_file_dialog():
    """Open a save file dialog"""
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.asksaveasfilename(
        title="Save file as",
        defaultextension=".txt",
        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )

    root.destroy()
    return file_path


# Example usage
if __name__ == "__main__":
    # Single file selection
    selected_file = select_file()
    if selected_file:
        print(f"Selected file: {selected_file}")
    else:
        print("No file selected")

    # Multiple file selection
    # selected_files = select_multiple_files()
    # print(f"Selected files: {selected_files}")

    # Save file dialog
    # save_path = save_file_dialog()
    # print(f"Save path: {save_path}")
