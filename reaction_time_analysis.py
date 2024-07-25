import time
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def reaction_time_test(trials=5):
    print("Reaction Time Test")
    print("Press Enter as soon as you see 'Go!'")
    
    reaction_times = []
    
    for trial in range(trials):
        print(f"Trial {trial + 1}")
        time.sleep(random.uniform(1, 3))  # Wait for a random time between 1 and 3 seconds
        input("Press Enter to start...")
        start_time = time.time()
        input("Go! Press Enter now!")
        end_time = time.time()
        reaction_time = end_time - start_time
        reaction_times.append(reaction_time)
        print(f"Your reaction time was {reaction_time:.4f} seconds\n")
    
    return reaction_times

def analyze_reaction_times(reaction_times):
    df = pd.DataFrame(reaction_times, columns=['Reaction Time'])
    mean_rt = df['Reaction Time'].mean()
    median_rt = df['Reaction Time'].median()
    std_rt = df['Reaction Time'].std()

    print(f"Mean Reaction Time: {mean_rt:.4f} seconds")
    print(f"Median Reaction Time: {median_rt:.4f} seconds")
    print(f"Standard Deviation: {std_rt:.4f} seconds")
    
    return df

def plot_reaction_times(df):
    plt.figure(figsize=(10, 5))
    plt.hist(df['Reaction Time'], bins=10, edgecolor='black')
    plt.title('Reaction Time Distribution')
    plt.xlabel('Reaction Time (seconds)')
    plt.ylabel('Frequency')
    plt.show()

# Running the test
reaction_times = reaction_time_test()

# Analyzing the results
df_reaction_times = analyze_reaction_times(reaction_times)

# Plotting the results
plot_reaction_times(df_reaction_times)
