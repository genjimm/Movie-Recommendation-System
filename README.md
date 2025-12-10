# 🎬 Movie Recommendation System  
### *A Big Data Pipeline for Distributed Movie Recommendation using PySpark*

This repository contains an end-to-end **Big Data movie recommendation project** implemented in a single PySpark notebook.  
The project focuses on **large-scale data processing**, **distributed computation**, **multi-source data integration**, and the construction of a scalable recommendation pipeline.

---

## Project Structure

```
Movie-Recommendation-System
├── Bigdata.ipynb               # Main notebook: data cleaning, integration, EDA, modeling, evaluation
├── README.md                   # Project documentation
│
├── data_raw/                   # Original raw datasets (MovieLens + TMDB)
│   ├── ratings_small.csv
│   ├── movies_metadata.csv
│   ├── keywords.csv
│   ├── links.csv
│   └── credits.zip
│
├── data_clean/                 # Cleaned & processed data + saved models
│
└── .gitattributes              # Git LFS settings
```

> All work is included in one well-organized notebook for easy reproducibility and final project submission.

The notebook is structured into eight major stages:

1. **Setup and configuration** – Initialize PySpark and environment paths.
2. **Data loading and analysis** – Load MovieLens and TMDB datasets and inspect data quality.
3. **Data cleaning** – Normalize metadata, parse JSON fields, resolve missing values.
4. **Feature engineering** – Build TF-IDF movie profiles and prepare user-item matrices.
5. **Exploratory Data Analysis** – Analyze rating patterns, genres, user activity, and long-tail effects.
6. **Data visualization** – Produce histograms, correlation heatmaps, and genre distributions.
7. **Models** – Implement content-based similarity and train ALS collaborative filtering.
8. **Streamlit Web Application** – Provide an interactive interface for recommendations.

---

## Big Data Technologies Used

| Component | Tools |
|----------|-------|
| Distributed ETL | PySpark DataFrames, Window functions, `explode()` |
| Storage | Parquet (columnar), pickle |
| Feature Engineering | Spark transformations, UDFs |
| Modeling | Spark MLlib ALS, TF-IDF |
| Visualization | Matplotlib |
| Serving | Streamlit (optional) |
---

## System Architecture

```mermaid
flowchart LR
    A[Raw Movie & Rating Data] --> B[Data Cleaning & Preprocessing]
    B --> C1[Feature Engineering - Combined Text]
    B --> C2[User-Item Rating Matrix]

    C1 --> D1[Content-Based Model - TF-IDF + Cosine Similarity]
    C2 --> D2[Collaborative Filtering Model - ALS]

    D1 --> E[Recommendation Engine]
    D2 --> E

    E --> F[Streamlit Web App]

```

## How to Run the Notebook

### 1. Clone the repository

```
git clone https://github.com/yourusername/Movie-Recommender-System.git
cd Movie-Recommender-System
```

### 2. Open the notebook

```
jupyter notebook movie_recommender.ipynb
```

Or open directly in Google Colab.
