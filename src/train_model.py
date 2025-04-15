"""
Model Training Module
=====================
This module trains a machine learning model to classify human activities
based on sensor data features. The model can identify activities like:
- Walking
- Walking Upstairs
- Walking Downstairs
- Sitting
- Standing
- Laying

This is useful for fall detection in elderly people by recognizing
abnormal activity patterns.

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
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


ACTIVITY_LABELS = {
    1: 'Walking',
    2: 'Walking Upstairs',
    3: 'Walking Downstairs',
    4: 'Sitting',
    5: 'Standing',
    6: 'Laying'
}


def load_data():
    """
    Load the processed feature data from CSV files.
    
    Returns:
        tuple: (X_train, y_train, X_test, y_test) containing:
            - X_train: Training features
            - y_train: Training labels
            - X_test: Test features
            - y_test: Test labels
    
    Raises:
        FileNotFoundError: If the feature files don't exist
    """
    print("Loading processed data from CSV files...")
    
    try:
        X_train = pd.read_csv(os.path.join('data', 'X_train.csv'))
        y_train = pd.read_csv(os.path.join('data', 'y_train.csv')).values.ravel()
        X_test = pd.read_csv(os.path.join('data', 'X_test.csv'))
        y_test = pd.read_csv(os.path.join('data', 'y_test.csv')).values.ravel()
        
        print(f"Training data loaded: {X_train.shape[0]} samples, {X_train.shape[1]} features")
        print(f"Test data loaded: {X_test.shape[0]} samples")
        
        return X_train, y_train, X_test, y_test
        
    except FileNotFoundError:
        print("Error: Processed data files not found!")
        print("Please run 'python src/feature_extraction.py' first to extract features.")
        raise


def train_model(X_train, y_train):
    """
    Train a Random Forest classifier on the training data.
    
    Args:
        X_train (pandas.DataFrame): Training features
        y_train (numpy.ndarray): Training labels
    
    Returns:
        RandomForestClassifier: Trained model
    """
    print("\nTraining Random Forest Classifier...")
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    print("Model training complete!")
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on test data.
    
    Args:
        model: Trained classifier
        X_test (pandas.DataFrame): Test features
        y_test (numpy.ndarray): Test labels
    
    Returns:
        numpy.ndarray: Predicted labels
    """
    print("\nEvaluating model on test data...")
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nOverall Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    
    unique_labels = sorted(list(set(y_test)))
    activity_names = [ACTIVITY_LABELS[label] for label in unique_labels]
    
    print("\n" + "="*60)
    print("Classification Report:")
    print("="*60)
    print(classification_report(y_test, y_pred, target_names=activity_names, digits=4))
    
    print("\n" + "="*60)
    print("Confusion Matrix:")
    print("="*60)
    cm = confusion_matrix(y_test, y_pred)
    print("\nRows = Actual, Columns = Predicted")
    print("\n", cm)
    
    return y_pred


def save_model(model, filepath='data/activity_model.pkl'):
    """Save the trained model to a file."""
    print(f"\nSaving model to {filepath}...")
    joblib.dump(model, filepath)
    print("Model saved successfully!")


def main():
    """Train and evaluate the activity recognition model."""
    try:
        X_train, y_train, X_test, y_test = load_data()
        model = train_model(X_train, y_train)
        evaluate_model(model, X_test, y_test)
        save_model(model)
        
        print("\n" + "="*60)
        print("Training pipeline complete!")
        print("="*60)
        
    except FileNotFoundError:
        print("\nPlease run feature extraction first:")
        print("  python src/feature_extraction.py")
    except Exception as e:
        print(f"\nError occurred: {e}")
        raise


if __name__ == "__main__":
    main()
