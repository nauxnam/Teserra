from tkinter.ttk import *
from datetime import datetime

from core.interface.elements.style import *
from core.interface.functions.operator import *


class sourcesWindow:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.func = functions(self)

        self._rows = []

        self.src_win = tk.Toplevel()
        self.src_win.title("Backup Selected Folders")
        self.src_win.geometry("500x600")
        self.src_win.config(bg=BG_COLOR)
        self.src_win.attributes("-topmost", "true")
        self.src_win.grab_set()
        self.src_win.resizable(width=False, height=False)

        self._sourceListFrame = tk.Canvas(self.src_win)
        self.scrollbar = Scrollbar(self._sourceListFrame, orient="vertical", command=self._sourceListFrame.yview)

        self._backupTable = tk.Frame(self._sourceListFrame)
        self._backupTable.config(bg=BG_COLOR)

        self._backupTable.bind(
            "<Configure>",
            lambda e: self._sourceListFrame.configure(
                scrollregion=self._sourceListFrame.bbox("all")
            )
        )
        self._sourceListFrame.create_window((0,0), window=self._backupTable, anchor="nw")
        self._sourceListFrame.configure(yscrollcommand=self.scrollbar.set)
        self._sourceListFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self._backupTable.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self._createWidgets()

    def _createWidgets(self):
        self.topLabel = tk.Label(self._backupTable, text="Add & Remove Backups")
        self.topLabel.grid(row=0,column=0)
        self.addRowbtn = tk.Button(self._backupTable, text="Add Backup", command=self._add_row)
        self.addRowbtn.grid(row=1,column=0, sticky=tk.NW)

        self.pathLabel = tk.Label(self._backupTable, text="Backup Path")
        self.pathLabel.config(bg=BG_COLOR,fg=FG_COLOR,font=BOLD_FONT)
        self.pathLabel.grid(row=2,column=0)

        self.timeAddedLabel = tk.Label(self._backupTable, text="Time Added")
        self.timeAddedLabel.config(bg=BG_COLOR,fg=FG_COLOR,font=BOLD_FONT)
        self.timeAddedLabel.grid(row=2,column=1)

    def _add_row(self):
        r_index = len(self._rows) + 3
        self.current_time = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")

        pathEntry = tk.Entry(self._backupTable)
        pathEntry.grid(row=r_index,column=0)

        timeAdded = tk.Label(self._backupTable, text="%s" % self.current_time)
        timeAdded.config(bg=BG_COLOR,fg=FG_COLOR,font=GLOBAL_FONT)
        timeAdded.grid(row=r_index, column=1)

        removeRow = tk.Button(self._backupTable, text="X", command=lambda: self._delete_row(r_index))
        removeRow.config(bg="red",fg=FG_COLOR)
        removeRow.grid(row=r_index, column=2)

        self._rows.append((pathEntry, timeAdded, removeRow))

    def _delete_row(self, r_index: int):
        adjusted_index = r_index - 3
        if 0 <= adjusted_index < len(self._rows):
            row = self._rows[adjusted_index]
            if row:
                for widget in row:
                    widget.grid_forget()
                    widget.destroy()
                self._reorder_rows()
    def _reorder_rows(self):
        for idx, row in enumerate(self._rows):
            if row:
                for col, widget in enumerate(row):
                    if widget.winfo_exists():
                        widget.grid(row=idx + 1, column=col)























