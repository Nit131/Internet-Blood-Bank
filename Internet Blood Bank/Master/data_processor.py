import pandas as pd

# Function to read the CSV file and filter the data
def filter_data(city=None, blood_group=None, age=None, gender=None):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('blood_data.csv')

    # Filter by city if provided
    if city:
        df = df[df['City'].str.contains(city, case=False, na=False)]

    # Filter by blood group if provided
    if blood_group:
        df = df[df['Blood Group'] == blood_group]

    # Filter by age if provided
    if age:
        df = df[df['Age'] == int(age)]  # Ensure age is an integer for comparison

    # Return the filtered data as a list of dictionaries
    return df.to_dict(orient='records')
