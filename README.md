# Fall Detection Using Machine Learning

A prototype machine learning system that analyzes accelerometer time-series data to distinguish falls from normal daily activities, demonstrating the feasibility of automated fall detection for elderly care and health monitoring applications.

## Problem Statement

Falls are a leading cause of injury among elderly populations. Traditional monitoring systems rely on manual observation or basic threshold-based sensors, which often produce false alarms or miss actual fall events. This project explores whether machine learning can accurately detect falls using wearable accelerometer sensors.

## Approach

**Data Processing**
- Sliding window technique: 2-second segments with 50% overlap (200 samples at 100Hz)
- Multi-axis accelerometer data (AccX, AccY, AccZ) plus total acceleration magnitude

**Feature Engineering**
- **Time-domain**: Mean, standard deviation, max, min, range, Signal Magnitude Area (37 features total)
- **Frequency-domain**: FFT-based dominant frequency and spectral energy to capture impact vibrations

**Classification**
- Random Forest (100 trees) with class balancing to handle imbalanced fall/non-fall distribution
- 80/20 train-test split with stratification
- Focus on both precision (minimizing false alarms) and recall (catching actual falls)

## Dataset

The analysis uses 3-axis accelerometer data sampled at 100Hz from multiple subjects performing controlled fall simulations and Activities of Daily Living (ADL) such as walking, sitting, and standing. Labels include task codes and precise fall timing (onset/impact frames).

**Data not included**: Raw sensor files and labels are excluded from this repository due to data usage restrictions. The notebook expects data in `data/raw/` with subject folders (SA##) containing CSV files.

## Tools & Technologies

- **Python 3.8+**: Core implementation
- **Data Processing**: pandas, numpy
- **Machine Learning**: scikit-learn (Random Forest, train-test split, metrics)
- **Signal Processing**: scipy (FFT for frequency analysis)
- **Visualization**: matplotlib, seaborn
- **Environment**: Jupyter Notebook

## Results

The prototype achieves strong performance on the test dataset:
- **Accuracy**: >95% in distinguishing falls from ADL
- **Detection Latency**: <2 seconds (sliding window approach)
- **Most Important Features**: Total acceleration statistics (max, range) and frequency-domain spectral energy

**Confusion matrix and classification metrics** (precision, recall, F1-score) are available in the notebook with detailed per-class breakdowns.

**Note**: This is a proof-of-concept trained on controlled laboratory data. Real-world deployment would require additional validation, edge case testing, and hardware optimization.

## Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/fall-detection.git
cd fall-detection
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Obtain dataset** (separately) and place in `data/raw/` structure

4. **Run the notebook**
```bash
jupyter notebook fall_detection_analysis.ipynb
```

The notebook includes:
- Data loading and exploratory analysis
- Feature extraction pipeline
- Model training and evaluation
- Real-time detection simulation

## Repository Structure

```
fall-detection/
├── fall_detection_analysis.ipynb    # Main analysis notebook
├── requirements.txt                  # Python dependencies
├── data/                            # Data directory (excluded from repo)
│   └── README.md                    # Data setup instructions
├── .gitignore                       # Excludes data files
└── README.md                        # Project overview
```

## Limitations & Future Work

This prototype was trained on controlled laboratory data with specific experimental conditions:
- Limited subject diversity (age, body type, sensor placement)
- Simulated falls may differ from real-world scenarios
- No testing on continuous multi-hour recordings
- Power consumption not optimized for wearable deployment

**Potential improvements:**
- Validate on diverse populations and real-world conditions
- Add gyroscope data for orientation context
- Implement real-time inference on embedded hardware
- Develop alert system integration (SMS, app notifications)

## License

MIT License - see [LICENSE](LICENSE) for details.
