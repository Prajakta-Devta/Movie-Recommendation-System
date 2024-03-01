import streamlit as st
import pickle
import pandas as pd
import requests
import time

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=b1cdac6ca05d97ac0cdecbead969c610&language=en-US".format(movie_id)
    response=requests.get(url)
    data=response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
    

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names=[]
    recommended_movie_poster=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie_names,recommended_movie_poster



st.set_page_config(page_title="Movie Recommendation")
movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommender System")
selected_movie_name= st.selectbox('How would you like to be contacted?',movies['title'].values)

if st.button('Show Recommendation',type="primary"):
    with st.spinner('Wait !!Recommending You!!'):
        time.sleep(3)
    st.success('Here You Go!')
    names,posters=recommend(selected_movie_name)
    col1, col2, col3 ,col4,col5= st.columns(5)

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

