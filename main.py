import argparse
from utils import validate_file
from cleaner import load_csv, remove_duplicates, handle_missing
from stats import generate_report

def main():
    
    parser = argparse.ArgumentParser(description="SIMPLE CLI FOR FILE PROCESSING")
    parser.add_argument('--input', type=str, required=True, help="Path to input CSV")
    parser.add_argument('--fill-missing', choices=['drop', 'mean', 'mode'], required=True)
    args = parser.parse_args()
    validate_file(args.input) 
    original_df = load_csv(args.input)
    df, duplicates_removed = remove_duplicates(original_df)
    df_1 = handle_missing(df,args.fill_missing)
    generate_report(original_df,df_1 ,duplicates_removed)
    df_1.to_csv('cleaned_output.csv', index=False) 

if __name__ == "__main__":
    main()

   