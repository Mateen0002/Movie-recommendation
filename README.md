# Movie Recommendation System – Machine Learning Project

A complete end-to-end Movie Recommendation System that suggests top similar movies based on content similarity. 
The project includes data analysis, visualization, text preprocessing, vectorization, similarity calculation, and deployment using Streamlit.
It also integrates TMDB API to fetch real movie posters for a better user experience.

# Table of Contents
- Project Overview
- Dataset and Features
- Technologies Used
- Key Components
- Workflow Summary
- Recommendation Logic
- Poster Fetching System (TMDB API)
- Streamlit Web Application

# Project Overview

This project aims to build an intelligent movie recommender system that suggests movies related to the one selected by the user.
It follows a systematic workflow involving data exploration, preprocessing, machine learning pipelines, and similarity-based recommendation techniques. 
The system enhances user understanding of movie relationships using NLP and vector similarity.

# Dataset and Features
The dataset contains movie metadata, including:
- Title
- Overview
- Genres
- Keywords
- Cast
- Crew
These features are combined and transformed into a structured format suitable for text processing and similarity analysis.
# Technologies Used
- Python
- Pandas, NumPy
- NLTK (PorterStemmer)
- scikit-learn (similarity computation and preprocessing)
- TMDB API for movie posters
-Streamlit for web deployment

# Key Components
1. Data Analysis
The dataset is thoroughly analyzed to understand:
- Distribution of features
- Missing values
- Unique movie attributes
- Patterns among genres and cast
- This step ensures clarity before moving into model development.

2. Data Visualization
Basic visualizations are created to observe:
- Most frequent genres
- Popular keywords
- Relationship between different movie attributes
- Visualization helps identify which features significantly contribute to similarity.

3. Data Preprocessing
- Several preprocessing steps are applied:
- Cleaning the dataset
- Removing missing or unusable values
- Extracting useful text attributes
- Stemming words using PorterStemmer to reduce them to their root forms
- Combining selected features into a single text representation ("tags")
- This prepares the dataset for language-based machine learning techniques.

4. Machine Learning Pipeline
A pipeline is designed to:
- Transform text into numerical vectors
- Apply tokenization and stemming
- Convert text into vector embeddings
- Compute similarity scores for recommendations
- This structured pipeline ensures reproducibility and clean workflow management.

#  Recommendation Logic
The system uses cosine similarity to measure how closely related two movies are.
- When a user selects a movie:
- The system identifies its index in the processed dataset.
- It retrieves the similarity distance between that movie and all others.
- The top 5 most similar movies (excluding the selected one) are chosen.
- Their titles and posters are displayed to the user.
- This approach ensures fast, accurate, and relevant recommendations.

# Poster Fetching System (TMDB API Integration)

To improve the user interface, each recommended movie displays a poster.
This is achieved using the TMDB (The Movie Database) API, which provides real-time poster URLs.

The API system:
- Sends a request to TMDB servers using the movie ID
- Safely handles errors and fallback images
- Returns high-resolution poster links
- This integration makes the system visually appealing and user-friendly.

# Streamlit Web Application
The complete system is deployed using Streamlit, providing:
- A clean user interface
- A dropdown list of movies
- Real-time movie recommendations
- Posters for each recommended movie
- Users can interact with the system easily without running Python scripts manually.


This Movie Recommendation System combines NLP, machine learning, API integration, and web deployment to deliver a complete and practical project. 
The structured workflow, effective preprocessing, and similarity-based model ensure accurate and relevant recommendations. 
The inclusion of TMDB posters and a Streamlit interface creates a professional and interactive user experience.
