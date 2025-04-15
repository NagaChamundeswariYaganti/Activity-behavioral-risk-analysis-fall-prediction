# Activity Behavioral Risk Analysis - Fall Detection in Elderly People

**Project Date: April 2025**

A machine learning project that analyzes human activity patterns using sensor data (accelerometer and gyroscope) to detect potential fall risks in elderly people. This project uses the UCI Human Activity Recognition (HAR) Dataset to classify different activities and identify abnormal patterns that could indicate fall risk.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Dataset](#dataset)
- [Results](#results)
- [Future Improvements](#future-improvements)

## Overview

This project implements a machine learning pipeline to:
1. Extract statistical features from sensor data (accelerometer and gyroscope)
2. Train a Random Forest classifier to recognize different activities
3. Identify patterns that could indicate fall risk in elderly individuals

The system can classify activities such as:
- Walking
- Walking Upstairs
- Walking Downstairs
- Sitting
- Standing
- Laying

## Features

- **Feature Extraction**: Automatically extracts statistical features (mean, std, max, min) from sensor data
- **Machine Learning Model**: Uses Random Forest classifier for robust activity recognition
- **Easy to Use**: Simple command-line interface for running the pipeline
- **Well Documented**: Clean code with detailed comments for beginners
- **Reproducible**: Fixed random seeds ensure consistent results

## Project Structure

```
FallDetectionProject/
│
├── data/                          # Data directory
│   ├── UCI HAR Dataset/          # Original dataset (download separately)
│   ├── X_train.csv               # Extracted training features
│   ├── y_train.csv               # Training labels
│   ├── X_test.csv                # Extracted test features
│   ├── y_test.csv                # Test labels
│   └── activity_model.pkl        # Trained model (generated)
│
├── src/                          # Source code
│   ├── feature_extraction.py    # Feature extraction script
│   └── train_model.py           # Model training script
│
├── README.md                     # This file
├── requirements.txt              # Python dependencies
└── .gitignore                   # Git ignore file
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd FallDetectionProject
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Download the Dataset

1. Download the UCI HAR Dataset from: https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones
2. Extract the dataset
3. Place the `UCI HAR Dataset` folder in the `data/` directory

Your directory structure should look like:
```
data/
└── UCI HAR Dataset/
    ├── train/
    ├── test/
    └── ...
```

## Usage

### Step 1: Extract Features

First, extract features from the raw sensor data:

```bash
python src/feature_extraction.py
```

This will:
- Load the UCI HAR Dataset
- Extract statistical features from accelerometer and gyroscope data
- Save processed features to CSV files in the `data/` folder

**Expected Output:**
```
Found dataset at: data/UCI HAR Dataset/

Loading Training Data...
Training data shape: (7352, 128, 9)
  - Samples: 7352
  - Timesteps: 128
  - Channels: 9

Loading Test Data...
Test data shape: (2947, 128, 9)

Extracting Features...
Training features shape: (7352, 36)
Test features shape: (2947, 36)

Saving features to CSV files...

Feature extraction complete!
```

### Step 2: Train the Model

Train the Random Forest classifier:

```bash
python src/train_model.py
```

This will:
- Load the extracted features
- Train a Random Forest classifier
- Evaluate the model on test data
- Save the trained model to `data/activity_model.pkl`

**Expected Output:**
```
Loading processed data from CSV files...
Training data loaded: 7352 samples, 36 features
Test data loaded: 2947 samples

Training Random Forest Classifier...
Model training complete!

Evaluating model on test data...

Overall Accuracy: 0.XXXX (XX.XX%)

Detailed Classification Report:
...
```

## How It Works

### 1. Feature Extraction

The feature extraction process:
- Loads raw sensor data from 9 channels (3 accelerometer + 3 body acceleration + 3 gyroscope)
- For each channel, calculates 4 statistical features:
  - **Mean**: Average value
  - **Standard Deviation**: Measure of variability
  - **Maximum**: Peak value
  - **Minimum**: Lowest value
- Results in 36 features per sample (9 channels × 4 features)

### 2. Model Training

The Random Forest classifier:
- Uses 100 decision trees
- Each tree votes on the activity class
- Final prediction is the majority vote
- Handles non-linear relationships well
- Provides feature importance scores

### 3. Activity Classification

The model predicts one of 6 activities:
1. Walking
2. Walking Upstairs
3. Walking Downstairs
4. Sitting
5. Standing
6. Laying

## Dataset

This project uses the **UCI Human Activity Recognition Using Smartphones Dataset**.

**Dataset Information:**
- **Source**: UCI Machine Learning Repository
- **Dataset URL**: https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones
- **Sensors**: Accelerometer and Gyroscope
- **Activities**: 6 different activities
- **Training Samples**: 7,352
- **Test Samples**: 2,947
- **Features**: 561 (raw), 36 (after our extraction)

**Citation:**

If you use this dataset in your research, please cite the following paper:

Anguita, D., Ghio, A., Oneto, L., Parra, X., & Reyes-Ortiz, J. L. (2013). Human Activity Recognition on Smartphones using a Multiclass Hardware-Friendly Support Vector Machine. In *International Workshop of Ambient Assisted Living (IWAAL 2012)* (pp. 216-223). Vitoria-Gasteiz, Spain.

**BibTeX Format:**
```bibtex
@inproceedings{anguita2013human,
  title={Human Activity Recognition on Smartphones using a Multiclass Hardware-Friendly Support Vector Machine},
  author={Anguita, Davide and Ghio, Alessandro and Oneto, Luca and Parra, Xavier and Reyes-Ortiz, Jorge L},
  booktitle={International Workshop of Ambient Assisted Living (IWAAL 2012)},
  pages={216--223},
  year={2013},
  address={Vitoria-Gasteiz, Spain}
}
```

**APA Format:**
Anguita, D., Ghio, A., Oneto, L., Parra, X., & Reyes-Ortiz, J. L. (2013). Human Activity Recognition on Smartphones using a Multiclass Hardware-Friendly Support Vector Machine. In *International Workshop of Ambient Assisted Living (IWAAL 2012)* (pp. 216-223). Vitoria-Gasteiz, Spain.

## Results

The model typically achieves:
- **Accuracy**: ~85-95% (depending on hyperparameters)
- **Per-class Performance**: Detailed metrics shown in classification report

To see detailed results, run the training script and check the classification report.

## Future Improvements

Potential enhancements for this project:

1. **Advanced Features**: Add more sophisticated features like:
   - Frequency domain features (FFT)
   - Correlation between axes
   - Signal magnitude area
   - Energy features

2. **Deep Learning**: Try neural networks:
   - LSTM for temporal patterns
   - CNN for spatial patterns
   - Transformer models

3. **Fall Detection**: Adapt specifically for fall detection:
   - Binary classification (Fall vs. Non-fall)
   - Impact detection algorithms
   - Orientation change detection

4. **Real-time Processing**: 
   - Stream processing capabilities
   - Mobile app integration
   - Edge device deployment

5. **Model Improvements**:
   - Hyperparameter tuning
   - Cross-validation
   - Ensemble methods
   - Feature selection

## Notes for Beginners

### Understanding the Code

- **`feature_extraction.py`**: Processes raw sensor data into features that the model can understand
- **`train_model.py`**: Trains a machine learning model to recognize activities

### Key Concepts

- **Features**: Numerical values that describe the data (e.g., mean acceleration)
- **Labels**: The correct answers (e.g., "Walking", "Sitting")
- **Training**: Teaching the model using examples
- **Testing**: Checking if the model learned correctly

### Common Issues

1. **Dataset not found**: Make sure the `UCI HAR Dataset` folder is in the `data/` directory
2. **Import errors**: Run `pip install -r requirements.txt` to install dependencies
3. **File not found**: Run `feature_extraction.py` before `train_model.py`

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is open source and available for educational purposes.

## Authors

Fall Detection Project Team  
**Date**: April 2025

