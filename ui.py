import pandas as pd
import tkinter as tk
from tkinter import ttk
class CaptionViewer:
    def __init__(self, root, df):
        self.root = root
        self.df = df
        self.current_page = 0
        self.rows_per_page = 5
        self.tree = None
        self.setup_ui()

    def setup_ui(self):
        self.tree = ttk.Treeview(self.root, columns=('Start Time', 'End Time', 'Text', 'Translated Text'), show='headings')
        for column in self.tree['columns']:
            if column in ['Text', 'Translated Text']:
                self.tree.column(column, width=500) 
            self.tree.heading(column, text=column)
        self.tree.grid(row=0, column=0, sticky='nsew')

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, sticky='nsew')

        prev_button = tk.Button(button_frame, text='Previous', command=self.prev_page)
        prev_button.pack(side='left')

        next_button = tk.Button(button_frame, text='Next', command=self.next_page)
        next_button.pack(side='right')

        self.load_page()

    def load_page(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        start = self.current_page * self.rows_per_page
        end = start + self.rows_per_page

        data = self.df.iloc[start:end]

        for _, row in data.iterrows():
            self.tree.insert('', 'end', values=(row['Start Time'], row['End Time'], row['Text'], row['translated_text']))

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.load_page()

    def next_page(self):
        if (self.current_page + 1) * self.rows_per_page < len(self.df):
            self.current_page += 1
            self.load_page()

def main():
    df = pd.read_csv('data/target/translated/Badiucao:_The_60_Minutes_Interview.csv')
    root = tk.Tk()
    viewer = CaptionViewer(root, df)
    root.mainloop()

if __name__ == '__main__':
    main()
