from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle

# Load data
df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

app = Flask(__name__)

# Recommendation function
def recommend(song):
    song_index = df[df['song'] == song].index[0]
    distances = similarity.iloc[song_index].values

    songs_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_songs = []
    for i in songs_list:
        recommended_songs.append(df.iloc[i[0]].song)
    return recommended_songs

@app.route('/')
def index():
    songs = df['song'].values
    return render_template('index.html', songs=songs)

@app.route('/recom', methods=['POST'])
def mysong():
    selected_song = request.form.get('song')
    recommended = recommend(selected_song)
    return render_template('index.html', songs=df['song'].values,
                           selected_song=selected_song,
                           recommended_songs=recommended)

if __name__ == "__main__":
    app.run(debug=True)
