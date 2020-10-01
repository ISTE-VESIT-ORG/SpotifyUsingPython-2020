import tkinter as tk

count = 1

class CustomButton(tk.Button):
    def __init__(self, master, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)
        self['text'] = "Click Me"
        self['background'] = "green"

def onClick():
    global count
    print("I got clicked", count)
    count+=1

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Button")
    root.state("zoomed")

    button = CustomButton(root, command=onClick)
    button.pack()

    root.mainloop()