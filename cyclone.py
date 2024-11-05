import pandas as pd
import matplotlib.pyplot as plt
<<<<<<< HEAD
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point
=======
import seaborn as sns # type: ignore
>>>>>>> c22b0d6d1f29a2f1d4690aa18ac28ea829163e1b


# Load the data files
def load_data():
    annual_data = pd.read_csv("cyclone_dataset/annualFrequency-1891-2021.csv")
    seasonal_cd_monsoon = pd.read_csv(
        "cyclone_dataset/seasonalFrequency_cd_Monsoon1891-2021.csv"
    )
    seasonal_cd_post = pd.read_csv(
        "cyclone_dataset/seasonalFrequency_cd_Post-Monsoon1891-2021.csv"
    )
    seasonal_cd_pre = pd.read_csv(
        "cyclone_dataset/seasonalFrequency_cd_Pre-Monsoon1891-2021.csv"
    )
    seasonal_cd_winter = pd.read_csv(
        "cyclone_dataset/seasonalFrequency_cd_Winter-1891-2021.csv"
    )
    seasonal_sc_monsoon = pd.read_csv(
        "cyclone_dataset/seasonalFrequency_sc_Monsoon1891-2021.csv"
    )
    seasonal_sc_post = pd.read_csv(
        "cyclone_dataset/seasonalFrequency_sc_Post-Monsoon1891-2021.csv"
    )
    seasonal_sc_pre = pd.read_csv(
        "cyclone_dataset/seasonalFrequency_sc_Pre-Monsoon1891-2021.csv"
    )
    return (
        annual_data,
        seasonal_cd_monsoon,
        seasonal_cd_post,
        seasonal_cd_pre,
        seasonal_cd_winter,
        seasonal_sc_monsoon,
        seasonal_sc_post,
        seasonal_sc_pre,
    )


# Plot 1: Annual vs Monsoon Frequency
def plot_annual_vs_monsoon(annual_data, seasonal_cd_monsoon):
    plt.figure(figsize=(12, 6))
    plt.plot(
        annual_data["Year"],
        annual_data["Cyclonic Disturbances - TOTAL"],
        label="Annual Cyclonic Disturbances",
        color="blue",
    )
    plt.plot(
        seasonal_cd_monsoon["Year"],
        seasonal_cd_monsoon["June - September: TOTAL"],
        label="Monsoon Cyclonic Disturbances",
        color="green",
    )
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.title("Annual Cyclonic Disturbances vs. Monsoon Season")
    plt.legend()
    plt.grid(True)
    plt.show()


# Plot 2: Annual vs Seasonal Frequency (Stacked Area Plot)
def plot_annual_vs_seasonal(
    annual_data,
    seasonal_cd_winter,
    seasonal_cd_pre,
    seasonal_cd_monsoon,
    seasonal_cd_post,
):
    seasonal_data = pd.DataFrame(
        {
            "Year": annual_data["Year"],
            "Winter": seasonal_cd_winter["January-February: TOTAL"],
            "Pre-Monsoon": seasonal_cd_pre["March-May: TOTAL"],
            "Monsoon": seasonal_cd_monsoon["June - September: TOTAL"],
            "Post-Monsoon": seasonal_cd_post["October - December: TOTAL"],
        }
    ).fillna(0)

    plt.figure(figsize=(12, 6))
    plt.stackplot(
        seasonal_data["Year"],
        seasonal_data["Winter"],
        seasonal_data["Pre-Monsoon"],
        seasonal_data["Monsoon"],
        seasonal_data["Post-Monsoon"],
        labels=["Winter", "Pre-Monsoon", "Monsoon", "Post-Monsoon"],
        colors=["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c"],
    )
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.title("Seasonal Cyclonic Disturbances Distribution by Year")
    plt.legend(loc="upper left")
    plt.show()


# Plot 3: Seasonal Cyclonic Disturbances by Region (Bar Plot)
def plot_seasonal_disturbances_by_region_total(
    seasonal_cd_pre, seasonal_cd_monsoon, seasonal_cd_post
):
    # Sum the total disturbances across all years for each season and region
    pre_monsoon_data = (
        seasonal_cd_pre[["March: BOB", "March: AS", "March: LAND"]].sum().values
    )
    monsoon_data = (
        seasonal_cd_monsoon[["June: BOB", "June: AS", "June: LAND"]].sum().values
    )
    post_monsoon_data = (
        seasonal_cd_post[["October: BOB", "October: AS", "October: LAND"]].sum().values
    )

    # Create a DataFrame with the total summed data
    season_data_total = {
        "Region": ["Bay of Bengal", "Arabian Sea", "LAND"],
        "Pre-Monsoon": pre_monsoon_data,
        "Monsoon": monsoon_data,
        "Post-Monsoon": post_monsoon_data,
    }
    season_df = pd.DataFrame(season_data_total).set_index("Region")

    # Plot the DataFrame
    season_df.plot(kind="bar", figsize=(10, 6), color=["#ff7f00", "#e31a1c", "#6a3d9a"])
    plt.ylabel("Total Frequency")
    plt.title("Total Seasonal Cyclonic Disturbances by Region (1891 - 2021)")
    plt.xticks(rotation=0)
    plt.legend(title="Season")
    plt.show()


