import data_analysis as da
import argparse
import subprocess

def git_commit(message):
    try:
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)
        print("Changes committed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error committing changes: {e}")

def main():
    parser = argparse.ArgumentParser(description='Facebook Dataset Analysis')
    parser.add_argument('--data', type=str, required=True, help='Path to dataset CSV file')
    parser.add_argument('--commit', type=str, help='Commit changes with provided message')
    args = parser.parse_args()

    # Load and analyze data
    df = da.load_and_prepare_data(args.data)
    df = da.add_time_features(df)
    metrics = da.get_engagement_metrics(df)
    
    print("Analysis complete. Check results in the output directory.")

    if args.commit:
        git_commit(args.commit)

if __name__ == "__main__":
    main()
