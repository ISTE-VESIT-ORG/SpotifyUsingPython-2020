import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Frame")
    root.state("zoomed")

    top = tk.Frame(background="red")
    bottom = tk.Frame(background="#2c2c2c")

    topLeft = tk.Frame(top, background="#121212")
    topRight = tk.Frame(top, background="pink")

    topRightTop = tk.Frame(topRight, background="#000000")
    topRightBottom = tk.Frame(topRight, background="#181818")

    topRightTop.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    topRightBottom.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

    topRight.grid_columnconfigure(0, weight=1)
    topRight.grid_rowconfigure(0, weight=1)
    topRight.grid_rowconfigure(1, weight=10)

    topLeft.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    topRight.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)    

    top.grid_columnconfigure(0, weight=1)
    top.grid_columnconfigure(1, weight=7)
    top.grid_rowconfigure(0, weight=1)    

    top.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    bottom.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=8)
    root.grid_rowconfigure(1, weight=1)

    root.mainloop()