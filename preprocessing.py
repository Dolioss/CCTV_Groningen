def preprocessed_data(data):
    import pandas as pd
    import re

    df = pd.read_csv(data)

    # Dropping unnecessary columns
    df = df.drop(columns=['StartDate', 'EndDate', 'Status', 'Progress', 'Duration (in seconds)', 'Finished', 'RecordedDate', 'DistributionChannel', 'UserLanguage', 'Consent form'])
    df = df.drop(index=1)

    # Combining the first two rows to form the column names
    new_header = df.columns.astype(str) + '_' + df.iloc[0].astype(str)
    df.columns = new_header

    # Keep only rows where the answer is 'Yes'. The people that awnsered 'No' (or those that did not awnser at all), are not relevant for the study
    df = df[df["Q0_Do you live in or frequently visit the city of Groningen?"] == "Yes"].reset_index(drop=True)

    # Extract only numbers from Q1
    Q1 = "Q1_How many CCTV cameras for surveillance do you think the municipality of Groningen currently owns?"
    df[Q1] = df[Q1].astype(str).apply(lambda x: re.search(r'\d+', x).group(0) if re.search(r'\d+', x) else None)
    df[Q1] = pd.to_numeric(df[Q1], errors='coerce').astype('Int64')
    
    return df