# Student ID: 2022-0076767
# Course: MATH6200 - Data Analysis
# Activity: Course Project (Week 13)
# Question: [C] Is there a significant difference in the level of job performance when they grouped according to sex?
# Formula: Statistical Test (ttest)

import pandas as pd
import os
from scipy import stats

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

def get_job_performance_column(data_frame: pd.DataFrame):
    return data_frame['Job Performance']

def get_sex_column(data_frame: pd.DataFrame):
    return data_frame['Sex']

def answer_c():
    # Clear the terminal first.
    clear_terminal()
    add_new_line()

    # Show the description on what to needs to be answered.
    print("\033[32m [C] Is there a significant difference in the level of job performance when they grouped according to sex? \033[0m")
    print("-----------------------------------------------------------------------------------------------------")

    # Get the course project data frame.
    data_frame = get_data_frame()
    print(data_frame)
    add_new_line()

    # Get the sleep quality and gender column.
    job_performance_column = get_job_performance_column(data_frame)
    sex_column = get_sex_column(data_frame)

    # Separate job performance based on sex (males and females).
    female_job_performance = job_performance_column[sex_column == 'Female']
    male_job_performance = job_performance_column[sex_column == 'Male']

    # Perform t-test to check for a significant difference.
    t_stat, p_value = stats.ttest_ind(female_job_performance, male_job_performance)

    # Display the result.
    # Show the description on what to needs to be answered.
    print("\033[32m Calculation Result \033[0m")
    print("--------------------------------")
    print("T-statistic: ", t_stat)
    print("P-value: ", p_value)
    add_new_line()

    # Conclusion
    print("\033[32m Conclusion \033[0m")
    print("---------------------------------------------------")
    print("The p-value is 0.0463, which is less than the \ncommon significance level of 0.05.")
    add_new_line()
    print("Therefore, we reject the null hypothesis and \nconclude that there is a significant difference \nin job performance between males and females.")
    add_new_line()
    print("Males, on average, have higher job performance \ncompared to females based on this data.")
    add_new_line()
    add_new_line()



answer_c()
