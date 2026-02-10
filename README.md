# CORD-19 Research Analysis Framework
## Overview
The CORD-19 Research Analysis Framework is a Python-based project for cleaning, analyzing, and visualizing research metadata from the COVID-19 Open Research Dataset (CORD-19).
The framework focuses on scalable data exploration and provides an interactive Streamlit dashboard for examining publication trends, journals, and textual patterns in COVID-19 research.

To ensure compatibility with cloud deployment and large datasets, the application is designed to work with sampled data and controlled memory usage.

## Live Demo
### Streamlit Application
https://cord-19-data-analysis-framework-bjqmhuqxqmxyzo6i5xvmwo.streamlit.app/
### Demo Notes
- The application is deployed on Streamlit Community Cloud.

- Due to the large size of the CORD-19 dataset, data is loaded via a Streamlit file uploader.

- The app uses caching and guarded execution to reduce memory usage and prevent rerun hangs.

- Visualizations are generated from sampled data to ensure responsiveness.


## Features
- Data cleaning and preprocessing of CORD-19 metadata

- Exploratory data analysis and statistical summaries

- Interactive visualizations using Matplotlib and Seaborn

- Streamlit web application for interactive exploration

- Optimized data loading to reduce memory usage during analysis
## Visualisation
This project includes a Streamlit dashboard that allows users to:
- Upload a CORD-19 CSV file via the browser

- Filter publications by year

- Explore publication trends over time

- Identify top journals and sources

- Generate word clouds from paper titles

- View a sampled subset of the dataset for quick inspection

The Streamlit application is designed for cloud deployment and uses caching and guarded execution to prevent performance issues when working with large datasets.
### Output
The framework generates:

- Interactive visualizations in the Streamlit web interface

- Static figures (PNG/PDF) for offline analysis and reporting
## Prerequisites
- Python 3.7+
- pandas (data manipulation)
- matplotlib and seaborn (data visualization)
- Streamlit (web application framework)
## Running the Application
pip install -r requirements.txt
streamlit run app.py

Upload the cleaned CORD19 CSV file through the streamlit interface to begin analysis.
## Contributing
1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch to your fork
5. Open a pull request describing your changes

## Notes
This project is intended as an exploratory analysis framework and learning tool.
While it does not modify the original CORD-19 dataset, it demonstrates practical techniques for handling large research metadata, deploying data applications to the cloud, and optimizing performance in Python-based analytical workflows.
