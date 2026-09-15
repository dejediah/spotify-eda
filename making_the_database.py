import glob
import sqlite3
import pandas as pd

# 1. Use wildcards (*) to match all JSON files in the folder
path_pattern = "C:/Users/armin/Downloads/spredictify/my_spotify_data/*.json"
files = glob.glob(path_pattern)

# Debug check: verify files were found before concatenating
if not files:
    raise FileNotFoundError(
        f"No JSON files found! Check that this exact path exists:\n{path_pattern}"
    )

print(f"Found {len(files)} files to load.")

df = pd.concat([pd.read_json(f) for f in files], ignore_index=True)

# 2. Connect to local SQLite database file
conn = sqlite3.connect("spotify_history.db")

# 3. Save to SQL table
df.to_sql("raw_streaming_history", conn, if_exists="replace", index=False)

# 4. Run a quick SQL query test
sample = pd.read_sql_query(
    "SELECT * FROM raw_streaming_history LIMIT 5", conn
)
print(sample)

conn.close()