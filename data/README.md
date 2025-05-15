# Dataset Directory

⚠️ **This directory should contain your sensor data files but is excluded from Git.**

## Required Structure

Place your data files in the `data/raw/` directory following this structure:

```
data/
└── raw/
    ├── SA06/                  # Subject 06 folder
    │   ├── S06T01R01.csv     # Sensor recordings
    │   ├── S06T02R01.csv
    │   └── ...
    ├── SA06_label.xlsx        # Subject 06 labels
    ├── SA07/                  # Subject 07 folder
    │   ├── S07T01R01.csv
    │   └── ...
    ├── SA07_label.xlsx        # Subject 07 labels
    └── ...
```

## File Formats

### CSV Files (Sensor Data)
Each CSV file contains accelerometer readings with these columns:
- `FrameCounter`: Sample number
- `TimeStamp(s)`: Time in seconds
- `AccX`: X-axis acceleration (g)
- `AccY`: Y-axis acceleration (g)
- `AccZ`: Z-axis acceleration (g)

### Excel Files (Labels)
Each Excel file contains activity labels with:
- `Task Code (Task ID)`: Activity identifier
- `Trial ID`: Repetition number
- `Fall_onset_frame`: Frame where fall begins
- `Fall_impact_frame`: Frame where person hits ground
- `Description`: Activity description

## Dataset Information

- **Sampling Rate**: 100 Hz
- **Sensor Location**: Waist-mounted accelerometer
- **Activities**: Falls (Task ID ≥ 20) and ADL activities (Task ID < 20)

## Data Not Included

The actual dataset files are **NOT** included in this repository due to:
- Large file sizes
- Potential privacy concerns
- Copyright/licensing restrictions

## How to Obtain Dataset

[Add information about where to obtain or request access to the dataset]

## Moving Your Data

If you have the data elsewhere, move it to the `data/raw/` directory:

```bash
# On Windows
move "path\to\your\SA06" "data\raw\SA06"
move "path\to\your\SA06_label.xlsx" "data\raw\SA06_label.xlsx"

# On Linux/Mac
mv /path/to/your/SA06 data/raw/SA06
mv /path/to/your/SA06_label.xlsx data/raw/SA06_label.xlsx
```

After placing the data, verify the structure matches the example above.
