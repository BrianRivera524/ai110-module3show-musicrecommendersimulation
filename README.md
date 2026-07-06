# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each 'Song' use in your system
  - For example: genre, mood, energy, tempo
- What information does your 'UserProfile' store
- How does your 'Recommender' compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

## How The System Works

This project simulates a simple music recommendation system. 
Real platforms like Spotify or YouTube use many types of data, 
such as likes, skips, playlists, listening history, and song 
features, to predict what users may enjoy next. My version 
is smaller and focuses on content-based filtering, which means 
it recommends songs by comparing the features of each song 
to a user’s taste profile.

Each 'Song' in the system uses features from 'songs.csv', 
including 'title', 'artist', 'genre', 'mood', 'energy', 
'tempo_bpm', 'valence', 'danceability', and 'acousticness'. 
These features help describe the overall “vibe” of a song. 
For example, 'genre' and 'mood' describe the category and 
feeling of the song, while 'energy', 'valence', 'danceability', 
and 'acousticness' help measure how intense, positive, 
rhythmic, or acoustic the song feels.

The 'UserProfile' stores the listener’s preferences, such as 
their favorite genre, favorite mood, target energy, target 
tempo, target valence, target danceability, and target 
acousticness. These values act like the user’s ideal song profile.

The 'Recommender' scores each song by comparing the song’s 
features to the user’s preferences. A song gets extra points 
if its genre or mood matches the user’s favorites. For 
numerical features like energy or danceability, the 
system gives more points when the song’s value is closer 
to the user’s target value. This helps the system reward 
similarity instead of simply choosing the highest number.

After every song receives a score, the recommender sorts the 
songs from highest score to lowest score. The songs with the 
highest scores are returned as the top recommendations.

Simple data flow:

User Preferences → Compare Against Each Song → 
Calculate Score → Sort Songs → Return Top Recommendations

Overall, this system prioritizes songs that match the user’s 
preferred genre and mood while also considering how close each 
song is to the user’s preferred musical vibe.


Data Flow Sketch:

User Preferences
→ The user profile stores the listener’s favorite genre, favorite mood, 
and target values for energy, tempo, valence, danceability, and acousticness.

Song Catalog
→ The system loads every song from 'songs.csv' and reads each song’s features.

Scoring Process
→ The recommender loops through each song and compares its features to the 
user’s preferences. It gives points for genre and mood matches, then adds 
similarity points for numerical features.

Ranking Process
→ After every song has a score, the system sorts the songs from highest
score to lowest score.

Final Output
→ The recommender returns the top 'k' songs with their scores and explanations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   '''bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

'''bash
pip install -r requirements.txt
'''

3. Run the app:

'''bash
python -m src.main
'''

### Running Tests

Run the starter tests with:

'''bash
pytest
'''

You can add more tests in 'tests/test_recommender.py'.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

'''
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
'''

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->


'''
Loaded songs: 20

User Profile: Happy Pop Listener
--------------------------------
Favorite genre: pop
Favorite mood: happy
Target energy: 0.8
Target tempo: 120 BPM
Target valence: 0.85
Target danceability: 0.8
Target acousticness: 0.2

Top Recommendations
-------------------
1. Sunrise City by Neon Echo
   Score: 9.40
   Genre: pop | Mood: happy
   Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+1.96), tempo similarity (+0.98), valence similarity (+0.99), danceability similarity (+0.99), acousticness similarity (+0.98)

2. Gym Hero by Max Pulse
   Score: 7.31
   Genre: pop | Mood: intense
   Reasons: genre match (+2.0), energy similarity (+1.74), tempo similarity (+0.88), valence similarity (+0.92), danceability similarity (+0.92), acousticness similarity (+0.85)

3. Chicago by Michael Jackson
   Score: 7.25
   Genre: pop | Mood: moody
   Reasons: genre match (+2.0), energy similarity (+1.84), tempo similarity (+0.80), valence similarity (+0.70), danceability similarity (+0.91), acousticness similarity (+1.00)

4. Rooftop Lights by Indigo Parade
   Score: 7.17
   Genre: indie pop | Mood: happy
   Reasons: mood match (+1.5), energy similarity (+1.92), tempo similarity (+0.96), valence similarity (+0.96), danceability similarity (+0.98), acousticness similarity (+0.85)

5. Vivir Mi Vida by Marc Anthony
   Score: 5.71
   Genre: salsa | Mood: uplifting
   Reasons: energy similarity (+1.92), tempo similarity (+0.85), valence similarity (+0.97), danceability similarity (+0.99), acousticness similarity (+0.98)
'''
-----------------

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete 'model_card.md':

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



