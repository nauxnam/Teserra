import tkinter as tk
import logging
from tkinter import filedialog

from core.interface.elements.style import *
from core.interface.elements.menuBar import MenuBar
from core.interface.elements.bssFrame import BssFrame
from core.interface.elements.logger import Logger

logger = logging.getLogger()


class Gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("nauxnam's Backup Tool")
        self.geometry("650x300")
        self.resizable(width=False, height=False)

        # MENU BAR
        self._menu = tk.Menu(MenuBar())
        self.configure(menu=self._menu, bg=BG_COLOR)

        # TOP FRAME
        self._top_frame = tk.Frame(self, bg=BG_COLOR)
        self._top_frame.pack(side=tk.TOP,fill="y")

        self._bss_frame = BssFrame(self._top_frame)
        self._bss_frame.pack(side=tk.LEFT)

        self._timesel_frame = tk.Frame(self._top_frame, bg=BG_COLOR)
        self._timesel_frame.pack()

        self._remote_frame = tk.Frame(self._top_frame, bg=BG_COLOR)
        self._remote_frame.pack(side=tk.RIGHT)

        # BOTTOM FRAME
        self._bottom_frame = tk.Frame(self, bg=BG_COLOR)
        self._bottom_frame.pack(side=tk.BOTTOM,fill="y")

        self._log_frame = Logger(self._bottom_frame, bg=LOG_BGCOLOR)
        self._log_frame.pack(side=tk.LEFT)

        self._pbar_frame = tk.Frame(self._bottom_frame, bg=BG_COLOR)
        self._pbar_frame.pack()

        # STATUS BAR

        self._status_frame = tk.Frame(self, bg=STATUSBAR_COLOR)
        self._status_frame.pack(side=tk.BOTTOM)












