# 🔍 Crime Data Analysis & Geospatial Hotspot Detection

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Libraries](https://img.shields.io/badge/Libraries-Pandas%20%7C%20Folium%20%7C%20ScikitLearn-green)

## 🎯 Project Objective
This project analyzes crime data from **[INSERT CITY NAME, e.g., Chicago]** to identify temporal patterns and geospatial hotspots. By applying **K-Means Clustering** and density mapping, we aim to provide actionable insights for resource allocation and public safety awareness.

**Key Questions Answered:**
1.  **When** does crime happen? (Time-series analysis)
2.  **Where** are the high-density "Red Zones"? (Geospatial analysis)
3.  Can we utilize **Unsupervised Learning** to segment the city into distinct danger zones automatically?

---

## 📂 Project Structure
This repository is organized as follows:

```text
├── data/                  # Raw and Processed CSVs (GitIgnored)
├── notebooks/             # Jupyter Notebooks for analysis
│   ├── 01_Data_Cleaning.ipynb    # Preprocessing & Feature Engineering
│   ├── 02_EDA_Temporal.ipynb     # Time-series & Distribution analysis
│   ├── 03_Geospatial_Map.ipynb   # Folium Maps & Heatmaps
│   └── 04_Clustering_Model.ipynb # K-Means Clustering implementation
├── images/                # Screenshots of plots and maps
├── README.md              # Project documentation
└── requirements.txt       # Dependencies
⚙️ Setup & InstallationSince the data files are too large for GitHub, you must download the dataset locally.
1. Clone the Repository
```
git clone [https://github.com/suso-van/crime-data-hotspot-analysis.git](https://github.com/suso-van/crime-data-hotspot-analysis.git)
cd crime-data-hotspot-analysis
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Download the Data...
Go to the Chicago Data Portal.
Filter for Year 2025 and Export as CSV.
Rename the file to raw_crime_data.csv.
Move it into the data/ folder in this project.

📊 Methodology
1.Data Cleaning & Feature Engineering
  Handling Nulls:Removed rows with missing Latitude/Longitude as geospatial precision is critical.
  Time Features: Extracted Hour, Day_of_Week, Month from the raw timestamp.
  Filtering: Focused specifically on 2025 data to ensure relevance.
2. Exploratory Data Analysis (EDA)
  Temporal Trends:Analyzed crime frequency by hour of the day.
  Distribution: Identified the top 10 most common crimes (e.g., Theft, Battery).
3. Machine Learning: K-Means Clustering
   Algorithm: K-Means Clustering (Unsupervised Learning).
   Feature Selection: Latitude and Longitude.
   Optimization: Used the Elbow Method to determine the optimal number of clusters ($k=5$).
   Result: The algorithm successfully segmented the city into 5 distinct zones based on crime density.
4. Geospatial Analysis
   Technique: Used Folium to generate interactive HTML maps.
   Visuals: Implemented color-coded markers based on Cluster ID and Heatmap layers to show density.
💡 Key Findings
1. The "Weekend Night" SpikeInsight: Crime frequency peaks significantly on Friday and Saturday nights between 8 PM and 2 AM.

2. Distinct Crime ZonesInsight: The K-Means algorithm identified 5 distinct geographical clusters.Cluster 0 (Downtown): Highest density of "Theft" and property crimes.Cluster 2 (West Side): Higher concentration of violent incidents compared to other clusters.

3. Interactive Map
   (See ``` images/ ```folder for full screenshots)
   
   🚀 How to Run the Analysis
    Once the data is in the data/ folder, run the notebooks in this order:
   
   ```
    01_Data_Cleaning.ipynb (Prepares the data)
    02_EDA_Temporal.ipynb (Generates charts)
    03_Clustering_Model.ipynb (Runs the ML model)
    03_Geospatial_Map.ipynb (Creates the map.html file)
    ```