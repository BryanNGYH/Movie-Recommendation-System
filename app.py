import streamlit as st
import pickle
import requests
import api_key

movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))

movies_list = movies['title'].values

st.header("Movie Recommendation System")
selectvalue = st.selectbox("Select movie from dropdown",movies_list)

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,api_key.api_key)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']   
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    recommendation = []
    recommendation_year = []
    recommendation_poster = []

    for i, (movie_index, similarity_score) in enumerate(distances[1:11]):
        id = movies.iloc[movie_index].id
        title = movies.iloc[movie_index].title
        year = movies.iloc[movie_index].year
        recommendation.append(title)
        recommendation_year.append(year)
        recommendation_poster.append(fetch_poster(id))
        # print(title,year)

    return recommendation, recommendation_year, recommendation_poster

if st.button("Show recommendation"):
    movie_name, movie_released_year,movie_poster = recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.text(movie_released_year[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.text(movie_released_year[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.text(movie_released_year[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.text(movie_released_year[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.text(movie_released_year[4])
        st.image(movie_poster[4])
 