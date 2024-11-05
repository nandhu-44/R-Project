import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load datasets
def load_data():
    global annual_freq, severe_monsoon, dist_monsoon
    global dist_pre_monsoon, dist_post_monsoon, dist_winter
    global severe_pre_monsoon, severe_post_monsoon, severe_winter

    # Load main datasets
    annual_freq = pd.read_csv('cyclone_dataset/annualFrequency-1891-2021.csv')
    severe_monsoon = pd.read_csv('cyclone_dataset/seasonalFrequency_sc_Monsoon1891-2021.csv')
    dist_monsoon = pd.read_csv('cyclone_dataset/seasonalFrequency_cd_Monsoon1891-2021.csv')
    
    # Load disturbance datasets
    dist_pre_monsoon = pd.read_csv('cyclone_dataset/seasonalFrequency_cd_Pre-Monsoon1891-2021.csv')
    dist_post_monsoon = pd.read_csv('cyclone_dataset/seasonalFrequency_cd_Post-Monsoon1891-2021.csv')
    dist_winter = pd.read_csv('cyclone_dataset/seasonalFrequency_cd_Winter-1891-2021.csv')

    # Load severe cyclone datasets
    severe_pre_monsoon = pd.read_csv('cyclone_dataset/seasonalFrequency_sc_Pre-Monsoon1891-2021.csv')
    severe_post_monsoon = pd.read_csv('cyclone_dataset/seasonalFrequency_sc_Post-Monsoon1891-2021.csv')
    severe_winter = pd.read_csv('cyclone_dataset/seasonalFrequency_sc_Winter-1891-2021.csv')

    # Strip any extra spaces from column names
    severe_winter.columns = severe_winter.columns.str.strip()
# Function to display the menu
def display_menu():
    print("\nChoose an option to display:")
    print("1. Annual Frequency and Severe Monsoon vs. Disturbance Monsoon")
    print("2. Disturbance Frequency for All Seasons")
    print("3. Severe Cyclone Frequency for All Seasons")
    print("4. Pre-Monsoon vs. Post-Monsoon Disturbance Frequency")
    print("5. Heatmap of Annual Cyclone Frequency")
    print("6. Exit")

# Function for visualizations
def plot_annual_and_monsoon():
    # Plotting Annual Cyclonic Disturbance Frequency
    plt.figure(figsize=(10, 5))
    plt.plot(annual_freq['Year'], annual_freq['Cyclonic Disturbances - TOTAL'], label='Cyclonic Disturbances - TOTAL')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('Annual Cyclonic Disturbance Frequency (1891-2021)')
    plt.legend()
    plt.show()

    # Severe Cyclones and Cyclonic Disturbances Comparison for Monsoon
    plt.figure(figsize=(10, 5))
    # Using specific columns for severe cyclones in Bay of Bengal and disturbances
    plt.plot(severe_monsoon['Year'], severe_monsoon['June: BOB'], label='Severe Cyclones - June: BOB', color='red')
    plt.plot(dist_monsoon['Year'], dist_monsoon['June: TOTAL'], label='Disturbance - June TOTAL', color='blue')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('Severe Cyclones vs Disturbance in June (1891-2021)')
    plt.legend()
    plt.show()

def plot_disturbance_all_seasons():
    plt.figure(figsize=(12, 8))
    # Plotting disturbances for different months
    plt.plot(dist_monsoon['Year'], dist_monsoon['June: TOTAL'], label='June Disturbances', color='lightblue')
    plt.plot(dist_monsoon['Year'], dist_monsoon['July: TOTAL'], label='July Disturbances', color='yellow')
    plt.plot(dist_monsoon['Year'], dist_monsoon['August: TOTAL'], label='August Disturbances', color='orange')
    plt.plot(dist_monsoon['Year'], dist_monsoon['September: TOTAL'], label='September Disturbances', color='red')
    plt.plot(dist_post_monsoon['Year'], dist_post_monsoon['October: TOTAL'], label='October Disturbances', color='purple')
    plt.plot(dist_post_monsoon['Year'], dist_post_monsoon['November: TOTAL'], label='November Disturbances', color='pink')
    plt.plot(dist_post_monsoon['Year'], dist_post_monsoon['December: TOTAL'], label='December Disturbances', color='brown')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('Cyclonic Disturbance Frequency from June to December (1891-2021)')
    plt.legend()
    plt.show()

# Function for plotting severe cyclones for all seasons
def plot_severe_all_seasons():
    plt.figure(figsize=(12, 8))
    
    # Plot Severe Monsoon using the correct header from your dataset
    plt.plot(severe_monsoon['Year'], severe_monsoon['October - December: TOTAL'], label='Severe Monsoon', color='red')
    
    # Plot Severe Pre-Monsoon using the correct header
    plt.plot(severe_pre_monsoon['Year'], severe_pre_monsoon['March-May: TOTAL'], label='Severe Pre-Monsoon', color='blue')
    
    # Plot Severe Post-Monsoon using the correct header
    plt.plot(severe_post_monsoon['Year'], severe_post_monsoon['October - December: TOTAL'], label='Severe Post-Monsoon', color='green')
    
    # Plot Severe Winter if the column exists
    if 'December: AS' in severe_winter.columns:
        plt.plot(severe_winter['Year'], severe_winter['December: AS'], label='Severe Winter - December: AS', color='orange')
    else:
        print("Column 'December: AS' not found in the dataset.")

    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('Severe Cyclone Frequency for All Seasons (1891-2021)')
    plt.legend()
    plt.show()


def plot_pre_post_monsoon():
    plt.figure(figsize=(10, 5))
    # Plotting pre-monsoon and post-monsoon disturbance frequencies
    plt.plot(dist_pre_monsoon['Year'], dist_pre_monsoon['March-May: TOTAL'], label='Pre-Monsoon', color='green')
    plt.plot(dist_post_monsoon['Year'], dist_post_monsoon['October - December: TOTAL'], label='Post-Monsoon', color='orange')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('Pre-Monsoon vs Post-Monsoon Disturbance Frequency (1891-2021)')
    plt.legend()
    plt.show()

def plot_heatmap():
    plt.figure(figsize=(12, 6))
    sns.heatmap(annual_freq.pivot_table(index='Year', values='Cyclonic Disturbances - TOTAL'), cmap='viridis', annot=True)
    plt.title('Heatmap of Annual Cyclonic Disturbance Frequency (1891-2021)')
    plt.show()

# Main function
def main():
    load_data()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            plot_annual_and_monsoon()
        elif choice == '2':
            plot_disturbance_all_seasons()
        elif choice == '3':
            plot_severe_all_seasons()
        elif choice == '4':
            plot_pre_post_monsoon()
        elif choice == '5':
            plot_heatmap()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
