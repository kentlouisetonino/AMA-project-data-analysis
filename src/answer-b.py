# Student ID: 2022-0076767
# Course: MATH6200 - Data Analysis
# Activity: Course Project (Week 13)
# Question: [B] Is there a significant difference in the level of sleep quality when they grouped according to sex?
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

def get_sleep_quality_column(data_frame: pd.DataFrame):
    return data_frame['Sleep Quality']

def get_job_performance_column(data_frame: pd.DataFrame):
    return data_frame['Job Performance']

def get_sex_column(data_frame: pd.DataFrame):
    return data_frame['Sex']

def answer_b():
    # Clear the terminal first.
    clear_terminal()
    add_new_line()

    # Show the description on what to needs to be answered.
    print("\033[32m Is there a significant difference in the level of sleep quality when they grouped according to sex? \033[0m")
    print("-----------------------------------------------------------------------------------------------------")

    # Get the course project data frame.
    data_frame = get_data_frame()
    print(data_frame)
    add_new_line()

    # Get the sleep quality and gender column.
    sleep_quality_column = get_sleep_quality_column(data_frame)
    sex_column = get_sex_column(data_frame)

    # Separate sleep quality based on sex (males and females).
    female_sleep_quality = sleep_quality_column[sex_column == 'Female']
    male_sleep_quality = sleep_quality_column[sex_column == 'Male']

    # Perform t-test to check for a significant difference
    t_stat, p_value = stats.ttest_ind(female_sleep_quality, male_sleep_quality)

    # Display the result.
    # Show the description on what to needs to be answered.
    print("\033[32m Calculation Result \033[0m")
    print("--------------------------------")
    print("T-statistic: ", t_stat)
    print("P-value: ", p_value)
    add_new_line()

    # Conclusion
    print("\033[32m Interpretation and Conclusion \033[0m")
    print("---------------------------------------------------")
    print("Here, a T-statistic of 2.7778 indicates that the \ndifference in sleep quality between females and \nmales is significant in the context of the \nvariability of the data.")
    add_new_line()
    print("A P-value of 0.0097 is very small, much lower \nthan the common significance threshold of 0.05. \nThis suggests that there is a statistically \nsignificant difference between the sleep \nquality of females and males.")
    add_new_line()
    print("This result means that the data provides strong \nevidence that the average sleep quality is \ndifferent for females and males.")
    add_new_line()



answer_b()
