import pandas as pd
import numpy as np
import time
import gc
import psutil
import os
import matplotlib.pyplot as plt

def plot_distribution(df, column):
    """
    Plot the distribution of a specified column in a DataFrame, take input a dataframe and one column
    """
    # Create a histogram to show the distribution
    plt.figure(figsize=(10, 2))
    plt.hist(df[column], bins=40, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def average_by_level(df, level_col, value_col):
    """
    Calculate average value by level of a T column of dataframe and return the result as dict
    Take 3 input: dataframe, level column, value column of T 
    """

    # Group by the level column and calculate the mean of the value column
    averages = df.groupby(level_col)[value_col].mean()
    # Convert the resulting Series to a dictionary
    return averages.to_dict()

def fill_value(row, value_col, result_dict):
    """
    Fill NaN values in a T column with corresponding average values from a dictionary 
    Only if T column is null, otherwise returns original value
    """

    if pd.isna(row[value_col]):
        return round(result_dict[row['Level']],1)
    else:
        return round(row[value_col],1)
    
# Custom descriptive statistics
def custom_describe(df):
    """
    Calculate descriptive statistics for each column in the DataFrame.
    Receive the whole dataframe as input
    How it works: 
    1. Each keys in the dict contained a measure of every columns in dataframe, in a form a pandas series
    2. The dict is converted back into a dataframe, and transposed for the dimension to match the original describe method
    """
    
    stats = {
        'count': df.count(),         # Number of non-missing values
        'mean': df.mean(),           # Mean of values
        'std': df.std(),             # Standard deviation of values
        'min': df.min(),             # Minimum value
        '25%': df.quantile(0.25),    # 25th percentile (first quartile)
        '50%': df.median(),          # Median (50th percentile)
        '75%': df.quantile(0.75),    # 75th percentile (third quartile)
        'max': df.max()              # Maximum value
    }
    return pd.DataFrame(stats).T

def matrix_mult(size):
    """
    Standard cn^3 matrix multiplication with matrices A and B
    """
    
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    return np.dot(A, B)

def selection_sort(random_list):
    """
    Sorts through a list inefficiently by finding the smallest component in the list
    and repositioned each component in the list
    This will take a list as input and return the sorted list
    """

    # Iterate through the entire list
    for i in range(len(random_list)):

        # Find the smallest element in the list
        smallest = min(random_list[i:]) 
        
        # Find the index of the smallest element
        smallest_index = random_list.index(smallest, i)  
        
        # Swap the smallest element with the current element at index i
        random_list[i], random_list[smallest_index] = random_list[smallest_index], random_list[i]

    return random_list

def is_substring(substring, main_string):
    """
    Sorts through each slice in the main string looking for the substring
    This function requires 2 inputs: substring and the mainstring
    In case the substring match the mainstring, it returns TRUE
    """

    # Get the length of the substring and the main string
    len_sub = len(substring)
    len_main = len(main_string)
    
    # Loop through the main string to check for the substring, each slice of the main string equals the length of the substring
    for i in range(len_main - len_sub + 1):

        # Check if the current slice of main string matches the substring. If matched returns True and end the function
        if main_string[i:i+len_sub] == substring:
            return True
    return False