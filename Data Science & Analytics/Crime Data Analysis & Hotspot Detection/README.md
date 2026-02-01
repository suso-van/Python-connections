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
