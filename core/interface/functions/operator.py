import os
import logging
import tkinter as tk
import typing
from tkinter import filedialog


logger = logging.getLogger()

if typing.TYPE_CHECKING:
    from core.interface.elements.source import sourcesWindow


class functions:
    def __init__(self, srcwin: "sourcesWindow", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.selectedDir = tk.StringVar()

        self.path = ""
        self.src = srcwin

    def fileSelect(self):
        self.selectedDir = filedialog.askdirectory(initialdir=os.sep, title="Select a Directory")
        return self.selectedDir


