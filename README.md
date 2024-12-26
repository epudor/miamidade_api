Parcel Data Retrieval from Web API

This script retrieves property data for a specific parcel using a web API.

Requirements:

requests
pandas
json
How to Use:

Run the script:

Bash

python fetch_data_for_parcel.py
Enter the parcel value when prompted.

Output:

The script displays a pandas DataFrame containing the retrieved property details (if available) for the entered parcel value.

Notes:

This script relies on a specific web API and its data structure. Modifications may be needed for different APIs.
Error handling is included for cases where the API request fails.
