import requests
import pandas as pd
import json


def fetch_data_for_parcel(parcel_value):
    url = "https://services.arcgis.com/8Pc9XBTAsYuxx9Ny/arcgis/rest/services/PaGISView_gdb/FeatureServer/0/query"
    params = {
        "where": "FOLIO = '{}'".format(parcel_value),
        "outFields": "FOLIO,DOS_1,PRICE_1,X_COORD,Y_COORD,TRUE_SITE_ADDR,TRUE_SITE_UNIT,TRUE_SITE_CITY,TRUE_SITE_ZIP_CODE,TRUE_OWNER1,TRUE_OWNER2,TRUE_OWNER3,CONDO_FLAG,PARENT_FOLIO,BEDROOM_COUNT,BATHROOM_COUNT,HALF_BATHROOM_COUNT,FLOOR_COUNT,UNIT_COUNT,BUILDING_ACTUAL_AREA,BUILDING_HEATED_AREA,LOT_SIZE,YEAR_BUILT,ASSESSMENT_YEAR_CUR,ASSESSED_VAL_CUR",
        "returnGeometry": "false",
        "outSR": "",
        "f": "json"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch data from the API for Parcel:", parcel_value)
        return None

# Main function to fetch data from API for each Parcel value in the DataFrame
def main():
    parcel_value = input("Enter the Parcel value: ")
    api_results = []  # Initialize an empty list to store API results
    api_data = fetch_data_for_parcel(parcel_value)
    if api_data:
        # Extract features from API response
        features = api_data.get("features", [])
        if features:
            # Extract attributes from the first feature (assuming there's only one feature)
            attributes = features[0].get("attributes", {})
            api_results.append(attributes)

    # Convert the list of API results into a DataFrame
    api_results_df = pd.DataFrame(api_results)

    pd.set_option('display.max_columns', None)
    # Print the DataFrame with API results
    print("API Results:")
    print(api_results_df)

if __name__ == "__main__":
    main()

