import tkinter as tk

from interface.elements.style import *

def donothing():
    print('Done')


class MenuBar(tk.Menu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # File cascade
        self.file = tk.Menu(self, tearoff=0)
        self.add_cascade(label='File', menu=self.file)
        self.add_command(label='New Backup...', command=donothing)
        self.add_command(label='Stop Backup Tasks', command=donothing)

        # Option cascade
        self.options = tk.Menu(self, tearoff=0)
        self.add_cascade(label='Options', menu=self.options)
        self.themes = tk.Menu(self.options, tearoff=0)
        self.options.add_cascade(label='Themes', menu=self.options)
        self.themes.add_command(label='Light Theme', command=donothing)
        self.themes.add_command(label='Dark Theme', command=donothing)
        self.options.add_separator()
        self.options.add_command(label='Preferences...', command=donothing)

        # Profile cascade
        self.profile = tk.Menu(self, tearoff=0)
        self.add_cascade(label='Profile', menu=self.profile)
        self.profile.add_command(label='Create a backup profile', command=donothing)
        self.profile.add_command(label='Import Profile...', command=donothing)
        self.profile.add_command(label='Export Profile...', command=donothing)

        # Help cascade
        self.helpmenu = tk.Menu(self, tearoff=0)
        self.add_cascade(label='Help', menu=self.helpmenu)
        self.helpmenu.add_command(label='Help Page', command=donothing)
        self.helpmenu.add_command(label='About', command=donothing)

        self.exitApp = tk.Menu(self, tearoff=0)
        self.exitApp.add_command(label='Exit', command=donothing)
