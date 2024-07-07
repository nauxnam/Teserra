import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import logging
import os

from interface.elements.style import *

logger = logging.getLogger()


class SourceDialog(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.directory_paths = []

        self.title("Select directories for backup")
        self.config(bg=BG_COLOR)
        self.geometry("400x150")
        self.resizable(width=False, height=False)
        self.grab_set()

        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(frame)
        canvas.config(bg=BG_COLOR)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        contentFrame = tk.Frame(canvas)
        contentFrame.config(bg=BG_COLOR)
        canvas.create_window((0,0), window=contentFrame, anchor="nw")

        header = tk.Label(contentFrame, text="Selected Directories:", bg=BG_COLOR, fg=FG_COLOR, font=SHEADER_FONT)
        header.grid(row=0, column=0)

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        contentFrame.bind("<Configure>", on_configure)

        def addRow():

            self.grab_release()
            self.lift()
            directory_path = filedialog.askdirectory(parent=self)
            if not directory_path:
                return

            # Validate directory path
            if not os.path.isdir(directory_path):
                raise ValueError("Selected path is not a directory")

            self.grab_set()
            self.directory_paths.append(directory_path)

            rowFrame = tk.Frame(contentFrame)
            rowFrame.grid(row=len(self.directory_paths) - 1, column=0, sticky="ew")

            entry = tk.Entry(rowFrame)
            entry.grid(row=0,column=0, sticky="ew")
            entry.insert(0, directory_path)

            timestamp = tk.Label(rowFrame, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            timestamp.grid(row=0,column=1)

            delBtn = tk.Button(rowFrame, text="X", command=lambda: deleteRow(rowFrame, directory_path))
            delBtn.grid(row=0,column=2)

            rowFrame.columnconfigure(0, weight=1)
            contentFrame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        def deleteRow(row, directory_path):
            row.destroy()
            self.directory_paths.remove(directory_path)

            # Repack the remaining rows to fill the empty space
            for i, widget in enumerate(contentFrame.winfo_children()):
                widget.grid(row=i, column=0, sticky="ew")
            contentFrame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        addBtn = tk.Button(contentFrame, text="Add", command=addRow)
        addBtn.grid(row=0, column=0)


