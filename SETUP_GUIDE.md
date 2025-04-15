# Setup Guide for GitHub Repository

## Pre-Upload Checklist

### 1. Organize Your Files

Move your data files to the `data/raw/` directory:

```
Fall detection/
├── data/                    # CREATE THIS FOLDER
│   └── raw/                 # CREATE THIS SUBFOLDER
│       ├── SA06/           # Move subject folders here
│       │   ├── S06T01R01.csv
│       │   └── ...
│       ├── SA06_label.xlsx  # Move label files here
│       ├── SA07/
│       └── ...
├── fall_detection_analysis.ipynb
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

### 2. Update the Notebook

The notebook has been updated to use relative paths:
- `base_path = os.getcwd()` instead of hardcoded paths
- Looks for data in `./data/` directory

### 3. Clear Notebook Outputs

Before pushing to GitHub:
1. Open the notebook in Jupyter
2. Go to: **Kernel** → **Restart & Clear Output**
3. Save the notebook

This reduces file size and keeps output private.

### 4. Test Locally

1. Create a new virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the notebook to ensure it works with new paths

### 5. Initialize Git Repository

```bash
# Initialize repo
git init

# Add files (data/ is excluded via .gitignore)
git add .

# First commit
git commit -m "Initial commit: Fall detection ML project"

# Add remote (replace with your GitHub repo URL)
git remote add origin https://github.com/yourusername/fall-detection.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Recommended Folder Structure

```
fall-detection/                    # Repository root
│
├── data/                          # Data directory
│   ├── raw/                      # NOT in Git (see .gitignore)
│   │   ├── SA06/
│   │   ├── SA07/
│   │   └── ...
│   └── README.md                 # Instructions for data placement
│
├── notebooks/                     # Optional: for multiple notebooks
│   └── fall_detection_analysis.ipynb
│
├── src/                           # Optional: for Python modules
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── features.py
│   └── models.py
│
├── models/                        # Optional: for saved models
│   └── .gitkeep
│
├── outputs/                       # Optional: for plots/results
│   └── .gitkeep
│
├── tests/                         # Optional: unit tests
│   └── test_features.py
│
├── .gitignore                     # Git ignore rules
├── LICENSE                        # MIT License
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
└── setup.py                       # Optional: for pip install
```

## Optional Enhancements

### Create a data README

Create `data/README.md`:
```markdown
# Dataset Directory

Place your sensor data files here following this structure:

\`\`\`
data/
├── SA06/
│   ├── S06T01R01.csv
│   ├── S06T02R01.csv
│   └── ...
├── SA06_label.xlsx
└── ...
\`\`\`

## Data Format

- CSV files: Accelerometer readings with columns: FrameCounter, TimeStamp(s), AccX, AccY, AccZ
- Excel files: Activity labels with task codes and fall timing information

## Dataset Source

[Add information about where to obtain the dataset]
```

### Add GitHub Actions (Optional)

Create `.github/workflows/test.yml` for automated testing:
```yaml
name: Test Notebook

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Test notebook execution
      run: jupyter nbconvert --to notebook --execute fall_detection_analysis.ipynb
```

## After Publishing

1. Add topics/tags on GitHub: `machine-learning`, `fall-detection`, `random-forest`, `wearable-sensors`
2. Add a shield badge to README.md
3. Create a release/tag for version 1.0.0
4. Consider adding example data (small subset) for demo purposes
5. Write a blog post or article about your project

## Privacy & Security

- ✅ No personal paths in code
- ✅ No raw data in repository
- ✅ Sensitive outputs cleared
- ✅ .gitignore configured properly

You're ready to publish! 🚀
