import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)  # Make the window not resizable

        self.result_var = tk.StringVar()
        self.history_var = tk.StringVar()
        self.history = []

        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Helvetica", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.history_label = tk.Label(root, textvariable=self.history_var, font=("Helvetica", 12))
        self.history_label.grid(row=5, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('CE', 5, 0),  # Clear Entry button
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Helvetica", 16), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew')

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set("{:.4f}".format(result))  # Limit to 4 decimal places
                self.history.append(f"{self.result_var.get()} = {result}")
                self.update_history_label()
            except Exception:
                self.result_var.set("Error")
        elif value == "CE":
            self.result_var.set("")
        else:
            current_value = self.result_var.get()
            if current_value == "Error":
                current_value = ""
            self.result_var.set(current_value + value)

    def update_history_label(self):
        self.history_var.set("\n".join(self.history[-5:]))  # Display the last 5 history entries

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
