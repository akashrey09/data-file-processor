def generate_report(original_df,cleaned_df,duplicates_removed):
    # ===== DATA CLEANING REPORT =====
    # Original row count   : 10
    # Cleaned row count    : 7
    # Duplicates removed   : 2
    # Null values found    : 3
    # ================================
    # Column Statistics:
    #     age  salary
    # count  7.0     7.0
    # mean   28.0  50000
    # ...
    # ================================

    print("===== DATA CLEANING REPORT =====")
    print(f"Original row count   : {len(original_df)}")
    print(f"Cleaned row count    : {len(cleaned_df)}")
    print(f"Duplicates removed   : {duplicates_removed}")
    print(f"Null values found    : \n{original_df.isnull().sum()}")
    print("================================")
    print("Column Statistics:")
    print(cleaned_df.describe())
    print("================================")