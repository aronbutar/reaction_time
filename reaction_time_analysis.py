import time
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox

class ReactionTimeTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Reaction Time Test")
        self.master.geometry("400x300")
        
        self.label = tk.Label(master, text="Enter your name and press Start to begin the test", font=('Helvetica', 12))
        self.label.pack(pady=20)
        
        self.name_entry = tk.Entry(master, font=('Helvetica', 12))
        self.name_entry.pack(pady=10)
        
        self.start_button = tk.Button(master, text="Start", command=self.start_test, font=('Helvetica', 12))
        self.start_button.pack(pady=20)
        
        self.analyze_button = tk.Button(master, text="Analyze", command=self.analyze_all_users, font=('Helvetica', 12))
        self.analyze_button.pack(pady=20)
        
        self.results = []
        self.trials = 5
        self.current_trial = 0
        self.start_time = 0
        self.user_name = ""
        self.load_results()

    def load_results(self):
        try:
            self.all_results = pd.read_csv('reaction_times.csv')
        except FileNotFoundError:
            self.all_results = pd.DataFrame()

    def start_test(self):
        self.user_name = self.name_entry.get().strip()
        if not self.user_name:
            messagebox.showerror("Error", "Please enter your name")
            return
        self.current_trial = 0
        self.results = []
        self.next_trial()
        
    def next_trial(self):
        if self.current_trial < self.trials:
            self.label.config(text="Get ready...")
            self.master.update()
            time.sleep(random.uniform(1, 3))
            self.label.config(text="Go!")
            self.start_time = time.time()
            self.master.bind('<Return>', self.record_reaction_time)
        else:
            self.save_results()
            self.show_results()
            
    def record_reaction_time(self, event):
        reaction_time = time.time() - self.start_time
        self.results.append(reaction_time)
        self.current_trial += 1
        self.label.config(text=f"Trial {self.current_trial} completed. Reaction time: {reaction_time:.4f} seconds")
        self.master.unbind('<Return>')
        self.master.after(1000, self.next_trial)

    def save_results(self):
        df = pd.DataFrame(self.results, columns=['Reaction Time'])
        df['User'] = self.user_name
        df.to_csv('reaction_times.csv', mode='a', header=not self.all_results.empty, index=False)
        self.all_results = pd.concat([self.all_results, df], ignore_index=True)
        
    def show_results(self):
        self.label.config(text="Test completed. See the console for results.")
        self.analyze_reaction_times(self.results, self.user_name)

    def analyze_reaction_times(self, results, user_name):
        df = pd.DataFrame(results, columns=['Reaction Time'])
        mean_rt = df['Reaction Time'].mean()
        median_rt = df['Reaction Time'].median()
        std_rt = df['Reaction Time'].std()
        min_rt = df['Reaction Time'].min()
        max_rt = df['Reaction Time'].max()

        print(f"Results for {user_name}:")
        print(f"Mean Reaction Time: {mean_rt:.4f} seconds")
        print(f"Median Reaction Time: {median_rt:.4f} seconds")
        print(f"Standard Deviation: {std_rt:.4f} seconds")
        print(f"Fastest Reaction Time: {min_rt:.4f} seconds")
        print(f"Slowest Reaction Time: {max_rt:.4f} seconds")
        
        self.plot_reaction_times(df, user_name)
        
    def plot_reaction_times(self, df, user_name):
        plt.figure(figsize=(10, 5))
        plt.hist(df['Reaction Time'], bins=10, edgecolor='black')
        plt.title(f'Reaction Time Distribution for {user_name}')
        plt.xlabel('Reaction Time (seconds)')
        plt.ylabel('Frequency')
        plt.show()

    def analyze_all_users(self):
        users = self.all_results['User'].unique()
        user_choice = simpledialog.askstring("Input", f"Select user(s) to analyze (available: {', '.join(users)})")
        if not user_choice:
            return
        selected_users = [user.strip() for user in user_choice.split(',')]
        filtered_df = self.all_results[self.all_results['User'].isin(selected_users)]
        
        self.plot_user_comparison(filtered_df, selected_users)
        self.plot_boxplot(filtered_df, selected_users)

    def plot_user_comparison(self, df, selected_users):
        plt.figure(figsize=(10, 5))
        for user in selected_users:
            user_df = df[df['User'] == user]
            plt.plot(user_df.index, user_df['Reaction Time'], marker='o', label=user)
        
        plt.title('Reaction Time Comparison')
        plt.xlabel('Trial')
        plt.ylabel('Reaction Time (seconds)')
        plt.legend()
        plt.show()

    def plot_boxplot(self, df, selected_users):
        plt.figure(figsize=(10, 5))
        df.boxplot(column='Reaction Time', by='User', grid=False)
        plt.title('Reaction Time Box Plot')
        plt.suptitle('')
        plt.xlabel('User')
        plt.ylabel('Reaction Time (seconds)')
        plt.show()

def main():
    root = tk.Tk()
    app = ReactionTimeTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()
