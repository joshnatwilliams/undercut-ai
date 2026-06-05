import fastf1
from pathlib import Path

Path("cache").mkdir(exist_ok=True)
Path("data").mkdir(exist_ok=True)

fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2026, "Canadian Grand Prix", "R")
session.load()

laps = session.laps[
    ["Driver", "LapNumber", "LapTime", "Compound", "Stint", "PitOutTime", "PitInTime"]
]

output_path = "data/2026_canadian_gp_laps.csv"
laps.to_csv(output_path, index=False)

print(f"Saved {output_path}")
print(laps.head())