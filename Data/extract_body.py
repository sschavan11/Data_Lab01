import pandas as pd

# Load CSV from your local path
df = pd.read_csv(r"C:\Northeastern Univesity\Academic\MLOps\Labs\Lab01-Data\Data\kaggle_RC_2019-05.csv", encoding='latin-1')

# Extract only body column and save as plain text in same folder
df["body"].dropna().to_csv(
    r"C:\Northeastern Univesity\Academic\MLOps\Labs\Lab01-Data\Data\reddit_text.txt",
    index=False,
    header=False
)

print("Body column extracted successfully into reddit_text.txt")