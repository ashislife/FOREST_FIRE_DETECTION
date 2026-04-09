import pandas as pd
import requests
from io import StringIO
from config import NASA_API_KEY


def get_live_fires():
    """Fetch real-time satellite data from NASA"""

    sensors = ["VIIRS_NOAA20_NRT", "VIIRS_SNPP_NRT", "MODIS_NRT"]
    areas = ["68,6,97,37", "90,20,110,30"]  # India + SE Asia (fire zone)

    for sensor in sensors:
        for area in areas:
            url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{NASA_API_KEY}/{sensor}/{area}/1"

            try:
                print(f"Trying: {sensor} | {area}")

                response = requests.get(url, timeout=30)

                if response.status_code == 200 and "latitude" in response.text:
                    df = pd.read_csv(StringIO(response.text))

                    if not df.empty:
                        print(f"🔥 Found {len(df)} fires")

                        cols = ['latitude', 'longitude', 'bright_ti4', 'bright_ti5',
                                'scan', 'track', 'acq_time', 'frp']

                        available = [c for c in cols if c in df.columns]
                        return df[available]

            except Exception as e:
                print("Error:", e)
                continue

    return None