# Plot 4: Monthly Heatmap of Cyclonic Activity
def plot_monthly_heatmap(seasonal_cd_monsoon):
    # Define the available months based on the columns you listed
    months = ["June", "July", "August", "September"]
    month_columns = [f"{month}: TOTAL" for month in months]

    # Prepare heatmap data
    heatmap_data = pd.DataFrame()

    for month in month_columns:
        heatmap_data[month.split(":")[0]] = seasonal_cd_monsoon[
            seasonal_cd_monsoon["Year"] >= 2000
        ][month]

    # Set index to the Year column for the heatmap
    heatmap_data.set_index(
        seasonal_cd_monsoon["Year"][seasonal_cd_monsoon["Year"] >= 2000], inplace=True
    )

    # Plot heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(
        heatmap_data.T, cmap="YlGnBu", cbar_kws={"label": "Frequency"}, annot=True
    )
    plt.xlabel("Year")
    plt.title("Monthly Cyclonic Activity Heatmap (June - September)")
    plt.show()


# Plot 5: Monthly Heatmap of Cyclonic Activity on Map
def plot_monthly_overlay_on_map(seasonal_cd_monsoon):
    # Load and filter the India shapefile
    india_map = gpd.read_file("shapefile/ne_110m_admin_0_countries.shp")
    india_map = india_map[india_map["ADMIN"] == "India"]

    # Prepare heatmap data (averaged by month for simplicity)
    months = ["June", "July", "August", "September"]
    month_columns = [f"{month}: TOTAL" for month in months]

    # Average monthly data over the years starting from 2000
    heatmap_data = {}
    for month in months:
        heatmap_data[month] = seasonal_cd_monsoon[seasonal_cd_monsoon["Year"] >= 2000][
            f"{month}: TOTAL"
        ].mean()

    # Map month color intensity based on cyclonic activity levels
    colors = {
        "June": "Red",
        "July": "Orange",
        "August": "Yellow",
        "September": "Purple",
    }

    # Plot the map and add month overlays
    fig, ax = plt.subplots(figsize=(10, 10))
    india_map.plot(ax=ax, color="white", edgecolor="black")
    ax.set_title("Monthly Cyclonic Activity Overlay on India Map (2000 onward)")

    for i, month in enumerate(months):
        alpha_value = heatmap_data[month] / max(
            heatmap_data.values()
        )  # Normalize for alpha intensity
        india_map.plot(
            ax=ax,
            color=colors[month],
            alpha=alpha_value * 0.6,
            edgecolor="none",
            legend=True,
        )

    # Add a custom legend
    legend_labels = [
        f"{month}: {round(heatmap_data[month], 1)} avg" for month in months
    ]
    handles = [
        plt.Line2D(
            [0], [0], color=plt.cm.get_cmap(colors[month])(0.6), lw=4, label=label
        )
        for month, label in zip(months, legend_labels)
    ]
    ax.legend(handles=handles, loc="upper left", title="Average Cyclonic Activity")

    plt.show()


# Plot 6: Cyclonic Disturbances vs Severe Cyclones (Monsoon Season)
def plot_disturbances_vs_severe_monsoon(seasonal_cd_monsoon, seasonal_sc_monsoon):
    plt.figure(figsize=(12, 6))
    plt.plot(
        seasonal_cd_monsoon["Year"],
        seasonal_cd_monsoon["June - September: TOTAL"],
        label="Cyclonic Disturbances - Monsoon",
        color="purple",
    )
    plt.plot(
        seasonal_sc_monsoon["Year"],
        seasonal_sc_monsoon["June- September: TOTAL"],
        label="Severe Cyclones - Monsoon",
        color="red",
    )
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.title("Cyclonic Disturbances vs. Severe Cyclones (Monsoon)")
    plt.legend()
    plt.grid(True)
    plt.show()


