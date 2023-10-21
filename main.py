import tkinter as tk
import tkinter.messagebox as tm
from tkinter import *
from classes import Workout


class Home:

    def calc_fees(self):
        try:
            if self.entry_courses.get().strip() == '':
                tm.showerror('Courses error', 'courses field is empty')
                self.entry_courses.focus_set()
                return
            courses = int(self.entry_courses.get().strip())
            fees_total.set(f'£{format(Workout().process(status.get(), courses), ",.2f")}')

        except ValueError:
            tm.showerror('Courses error', 'Please enter a valid number')
            self.entry_courses.focus_set()

    def clear_fields(self):
        self.entry_name.delete(0, END)
        self.entry_courses.delete(0, END)
        fees_total.set('')
        self.radio_home.select()  # default radio

    def __init__(self, master):
        self.master = master
        self.master.title("University of Greenwich Course Fees Calculator")
        self.master.geometry("700x180")
        self.frame = tk.Frame(self.master)
        self.master.resizable(0, 0)  # set resizable to false
        self.workout = Workout()

        # Check radio state
        global status
        global fees_total

        status = IntVar()
        fees_total = StringVar()
        # Label
        self.label_name = Label(self.frame, text="Enter your family name")
        self.label_courses = Label(self.frame, text="Enter number of courses you are taking")
        self.label_total = Label(self.frame, text="The fees for this year are")

        # Radio

        self.radio_home = Radiobutton(self.frame,
                                      text=f'Home Student £{format(self.workout.get_course_fees("home"), ",.2f")}',
                                      variable=status, value=1)
        self.radio_overseas = Radiobutton(self.frame,
                                          text=f'International Student £{format(self.workout.get_course_fees("international"), ",.2f")}',
                                          variable=status, value=2)
        # Entries
        self.entry_name = Entry(self.frame)
        self.entry_courses = Entry(self.frame)
        self.entry_total = Entry(self.frame, textvariable=fees_total, state='disabled')

        self.entry_name.focus_set()  # sets focus on name Entry
        # Grid Positions
        # Label Positions
        self.label_name.grid(row=1, sticky=E)
        self.label_courses.grid(row=2, sticky=E)
        self.label_total.grid(row=5, sticky=E)

        # Entries Positions
        self.entry_name.grid(row=1, column=1)
        self.entry_courses.grid(row=2, column=1)
        self.entry_total.grid(row=5, column=1)

        # Radio Buttons
        self.radio_home.grid(row=3, column=1)
        self.radio_overseas.grid(row=4, column=1)
        self.radio_home.select()  # default radio

        # Button Positions
        self.submit_Button = Button(self.frame, text="Submit details", relief=RAISED, command=lambda: self.calc_fees())
        self.clear_Button = Button(self.frame, text="CLEAR", relief=RAISED, command=lambda: self.clear_fields())
        self.submit_Button.grid(columnspan=2, padx=5, pady=5)
        self.clear_Button.grid(row=6, column=1)
        self.frame.pack()


def main():
    """Initialise the Window and class the home class"""
    root = tk.Tk()
    Home(root)  # Default to the Home Class
    root.resizable(0, 0)  # set resizable to false
    root.mainloop()


if __name__ == '__main__':
    main()
