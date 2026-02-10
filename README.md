# CORD-19 Research Analysis Framework
## Overview

The CORD-19 Research Analysis Framework is a Python-based project for cleaning, analyzing, and visualizing research metadata from the COVID-19 Open Research Dataset (CORD-19).

The framework focuses on scalable data exploration and provides an interactive Streamlit dashboard for examining publication trends, journals, sources, and textual patterns in COVID-19 research.

To ensure compatibility with cloud deployment and large datasets, the application uses a compressed Parquet dataset and optimized data-loading strategies.

## Live Demo
### Streamlit Application

🔗 https://cord-19-data-analysis-framework-bjqmhuqxqmxyzo6i5xvmwo.streamlit.app/

## Demo Notes

- The application is deployed on Streamlit Community Cloud.

- The CORD-19 dataset is stored in Parquet format and hosted via GitHub Releases.

- On first run, the app downloads and caches the dataset automatically to avoid large file uploads.

- Caching and guarded execution are used to reduce memory usage and prevent rerun hangs.

- Visualizations are generated from filtered data to maintain responsiveness.

## Features

- Data cleaning and preprocessing of CORD-19 metadata

- Exploratory data analysis and statistical summaries

- Interactive visualizations using Matplotlib and Seaborn

- Streamlit web application for interactive exploration

- Optimized data loading using Parquet for efficient cloud deployment

## Streamlit Dashboard

This project includes a Streamlit dashboard that allows users to:

- Filter publications by year

- Explore publication trends over time

- Identify top journals and data sources

- Generate word clouds from paper titles

- View a subset of the dataset for quick inspection

The dashboard is designed for cloud environments and avoids manual dataset uploads by downloading the dataset.

## Output

The framework generates:

- Interactive visualizations within the Streamlit web interface

- Static figures (PNG/PDF) suitable for offline analysis and reporting

## Prerequisites
- Python 3.7 or higher

- pandas (data manipulation)

- matplotlib and seaborn (data visualization)

- Streamlit (web application framework)

- pyarrow (Parquet support)

All dependencies are listed in requirements.txt

## Running the Application
pip install -r requirements.txt
streamlit run app.py

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository

2. Create a new feature branch

3. Commit your changes 

4. Push the branch to your fork

5. Open a pull request describing your changesContributing

## Notes

This project is intended as an exploratory analysis framework and learning tool.

While it does not modify the original CORD-19 dataset, it demonstrates practical techniques for handling large research metadata, using efficient storage formats, deploying data applications to the cloud, and managing performance constraints in Python-based analytical workflows.
