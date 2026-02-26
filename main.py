import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import shutil

from quiz.logic import build_questions, grade
from quiz.validators import validate_name, validate_choice
from quiz.models import QuizAttempt
from quiz.store import save_attempt, load_attempts

DATA_FILE = "data/attempts.csv"


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("BMW AI Quiz")

        self.questions = build_questions()
        self.index = 0
        self.answers = []
        self.name = ""

        
        tk.Label(root, text="Enter your name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Button(root, text="Start Quiz", command=self.start_quiz).pack(pady=5)

        
        self.question_label = tk.Label(root, text="", wraplength=450, justify="left")
        self.choice = tk.IntVar(value=-1)
        self.option_buttons = []
        self.next_button = tk.Button(root, text="Next", command=self.next_question)

       
        tk.Button(root, text="View Attempts", command=self.view_attempts).pack(pady=5)
        tk.Button(root, text="Export CSV", command=self.export_csv).pack()

    def start_quiz(self):
        ok, msg = validate_name(self.name_entry.get())
        if not ok:
            messagebox.showerror("Error", msg)
            return

        self.name = self.name_entry.get().strip()

        
        for widget in self.root.pack_slaves():
            pass  

        
        self.question_label.pack(pady=8)
        self.next_button.pack(pady=6)
        self.show_question()

    def show_question(self):
        q = self.questions[self.index]
        self.question_label.config(text=f"Q{self.index + 1}. {q.prompt}")

       
        self.choice.set(-1)

        
        for btn in self.option_buttons:
            btn.destroy()
        self.option_buttons.clear()

        
        for i, option in enumerate(q.options):
            rb = tk.Radiobutton(self.root, text=option, variable=self.choice, value=i, anchor="w")
            rb.pack(fill="x", padx=18)
            self.option_buttons.append(rb)

    def next_question(self):
        ok, msg = validate_choice(self.choice.get(), 4)
        if not ok:
            messagebox.showerror("Error", msg)
            return

        self.answers.append(self.choice.get())
        self.index += 1

        if self.index < len(self.questions):
            self.show_question()
        else:
            self.finish()

    def finish(self):
        score = grade(self.questions, self.answers)
        total = len(self.questions)

        attempt = QuizAttempt(self.name, score, total)
        save_attempt(DATA_FILE, attempt)

        messagebox.showinfo("Done", f"Score: {score}/{total}")
        self.root.destroy()

    def view_attempts(self):
        win = tk.Toplevel(self.root)
        win.title("Attempts")

        tree = ttk.Treeview(win, columns=("Name", "Time", "Score", "Total"), show="headings")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        for col in ("Name", "Time", "Score", "Total"):
            tree.heading(col, text=col)

        for row in load_attempts(DATA_FILE):
            tree.insert("", tk.END, values=row)

    def export_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv")
        if path:
            try:
                shutil.copy(DATA_FILE, path)
                messagebox.showinfo("Exported", "CSV exported.")
            except:
                messagebox.showerror("Error", "Export failed.")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()