# Plot 3: Seasonal Cyclonic Disturbances by Region (Heatmap on India Map)
# Plot 3: Seasonal Cyclonic Disturbances by Region (Heatmap on World Map)
def plot_seasonal_disturbances_by_region_map_world(
    seasonal_cd_pre, seasonal_cd_monsoon, seasonal_cd_post
):
    # Sum the total disturbances across all years for each season and region
    pre_monsoon_data = (
        seasonal_cd_pre[["March: BOB", "March: AS", "March: LAND"]].sum().values
    )
    monsoon_data = (
        seasonal_cd_monsoon[["June: BOB", "June: AS", "June: LAND"]].sum().values
    )
    post_monsoon_data = (
        seasonal_cd_post[["October: BOB", "October: AS", "October: LAND"]].sum().values
    )

    # Prepare heatmap data by region
    heatmap_data = {
        "Bay of Bengal": sum(
            [pre_monsoon_data[0], monsoon_data[0], post_monsoon_data[0]]
        ),
        "Arabian Sea": sum(
            [pre_monsoon_data[1], monsoon_data[1], post_monsoon_data[1]]
        ),
        "LAND": sum([pre_monsoon_data[2], monsoon_data[2], post_monsoon_data[2]]),
    }

    # Load the world shapefile
    world_map = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

    # Plot the world map with a focus on the Indian Ocean region
    fig, ax = plt.subplots(figsize=(12, 10))
    world_map.plot(ax=ax, color="lightgray", edgecolor="black")
    ax.set_xlim(50, 100)  # Longitudes around India and the adjacent seas
    ax.set_ylim(-10, 30)  # Latitudes around the Indian subcontinent

    # Define polygons for Bay of Bengal, Arabian Sea, and central India (LAND)
    bay_of_bengal_poly = gpd.GeoSeries(
        [Point(90, 15).buffer(5)]
    )  # Approximate Bay of Bengal area
    arabian_sea_poly = gpd.GeoSeries(
        [Point(65, 15).buffer(5)]
    )  # Approximate Arabian Sea area
    land_poly = gpd.GeoSeries(
        [Point(78, 23).buffer(5)]
    )  # Approximate LAND area (central India)

    # Normalize the intensity for each region to set the transparency
    max_intensity = max(heatmap_data.values())
    colors = {"Bay of Bengal": "blue", "Arabian Sea": "green", "LAND": "orange"}
    alpha_values = {
        region: heatmap_data[region] / max_intensity for region in heatmap_data
    }

    # Plot each region with its corresponding color and alpha transparency
    bay_of_bengal_poly.plot(
        ax=ax, color=colors["Bay of Bengal"], alpha=alpha_values["Bay of Bengal"]
    )
    arabian_sea_poly.plot(
        ax=ax, color=colors["Arabian Sea"], alpha=alpha_values["Arabian Sea"]
    )
    land_poly.plot(ax=ax, color=colors["LAND"], alpha=alpha_values["LAND"])

    # Add a legend to represent intensity by region
    legend_labels = [
        f"{region}: {round(heatmap_data[region], 1)} total" for region in heatmap_data
    ]
    handles = [
        plt.Line2D(
            [0],
            [0],
            color=colors[region],
            lw=6,
            alpha=alpha_values[region],
            label=label,
        )
        for region, label in zip(heatmap_data.keys(), legend_labels)
    ]
    ax.legend(
        handles=handles, loc="upper left", title="Cyclonic Disturbances by Region"
    )

    plt.title(
        "Total Seasonal Cyclonic Disturbances by Region on World Map (Bay of Bengal, Arabian Sea, LAND)"
    )
    plt.show()


# Menu logic
def display_menu():
    print("\nCyclone Dataset Visualization")
    print("1. Plot Annual vs Monsoon Cyclonic Disturbances")
    print("2. Plot Annual vs Seasonal Cyclonic Disturbances")
    print("3. Plot Seasonal Cyclonic Disturbances by Region")
    print("4. Plot Monthly Heatmap of Cyclonic Activity")
    print("5. Plot Monthly Heatmap of Cyclonic Activity on Map")
    print("6. Plot Cyclonic Disturbances vs Severe Cyclones (Monsoon)")
    print("7. Plot Seasonal Cyclonic Disturbances by Region on Map")
    print("0. Exit")


# Main function to call each plot function
def main():
    # Load the data
    (
        annual_data,
        seasonal_cd_monsoon,
        seasonal_cd_post,
        seasonal_cd_pre,
        seasonal_cd_winter,
        seasonal_sc_monsoon,
        seasonal_sc_post,
        seasonal_sc_pre,
    ) = load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (0-5): ")

        if choice == "1":
            plot_annual_vs_monsoon(annual_data, seasonal_cd_monsoon)
        elif choice == "2":
            plot_annual_vs_seasonal(
                annual_data,
                seasonal_cd_winter,
                seasonal_cd_pre,
                seasonal_cd_monsoon,
                seasonal_cd_post,
            )
        elif choice == "3":
            plot_seasonal_disturbances_by_region_total(
                seasonal_cd_pre, seasonal_cd_monsoon, seasonal_cd_post
            )
        elif choice == "4":
            plot_monthly_heatmap(seasonal_cd_monsoon)
        elif choice == "5":
            plot_monthly_overlay_on_map(seasonal_cd_monsoon)
        elif choice == "6":
            plot_disturbances_vs_severe_monsoon(
                seasonal_cd_monsoon, seasonal_sc_monsoon
            )
        elif choice == "7":
            plot_seasonal_disturbances_by_region_map_world(
                seasonal_cd_pre, seasonal_cd_monsoon, seasonal_cd_post
            )
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


# Call the main function
if __name__ == "__main__":
    main()
