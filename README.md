# Facebook-Dataset-Analysis

This project analyses Facebook Live Sellers data to understand engagement patterns, post effectiveness, and user behaviour.

## Repository

https://github.com/Prem-101/Facebook-Dataset-Analysis

## Features

- Time-based analysis of post engagement
- Clustering analysis of post types and engagement metrics
- Statistical analysis of reactions, comments, and shares
- Visualisation of engagement patterns

## Project Structure

```
.
├── data_analysis.py     # Core analysis functions
├── FacebookDataset.ipynb # Interactive analysis notebook
└── requirements.txt     # Project dependencies
```

## Requirements

- Python 3.8+
- Required packages listed in requirements.txt

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Prem-101/Facebook-Dataset-Analysis.git
cd Facebook-Dataset-Analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Place your Facebook_Marketplace_data.csv in the project root directory

## Setting up Git Repository

1. Initialize Git repository locally:
```bash
git init
git add .
git commit -m "Initial commit: Facebook Dataset Analysis Project"
```

2. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name your repository (e.g., Facebook-Dataset-Analysis)
   - Leave it empty (don't add README, license, or .gitignore)

3. Link and push to GitHub (if you get a push error, use method A or B):
```bash
git remote add origin https://github.com/YourUsername/Facebook-Dataset-Analysis.git
git branch -M main
```

Method A (if remote is empty):
```bash
git push -u origin main
```

Method B (if remote has existing files):
```bash
git pull origin main --allow-unrelated-histories
# Fix any merge conflicts if they appear
git push -u origin main
```

Replace `YourUsername` with your GitHub username.

## Usage

1. Core Analysis:
```python
import data_analysis as da

# Load and prepare data
df = da.load_and_prepare_data('Facebook_Marketplace_data.csv')

# Add time features
df = da.add_time_features(df)

# Get engagement metrics
metrics = da.get_engagement_metrics(df)
```

2. Interactive Analysis:
```bash
jupyter notebook FacebookDataset.ipynb
```

## Analysis Features

- Time-based engagement analysis
- Post type distribution analysis
- Clustering analysis of engagement patterns
- Correlation analysis of engagement metrics

## License

MIT License

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
