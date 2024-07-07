import os
import logging
import tkinter as tk
import typing
from tkinter import filedialog


logger = logging.getLogger()

class functions:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.selectedDir = tk.StringVar()

        self.path = ""

    def fileSelect(self):
        self.selectedDir = filedialog.askdirectory(initialdir=os.sep, title="Select a Directory")
        return self.selectedDir


