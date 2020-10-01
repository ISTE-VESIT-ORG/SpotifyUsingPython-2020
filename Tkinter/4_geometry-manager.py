import tkinter as tk
la = __import__("2_label")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Geometry Manager")
    root.state("zoomed")

    # PLACE
    label = la.CustomLabel(root, text="Hello", bg="red")
    label2 = la.CustomLabel(root, text="World", bg="yellow")

    label.place(x=5, y=5)
    label2.place(x=100, y=100)

    # PACK
    # label = la.CustomLabel(root, text="Hello")
    # label2 = la.CustomLabel(root, text="World")

    # label.pack(side=tk.RIGHT, padx=10)
    # label2.pack(side=tk.LEFT, padx=10)

    # GRID
    # label = la.CustomLabel(root, text="Hello")
    # label2 = la.CustomLabel(root, text="World")

    # label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    # label2.grid(row=1, column=0, stick="nsew", padx=10, pady=10)

    # root.grid_rowconfigure(0, weight=1)
    # root.grid_rowconfigure(1, weight=1)
    # root.grid_columnconfigure(0, weight=1)

    root.mainloop()