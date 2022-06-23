import tkinter as tk
# import cmdIndex.py 
from cmdIndex import cmdIndex

class Navbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.init_ui()

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.pack(fill=tk.BOTH, expand=1)

        self.btn_home = tk.Button(self, text="Home")
        self.btn_home.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_settings = tk.Button(self, text="Settings")
        self.btn_settings.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_logout = tk.Button(self, text="Logout")

class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.init_ui()
        self.input_text()

    def init_ui(self):
        self.pack(fill=tk.BOTH, expand=1)

        self.navbar = Navbar(self)
        self.navbar.pack(side=tk.TOP, fill=tk.X)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

    # input text box in style of a terminal window
    # if input text matches a function in cmdIndex, execute that function
    # first word is command, second word is argument
    # on input enter, reset input text box
    def input_text(self):
        self.input_frame = tk.Frame(self.main_frame)
        self.input_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.input_text = tk.Text(self.input_frame, height=1, width=50)
        self.input_text.pack(side=tk.LEFT, fill=tk.X)

        self.input_text.bind("<Return>", self.input_enter)

        # grab printed output from cmdIndex and print it in the main window
        self.output_frame = tk.Frame(self.main_frame)
        self.output_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.output_text = tk.Text(self.output_frame, height=1, width=50)
        self.output_text.pack(side=tk.LEFT, fill=tk.X)

        # grab output printed from cmdIndex function that was called and print it in the main window
        self.output_text.insert(tk.END, cmdIndex.output)

    def input_enter(self, event):
        input_text = self.input_text.get("1.0", tk.END)
        input_text = input_text.split()
        cmd = input_text[0]
        args = input_text[1:]
        if cmd in cmdIndex.cmds:
            cmdIndex.cmds[cmd](args)
        self.input_text.delete("1.0", tk.END)

# change title of window to "Home Interface"
class MainApp(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    tk.Frame.__init__(self, parent, *args, **kwargs)
    self.parent = parent
    self.master.title("Home Interface")

    # Create GUI here ↓
    self.main_window = MainWindow(self)
    self.main_window.pack(fill=tk.BOTH, expand=1)
    # Create GUI here ↑

    # GUI functions here ↓

    # GUI functions here ↑

if __name__ == '__main__':
  root = tk.Tk()
  app = MainApp(root)
  app.pack(side="top", fill="both", expand=True)
  root.mainloop()
