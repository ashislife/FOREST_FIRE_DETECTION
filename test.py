<<<<<<< HEAD
import pandas as pd
import requests

API_KEY = "c680bef335990c00322c76870c5d60a2"

# Different sensors try kar
sensors = ["VIIRS_SNPP", "MODIS", "VIIRS_NOAA20"]

for sensor in sensors:
    url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{API_KEY}/{sensor}/-125,24,-66,50/1"
    
    try:
        response = requests.get(url, timeout=30)
        print(f"{sensor}: Status {response.status_code}")
        
        if response.status_code == 200:
            df = pd.read_csv(pd.compat.StringIO(response.text))
            print(f"  ✅ {len(df)} fire points")
            break
        else:
            print(f"  ❌ No data")
    except Exception as e:
        print(f"{sensor}: Error - {e}")
















=======
# import pandas as pd
# import requests

# API_KEY = "c680bef335990c00322c76870c5d60a2"

# # Different sensors try kar
# sensors = ["VIIRS_SNPP", "MODIS", "VIIRS_NOAA20"]

# for sensor in sensors:
#     url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{API_KEY}/{sensor}/-125,24,-66,50/1"
    
#     try:
#         response = requests.get(url, timeout=30)
#         print(f"{sensor}: Status {response.status_code}")
        
#         if response.status_code == 200:
#             df = pd.read_csv(pd.compat.StringIO(response.text))
#             print(f"  ✅ {len(df)} fire points")
#             break
#         else:
#             print(f"  ❌ No data")
#     except Exception as e:
#         print(f"{sensor}: Error - {e}")

















import requests

API_KEY = "c680bef335990c00322c76870c5d60a2"
url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{API_KEY}/VIIRS_NOAA20/-125,24,-66,50/1"

response = requests.get(url)
print(response.status_code)  # Jab 200 aayega tab theek
>>>>>>> ef667b6 (first commit)
