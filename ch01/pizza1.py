import tkinter as tk
from tkinter import messagebox

def calculate_total():
    size_price = {"Small": 8000, "Medium": 12000, "Large": 16000}
    topping_price = 1500
    
    size = size_var.get()
    toppings = [t.get() for t in topping_vars if t.get()]
    quantity = int(quantity_var.get())
    
    total = (size_price[size] + topping_price * len(toppings)) * quantity
    
    messagebox.showinfo("Order Summary", f"Size: {size}\nToppings: {', '.join(toppings) if toppings else 'None'}\nQuantity: {quantity}\nTotal Price: {total} KRW")

def create_order_window():
    global size_var, topping_vars, quantity_var
    
    root = tk.Tk()
    root.title("Pizza Order System")
    root.geometry("300x400")
    
    tk.Label(root, text="Select Pizza Size", font=("Arial", 12, "bold")).pack()
    size_var = tk.StringVar(value="Medium")
    for size in ["Small", "Medium", "Large"]:
        tk.Radiobutton(root, text=size, variable=size_var, value=size).pack(anchor="w")
    
    tk.Label(root, text="Select Toppings", font=("Arial", 12, "bold")).pack()
    toppings = ["Pepperoni", "Mushrooms", "Olives", "Extra Cheese"]
    topping_vars = [tk.StringVar() for _ in toppings]
    for i, topping in enumerate(toppings):
        tk.Checkbutton(root, text=topping, variable=topping_vars[i], onvalue=topping, offvalue="").pack(anchor="w")
    
    tk.Label(root, text="Select Quantity", font=("Arial", 12, "bold")).pack()
    quantity_var = tk.StringVar(value="1")
    tk.Spinbox(root, from_=1, to=10, textvariable=quantity_var).pack()
    
    tk.Button(root, text="Order Now", command=calculate_total, bg="green", fg="white").pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_order_window()
