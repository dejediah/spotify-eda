import pandas as pd
import sqlite3

conn = sqlite3.connect("spotify_history.db")
df = pd.read_sql_query("SELECT * FROM raw_streaming_history", conn)

# Overhead exploration
print("Rows:", len(df))
print("Columns:", len(df.columns))
df.info()

# 1. Filter out skips (< 30 seconds) and non-song streams
ms_col = "ms_played"
noSkips_df = df[(df[ms_col] >= 30000) & (df["skipped"] != True)].copy()

# 2. Convert UTC timestamps to Philippine Standard Time (PHT / UTC+8)
noSkips_df["ts"] = pd.to_datetime(noSkips_df["ts"], utc=True)
noSkips_df["ts"] = (
    noSkips_df["ts"].dt.tz_convert("Asia/Manila").dt.strftime("%Y-%m-%d %H:%M:%S")
)

# 3. Add human-readable minutes column
noSkips_df["minutes_played"] = (noSkips_df[ms_col] / (1000 * 60)).round(2)

# 4. Drop unnecessary columns (removed duplicated 'incognito_mode')
cols_to_drop = [
    "skipped",
    "offline",
    "offline_timestamp",
    "incognito_mode",
    "platform",
    "episode_name",
    "episode_show_name",
    "spotify_episode_uri",
]
clean_df = noSkips_df.drop(columns=cols_to_drop, errors="ignore")

# 5. Overwrite the clean table reproducibly in SQLite
clean_df.to_sql("clean_streaming_history", conn, if_exists="replace", index=False)

print(f"\n✅ Filtered out {len(df) - len(clean_df)} skipped/short tracks.")
print("✅ Converted timestamps to Philippine Standard Time (Asia/Manila).")
print("Clean rows saved to table 'clean_streaming_history'.")

conn.close()