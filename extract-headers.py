import os
import pandas as pd


# Function to extract headers from CSV files
def extract_headers(directory):
    headers_info = {}

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            try:
                # Read the CSV file and get the headers
                df = pd.read_csv(file_path)
                headers_info[filename] = df.columns.tolist()
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    return headers_info


# Main function
def main():
    # Specify the directories to look for CSV files
    directories = [
        "cyclone_dataset",
        "temp_dataset",
    ]  # Add any other directories as needed

    all_headers = {}

    for directory in directories:
        print(f"Extracting headers from directory: {directory}")
        headers = extract_headers(directory)
        all_headers[directory] = headers

    # Print the extracted headers
    for dir_name, headers in all_headers.items():
        print(f"\nHeaders in directory '{dir_name}':")
        for file_name, header in headers.items():
            print(f"{file_name}: {header}")


# Run the main function
if __name__ == "__main__":
    main()
