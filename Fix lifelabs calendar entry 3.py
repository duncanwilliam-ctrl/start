'''
open file to Read
read records
if record contains identifier to fix,
then find "-" and correct with nothing
write record to new file
'''
import tkinter as tk
from tkinter import filedialog


def fix(record):
    if "DTSTART" in record or "DTEND" in record:
        record = record.replace(
            "-", "").replace(":", "").replace("DTSTART", "DTSTART:").replace("DTEND", "DTEND:")

    fixed = record
    return fixed


def select_file():
    """Open a file selection dialog and return the selected file path"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Select LIFELABS calendar file for fixing > .ics",
        filetypes=[
            ("Calendar Files", "*.ics"),
            ("All files", "*.*")

        ]
    )

    root.destroy()
    return file_path


selected_file = select_file()

fixed = ""

try:
    with open(selected_file, mode="r") as infile, open("lifelabsfixed.ics", mode="w") as outfile:
        for record in infile:
            fixed = fix(record)
            outfile.write(fixed)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")


if selected_file:
    print(f"Selected file: {selected_file} FIXED!")
else:
    print("No file selected")
