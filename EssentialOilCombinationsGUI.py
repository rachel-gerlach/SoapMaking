import random
import tkinter as tk
from tkinter import messagebox

class ComboSizeApp:
    def __init__(self, root):
        self.selected_combo_size = None

        tk.Label(root, text="Do you want combinations of 3, 2, or both?").pack(pady=10)
        tk.Button(root, text="2", command=lambda: self.set_combo_size("2")).pack(pady=5)
        tk.Button(root, text="3", command=lambda: self.set_combo_size("3")).pack(pady=5)
        tk.Button(root, text="Both", command=lambda: self.set_combo_size("both")).pack(pady=5)
        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack(pady=10)
        tk.Button(root, text="Use Combo Size", command=self.use_combo_size).pack(pady=10)

    def set_combo_size(self, size):
        self.selected_combo_size = size
        self.result_label.config(text=f"Selected combo size: {size}")

    def use_combo_size(self):
        if self.selected_combo_size:
            messagebox.showinfo("Combo Size", f"You selected: {self.selected_combo_size}")
        else:
            messagebox.showwarning("No Selection", "Please select a combo size first!")

    import tkinter as tk
from tkinter import messagebox

class SubmitNumResults:
    def __init__(self, root):
        self.saved_num_results = None  # To store the validated result

        # Instruction Label
        self.instruction_label = tk.Label(root, text="How many combinations do you want?")
        self.instruction_label.pack(pady=10)

        # Entry widget for user input
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Button to submit the input
        self.submit_button = tk.Button(root, text="Submit", command=self.validate_input)
        self.submit_button.pack(pady=5)

        # Label to display results
        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack(pady=10)

        # Label to display error messages
        self.error_label = tk.Label(root, text="", fg="red")
        self.error_label.pack()

    def validate_input(self):
        """
        Validate the input from the Entry widget.
        """
        try:
            # Get the input from the Entry widget
            num_results = int(self.entry.get())
            
            if num_results > 0:
                # Valid input: Display the number and save it
                self.saved_num_results = num_results
                self.result_label.config(text=f"Number of combinations: {num_results}")
                self.error_label.config(text="")  # Clear any previous error messages
            else:
                # Invalid input: Show an error message
                self.error_label.config(text="Value must be greater than 0.", fg="red")
        except ValueError:
            # Handle non-integer input
            self.error_label.config(text="Please enter a valid integer.", fg="red")


