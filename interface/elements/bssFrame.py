import tkinter as tk
import logging

from interface.elements.style import *
from interface.elements import srcdialog
from interface.elements import cloud
from interface.elements import scheduler


logger = logging.getLogger()


def donothing():
    logger.info("Done")


class BssFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logs = []

        self.config(bg=BG_COLOR)

        self.backupbFrame = tk.Frame(self)
        self.backupbFrame.config(border=1,bg=BG_COLOR)
        self.backupbFrame.pack(side=tk.LEFT,fill="both", expand=True)

        # Selector
        self.select_label = tk.Label(self.backupbFrame, text="Backup Actions", bg=BG_COLOR, fg=FG_COLOR)
        self.select_label.grid(row=0,column=0)
        self.selectb = tk.Button(self.backupbFrame, text="Select Source(s)", command=srcdialog.SourceDialog)
        self.selectb.grid(row=1,column=0,pady=2)

        # Sync
        self.syncb = tk.Button(self.backupbFrame, text="Synchronize", command=donothing)
        self.syncb.grid(row=2,column=0,sticky=tk.NSEW)

        # Backup Buttons
        self.bkstart_b = tk.Button(self.backupbFrame, text="Start Backup", command=donothing)
        self.bkstart_b.grid(row=1,column=1,padx=10)
        self.bkstop_b = tk.Button(self.backupbFrame, text="Stop Backup", command=donothing)
        self.bkstop_b.grid(row=2,column=1,padx=10)

