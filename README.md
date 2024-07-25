This project is a Python application that tests and analyzes human reaction times. It features a graphical user interface (GUI) and allows multiple users to take the test and compare their results.

Features

The application uses tkinter to provide a simple and intuitive GUI. Users can enter their name, start the test, and see their results on the screen. It supports multiple users, allowing each user to enter their name before starting the test, and their results will be saved separately. The reaction time data is saved to a CSV file (reaction_times.csv), which allows for persistent storage of results and enables future analysis.

The application calculates and displays various statistics, including the mean, median, standard deviation, fastest, and slowest reaction times for each user. Additionally, it provides multiple visualizations to analyze reaction times. These include a histogram that shows the distribution of reaction times for the current user, a line chart that compares reaction times across trials for selected users, and a box plot that visualizes the distribution of reaction times for selected users.

How It Works

To run the test, start the application by running the script advanced_reaction_time_analysis.py. Enter your name in the provided entry field and click the "Start" button to begin the reaction time test. The application will prompt you to press Enter as soon as you see the "Go!" signal. Your reaction times for each trial will be recorded and displayed on the screen. After completing all trials, detailed statistics and a histogram of your reaction times will be shown.

For analyzing results, you can click the "Analyze" button to compare results across multiple users. You will be prompted to enter the names of the users you want to analyze, separated by commas. The application will then display a line chart comparing reaction times across trials for the selected users and a box plot showing the distribution of reaction times.

