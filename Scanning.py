import tkinter as tk
import time

class ScanningSystem:
    def __init__(self, rows=10, cols=4):
        self.root = tk.Tk()
        self.root.bind('<space>', self.select)
        self.table = [[f'Row {i+1}, Column {j+1}' for j in range(cols)] for i in range(rows)]
        self.table[0][0] = "I am hungry" ## edited to change first row in first column
        self.table[1][0] = "I am thirsty"
        self.table[2][0] = "I am in pain"
        self.table[3][0] = "I am uncomfortable"
        self.table[4][0] = "I need to use the bathroom"
        self.table[5][0] = "I'd like to sleep"
        self.table[6][0] = "It's too hot"
        self.table[7][0] = "It's too cold"
        self.table[8][0] = "I'm bored"
        self.table[9][0] = "I want to shower"
        self.table[0][1] = "Contact my family"
        self.table[0][3] = "Scanning speed too fast"
        self.table[1][3] = "Scanning speed too slow"
        self.table[9][3] = "Thank you"
        self.labels = [[tk.Label(self.root, text=item) for item in row] for row in self.table]
        for i, row in enumerate(self.labels):
            for j, label in enumerate(row):
                label.grid(row=i, column=j)
        self.current_row = 0
        self.current_column = 0
        self.final_row = None
        self.final_column = None
        self.select_row = True
        self.final_selected = False
        self.update()

    def select(self, event):
        if self.select_row:
            self.select_row = False
        elif not self.final_selected:
            self.final_selected = True
            self.final_row = self.current_row
            self.final_column = self.current_column
            self.root.after_cancel(self.after_id)  # stop the automatic scanning

    def update(self):
        for i, row in enumerate(self.labels):
            for j, label in enumerate(row):
                if (i, j) == (self.current_row, self.current_column):
                    label.config(bg='yellow')
                elif (i, j) == (self.final_row, self.final_column):
                    label.config(bg='green')
                else:
                    label.config(bg='white')
        if not self.final_selected:
            if self.select_row:
                self.current_row = (self.current_row + 1) % len(self.labels)
            else:
                self.current_column = (self.current_column + 1) % len(self.labels[0])
            self.after_id = self.root.after(700, self.update)  # store the id to potentially cancel the call later

    def start(self):
        self.root.mainloop()

if __name__ == '__main__':
    system = ScanningSystem()
    system.start()

