# Student ID: 2022-0076767
# Course: MATH6200 - Data Analysis
# Activity: Course Project (Week 13)
# Question: [A] Is there a significant relationship between insomnia and job performance of the respondents?
# Formula: Pearson Correlation Coefficient (r) = (∑(x - x̄) (y - ȳ)) / √(∑(x - x̄)² ∑(x - ȳ)²).

# Dependencies and libraries.
import pandas as pd
import os

from pandas.io.formats.format import math

def clear_terminal():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')

def add_new_line():
    print("\n")

def get_data_frame():
    # Reading the absolute path of the file.
    course_project_data = os.path.join(os.path.dirname(__file__), 'files/course-project-data.csv')

    # Read the file into a data frame.
    # Return at the same time.
    return pd.read_csv(course_project_data)

def get_sleep_quality_column(data_frame: pd.DataFrame):
    return data_frame['Sleep Quality']

def get_job_performance_column(data_frame: pd.DataFrame):
    return data_frame['Job Performance']

def answer_a():
    # Clear the terminal first.
    clear_terminal()
    add_new_line()

    # Show the description on what to needs to be answered.
    print("\033[32m Is there a significant relationship between insomnia and job performance of the respondents? \033[0m")
    print("----------------------------------------------------------------------------------------------")

    # Get the course project data frame.
    data_frame = get_data_frame()
    print(data_frame)
    add_new_line()

    # Get the sleep quality and job performance column.
    sleep_quality_column = get_sleep_quality_column(data_frame)
    job_performance_column = get_job_performance_column(data_frame)

    # Get the mean of the column.
    sleep_quality_mean = sleep_quality_column.mean()
    job_performance_mean = job_performance_column.mean()

    # Compute the numerator ∑(x - x̄) (y - ȳ).
    numerator = sum((xi - sleep_quality_mean) * (yi - job_performance_mean) for xi, yi in zip(sleep_quality_column, job_performance_column))

    # Compute the denominator √(∑(x - x̄)² ∑(x - ȳ)²).
    summation_sleep_quality_deviation_squared = sum((xi - sleep_quality_mean) ** 2 for xi in sleep_quality_column)
    summation_job_performance_deviation_squared = sum((yi - job_performance_mean) ** 2 for yi in job_performance_column)
    denominator = math.sqrt(summation_sleep_quality_deviation_squared * summation_job_performance_deviation_squared)

    # Compute the pearson correlation coefficient (r).
    r = numerator / denominator

    # Display the computation result.
    # Show the description on what to needs to be answered.
    print("\033[32m Computation Result \033[0m")
    print("-----------------------------------------------------------")
    print("Sleep Quality Mean (x̄): ", sleep_quality_mean)
    print("Job Performance Mean (ȳ): ", job_performance_mean)
    print("∑(x - x̄) (y - ȳ): ", numerator)
    print("√(∑(x - x̄)² ∑(x - ȳ)²): ", denominator)
    print("Pearson Correlation Coefficient (r): ", r)
    add_new_line()

    # Display the concluation and explanation.
    print("\033[32m Conclusion \033[0m")
    print("--------------------------------------------")
    print("Given that the absolute value of r=-0.17 \nis relatively small, the correlation may \nnot be strong enough to conclude that\ninsomnia significantly impacts job \nperformance for the respondents in this \ndataset.")
    add_new_line()
    add_new_line()


# Run the program.
answer_a()
