import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide")

st.markdown("""
    <style>
        }
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF;
        }
        .title {
            color: #ffcc00;
            font-size: 42px;
            text-align: center;
        }
        .movie-text {
            font-size: 24px;
            font-weight: bold;
            color: #ff9933;
            margin-bottom: 5px;
        }
        .stButton>button {
            background-color: #ffcc00;
            border-radius: 10px;
            color: #000000;
        }
        .stButton>button:hover {
            background-color: #ff9933;
            color: white;
        }
        .stSelectbox>div>div>div {
            background-color: #ffcc00;
            color: #000000;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>🎥 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("""
    <h4 style='color:white; text-align:center;'>Explore personalized movie recommendations based on your choice. 
    Just select a movie, and let us suggest some great similar options for you!</h4>
    """, unsafe_allow_html=True)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie_names = st.selectbox(
    '🎬 Select a movie to get recommendations:',
    movies['title'].values, index=0)

if st.button('🚀 Get Recommendations'):
    recommendations = recommend(selected_movie_names)

    st.divider()  
    st.subheader('Top 5 Movie Recommendations 🎬:')
    

    cols = st.columns(5)
    
    for i, (col, name) in enumerate(zip(cols, recommendations)):
        with col:
            st.markdown(f"<p class='movie-text'>🎬{name}</p>", unsafe_allow_html=True)

    st.divider()  

st.markdown("<h6 style='text-align: center; color:white;'>Made by Vibhav Ahuja.</h6>", unsafe_allow_html=True)

# st.title('Movie Recommender System')
# 
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
# 
#     recommended_movies = []
#     for i in movies_list:
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies
# 
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# 
# similarity = pickle.load(open('similarity.pkl', 'rb'))
# 
# selected_movie_names = st.selectbox(
#     'Select a movie:',
#     movies['title'].values)
# 
# if st.button('Recommend'):
#     recommendations = recommend(selected_movie_names)
#     for name in recommendations:
#         st.text(name)
