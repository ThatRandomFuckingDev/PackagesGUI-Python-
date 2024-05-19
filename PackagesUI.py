"""GUI for Modules"""

# Yes, I chose tkinter, and custom tkinter for this. 

# It's a very simple application, and all it does is show the number of modules you have for Python; as well as sort them alphabetically.

import tkinter as tk
import pkg_resources as pr
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

# Made this so it's a whole load easier to see which packages you have, I suppose it's no different than the terminal; but meh.

# All this is; is a GUI so you can see what modules you have on your system. It wasn't hard to write the application, but to get certain
# parts (Like the GUI, and its colors) to work, I basically said: "Fuck this" and opted for an easier route.

class GUI(Frame):                                       # GUI frame
    def __init__(self, master) -> None:
            Frame.__init__(self, master)
            self.master = root
            self.pack(fill=tk.BOTH, expand=True)
            self.scrollingframe()
            self.styles()
            self.numer_of_packages()

# I swear, getting the scrolling to work correctly was tedious. I tried multiple ways, from using
# websites for information, to even asking ChatGPT.

    def scrollingframe(self):                            # Scrolling
        vertical = ttk.Scrollbar(self.master, orient='vertical')
        vertical.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = Text(self.master, width=15, height=1080, wrap=tk.NONE, 
                         yscrollcommand=vertical.set)
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        vertical.config(command=self.text.yview)

    def styles(self):                    # for the styles of ttk, which is used for the scrolling frame.
          default = ttk.Style()
          default.theme_use('default')

    def numer_of_packages(self):                          # Packages 
            il = list(pr.working_set)
            sorted_il = sorted(il, key=lambda x: x.key.lower())  # All this does is sor the names in alphebetical order.
            numil = len(sorted_il)

            explainer_text1 = "I made this so it's easier to see what modules"
            explainer_text2 = "are installed on your system. It's simple and "
            explainer_text3 = "it will help if you need to know this info."
            explainer_text4 = "Yep, it will tell you the number of modules"
            explainer_text5 = "and what you have. Alphebetical as well."

            warning_text = "!!NOTE: May not show *ALL* libraries and modules!!"

            warning = ttk.Label(self.master, text= f"{warning_text}",
                                   font = ("Arial", 25)).pack()

            packages = ttk.Label(self.master, text="Number of modules: ",   # No, these aren't syntaxed wrong, these are syntaxed correctly
                                font =("Arial", 45)                            # it's a lot easier to just make the packs here, and call them
                                ).pack()                                       # later if they need to. It works regardless.

            package_amount = ttk.Label(self.master, text = str(numil),      # I was a bit confused with this at first.
                             font = ("Arial", 75)
                             ).pack()

            for package in sorted_il: 
                self.text.insert(tk.END, package.key + " - version: "f"{package.version}" + "\n", "package_font")
                self.text.tag_configure("package_font", font=("Arial", 15))  # There's a couple of ways to do this, and the way I had to do it
                                                                             # is by asking ChatGPT, yeah, I am not doing a 40 hour search
                                                                             # it's already annoying enough anyway.
                
                                                                             # The first way is to literally just do: "font = ("Arial", #)"
                                                                             # which may or may not work.
            
            explaination = ttk.Label(self.master, text = "Read this if you want: ",
                                    font = ("Arial", 25)
                                    ).pack()
            
            explaining = ttk.Label(self.master, text = f"{explainer_text1} \n" # I found these are a lot easier to work with
                                  f"{explainer_text2} \n"                         # hence the reason they are calling variables
                                  f"{explainer_text3} \n"                         # it makes it a lot easier to work with.
                                  f"{explainer_text4} \n"
                                  f"{explainer_text5} \n",
                                  font = ("Arial", 25)).pack() 
            
            # I decided to combine tkinter with custom tkinter, because I wanted to see what I could come up with
            # after doing so, and trying to get colors to work correctly; I found that it only really would be useful
            # for the labels.

            # Strangely, I kept having serious issues with an X error for no real reason, and had to limit the size
            # of the scrolled text from 2080, down to 1080, and further until it worked.

            # After fixing the issue, I had to resolve the issues surrounding the color. I want to add custom color;
            # and ttk wasn't really offering much help here. I tried using base tkinter, and no luck. So I opted to use
            # customtkinter for the sake of ease. 
            

    def on_mousewheel(self, event):                                  # Mousewheel for scrolling the GUI text
        self.master.event_generate("<MouseWheel>", delta=event.delta)


    def GUI_close(self):                                               # To ensure it closes
            self.master.destroy()
            root.destroy()

if __name__ == '__main__':         # Just the root caller
       root = tk.Tk()
       app = GUI(master=root)
       root.geometry('750x380')
       root.title('Number of Packages')
       root.bind_all("<MouseWheel>", app.on_mousewheel)
       root.mainloop()
