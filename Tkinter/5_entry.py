import tkinter as tk
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Entry")
    root.state("zoomed")

    label = tk.Label(text="Name")
    entry = tk.Entry()

    def onclick():
        print(entry.get())
        entry.delete(0, tk.END)

    button = tk.Button(text="Submit", command=onclick) 

    label.grid(row=0, column=0, padx=10, pady=10)
    entry.grid(row=0, column=1, padx=10, pady=10)
    button.grid(row=0, column=2, padx=10, pady=10)

    
    
    root.mainloop()