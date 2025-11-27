import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os

# -----------------------------
# Google Drive se similarity.pkl Download
# -----------------------------
DRIVE_URL = "https://drive.google.com/uc?export=download&id=1zSHcNZNIEusxa4mGE1ngi6ADzjOzCqGV"
SIMILARITY_FILE = "similarity.pkl"

def download_similarity():
    if not os.path.exists(SIMILARITY_FILE):
        st.info("Downloading model file... Please wait ⏳")
        gdown.download(DRIVE_URL, SIMILARITY_FILE, quiet=False)
        st.success("Download Completed ✔")

download_similarity()

# -----------------------------
# Load Movie Data
# -----------------------------
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# -----------------------------
# Fetch Poster
# -----------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=fadfa094648b588a087b9c20b3f192e7&language=en-US"
    data = requests.get(url).json()

    poster_path = data.get("poster_path")
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/500x750?text=No+Image"

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# -----------------------------
# Streamlit UI
# -----------------------------
st.title(" Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])