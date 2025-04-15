"""
Feature Extraction Module
=========================
This module extracts statistical features from sensor data (accelerometer and gyroscope)
for activity recognition and fall detection in elderly people.

The features extracted include:
- Mean: Average value of the signal
- Standard Deviation: Measure of signal variability
- Maximum: Peak value in the signal
- Minimum: Lowest value in the signal

Dataset:
UCI Human Activity Recognition Using Smartphones Dataset
https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones

Citation:
Anguita, D., Ghio, A., Oneto, L., Parra, X., & Reyes-Ortiz, J. L. (2013).
Human Activity Recognition on Smartphones using a Multiclass Hardware-Friendly Support Vector Machine.
In International Workshop of Ambient Assisted Living (IWAAL 2012) (pp. 216-223).
Vitoria-Gasteiz, Spain.

Author: Fall Detection Project Team
Date: April 2025
"""

import pandas as pd
import numpy as np
import os


def load_file(filepath):
    """
    Load a single data file from the UCI HAR Dataset.
    
    Args:
        filepath (str): Path to the data file (.txt format)
    
    Returns:
        numpy.ndarray: Array containing the sensor data values
    """
    dataframe = pd.read_csv(filepath, header=None, delim_whitespace=True)
    return dataframe.values


def load_group(filenames, prefix=''):
    """
    Load multiple sensor data files and stack them together.
    
    Args:
        filenames (list): List of filenames to load
        prefix (str): Directory path prefix for the files
    
    Returns:
        numpy.ndarray: 3D array with shape (samples, timesteps, channels)
    """
    loaded = []
    for name in filenames:
        data = load_file(prefix + name)
        loaded.append(data)
    loaded = np.dstack(loaded)
    return loaded


def load_dataset_group(group, prefix=''):
    """
    Load all sensor data files for a dataset group (train or test).
    
    Args:
        group (str): Either 'train' or 'test'
        prefix (str): Base path to the dataset directory
    
    Returns:
        tuple: (X, y) where X is sensor data and y is activity labels
    """
    filepath = prefix + group + '/Inertial Signals/'
    filenames = []
    
    filenames += [
        f'total_acc_x_{group}.txt',
        f'total_acc_y_{group}.txt',
        f'total_acc_z_{group}.txt',
        f'body_acc_x_{group}.txt',
        f'body_acc_y_{group}.txt',
        f'body_acc_z_{group}.txt',
        f'body_gyro_x_{group}.txt',
        f'body_gyro_y_{group}.txt',
        f'body_gyro_z_{group}.txt'
    ]
    
    X = load_group(filenames, filepath)
    y = load_file(prefix + group + f'/y_{group}.txt')
    
    return X, y


def extract_features(X):
    """
    Extract statistical features from sensor data.
    
    Args:
        X (numpy.ndarray): Input data with shape (samples, timesteps, channels)
    
    Returns:
        numpy.ndarray: Feature matrix with shape (samples, channels * 4)
    """
    features = []
    for i in range(X.shape[0]):
        sample_features = []
        for channel in range(X.shape[2]):
            channel_data = X[i, :, channel]
            sample_features.append(np.mean(channel_data))
            sample_features.append(np.std(channel_data))
            sample_features.append(np.max(channel_data))
            sample_features.append(np.min(channel_data))
        features.append(sample_features)
    return np.array(features)


def main():
    """Extract features from the UCI HAR Dataset."""
    possible_paths = [
        os.path.join('data', 'UCI HAR Dataset'),
        os.path.join('..', 'UCI HAR Dataset'),
        'UCI HAR Dataset'
    ]
    
    dataset_path = None
    for path in possible_paths:
        if os.path.exists(path):
            dataset_path = path + '/'
            break
    
    if dataset_path is None:
        print("Error: 'UCI HAR Dataset' not found.")
        for path in possible_paths:
            print(f"  - {path}")
        return
    
    print(f"Found dataset at: {dataset_path}")
    
    print("\nLoading Training Data...")
    X_train_raw, y_train = load_dataset_group('train', dataset_path)
    print(f"Training data shape: {X_train_raw.shape}")
    
    print("\nLoading Test Data...")
    X_test_raw, y_test = load_dataset_group('test', dataset_path)
    print(f"Test data shape: {X_test_raw.shape}")
    
    print("\nExtracting Features...")
    X_train_features = extract_features(X_train_raw)
    X_test_features = extract_features(X_test_raw)
    print(f"Training features shape: {X_train_features.shape}")
    print(f"Test features shape: {X_test_features.shape}")
    
    os.makedirs('data', exist_ok=True)
    
    print("\nSaving features to CSV files...")
    files_to_save = [
        (X_train_features, 'X_train.csv'),
        (y_train, 'y_train.csv'),
        (X_test_features, 'X_test.csv'),
        (y_test, 'y_test.csv')
    ]
    
    for data, filename in files_to_save:
        pd.DataFrame(data).to_csv(os.path.join('data', filename), index=False)
    
    print("\nFeature extraction complete!")


if __name__ == "__main__":
    main()
