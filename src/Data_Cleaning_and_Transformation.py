import pandas as pd


# Removing Duplicates from Data
def remove_duplicates(data_frame):
    cleaned_data = data_frame.drop_duplicates()
    return cleaned_data


# Data Normalization
def normalize_data(data_frame):
    normalized_data = (data_frame - data_frame.mean()) / (data_frame.max() - data_frame.min())
    return normalized_data


# Handling Missing Values
def handle_missing_values(data_frame):
    filled_data = data_frame.fillna(method = 'ffill')
    return filled_data
