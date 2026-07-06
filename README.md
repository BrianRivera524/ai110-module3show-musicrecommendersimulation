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

PS C:\Users\river\Downloads\CodePath_TF_Tasks\ai110-module3show-musicrecommendersimulation> python -m pytest               
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\river\Downloads\CodePath_TF_Tasks\ai110-module3show-musicrecommendersimulation
plugins: anyio-4.13.0
collected 2 items                                                                                                                                                      

tests\test_recommender.py ..                                                                                                                                     [100%]

=========================== 2 passed in 0.16s =========================

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a' block so a reader can see what it produces:

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

## Stress Test Recommendation Output

### Happy Pop Listener

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

### Chill Lofi Listener

'''
Loaded songs: 20

User Profile: Chill Lofi Listener
---------------------------------
Favorite genre: lofi
Favorite mood: chill
Target energy: 0.35
Target tempo: 75 BPM
Target valence: 0.6
Target danceability: 0.58
Target acousticness: 0.85

Top Recommendations
-------------------
1. Library Rain by Paper Lanterns
   Score: 9.46
   Genre: lofi | Mood: chill
   Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+2.00), tempo similarity (+0.97), valence similarity (+1.00), danceability similarity (+1.00), acousticness similarity (+0.99)

2. Midnight Coding by LoRoom
   Score: 9.11
   Genre: lofi | Mood: chill
   Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+1.86), tempo similarity (+0.97), valence similarity (+0.96), danceability similarity (+0.96), acousticness similarity (+0.86)

3. Focus Flow by LoRoom
   Score: 7.75
   Genre: lofi | Mood: focused
   Reasons: genre match (+2.0), energy similarity (+1.90), tempo similarity (+0.95), valence similarity (+0.99), danceability similarity (+0.98), acousticness similarity (+0.93)

4. Spacewalk Thoughts by Orbit Bloom
   Score: 6.92
   Genre: ambient | Mood: chill
   Reasons: mood match (+1.5), energy similarity (+1.86), tempo similarity (+0.85), valence similarity (+0.95), danceability similarity (+0.83), acousticness similarity (+0.93)

5. Coffee Shop Stories by Slow Stereo
   Score: 5.62
   Genre: jazz | Mood: relaxed
   Reasons: energy similarity (+1.96), tempo similarity (+0.85), valence similarity (+0.89), danceability similarity (+0.96), acousticness similarity (+0.96)
'''

### Deep Intense Rock Listener

'''
Loaded songs: 20

User Profile: Deep Intense Rock Listener
----------------------------------------
Favorite genre: rock
Favorite mood: intense
Target energy: 0.9
Target tempo: 140 BPM
Target valence: 0.5
Target danceability: 0.65
Target acousticness: 0.1

Top Recommendations
-------------------
1. Storm Runner by Voltline
   Score: 9.33
   Genre: rock | Mood: intense
   Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+1.98), tempo similarity (+0.88), valence similarity (+0.98), danceability similarity (+0.99), acousticness similarity (+1.00)

2. Beggin' by Måneskin
   Score: 9.13
   Genre: rock | Mood: intense
   Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+1.92), tempo similarity (+0.94), valence similarity (+0.88), danceability similarity (+0.91), acousticness similarity (+0.98)

3. Gym Hero by Max Pulse
   Score: 6.81
   Genre: pop | Mood: intense
   Reasons: mood match (+1.5), energy similarity (+1.94), tempo similarity (+0.92), valence similarity (+0.73), danceability similarity (+0.77), acousticness similarity (+0.95)

4. Titanium by David Guetta ft. Sia
   Score: 5.57
   Genre: edm | Mood: empowering
   Reasons: energy similarity (+2.00), tempo similarity (+0.86), valence similarity (+0.82), danceability similarity (+0.95), acousticness similarity (+0.94)

5. Helena by My Chemical Romance
   Score: 5.50
   Genre: emo | Mood: melancholic
   Reasons: energy similarity (+1.98), tempo similarity (+0.85), valence similarity (+0.88), danceability similarity (+0.84), acousticness similarity (+0.95)
'''

### Edge Case: Sad High-Energy Listener

'''
Loaded songs: 20

User Profile: Edge Case: Sad High-Energy Listener
-------------------------------------------------
Favorite genre: alternative rock
Favorite mood: melancholic
Target energy: 0.9
Target tempo: 130 BPM
Target valence: 0.25
Target danceability: 0.45
Target acousticness: 0.2

Top Recommendations
-------------------
1. My Immortal by Evanescence
   Score: 7.19
   Genre: alternative rock | Mood: melancholic
   Reasons: genre match (+2.0), mood match (+1.5), energy similarity (+0.84), tempo similarity (+0.50), valence similarity (+0.97), danceability similarity (+0.86), acousticness similarity (+0.52)

2. Helena by My Chemical Romance
   Score: 7.11
   Genre: emo | Mood: melancholic
   Reasons: mood match (+1.5), energy similarity (+1.98), tempo similarity (+0.95), valence similarity (+0.87), danceability similarity (+0.96), acousticness similarity (+0.85)

3. Storm Runner by Voltline
   Score: 5.22
   Genre: rock | Mood: intense
   Reasons: energy similarity (+1.98), tempo similarity (+0.78), valence similarity (+0.77), danceability similarity (+0.79), acousticness similarity (+0.90)

4. Titanium by David Guetta ft. Sia
   Score: 5.22
   Genre: edm | Mood: empowering
   Reasons: energy similarity (+2.00), tempo similarity (+0.96), valence similarity (+0.57), danceability similarity (+0.85), acousticness similarity (+0.84)

5. Beggin' by Måneskin
   Score: 5.14
   Genre: rock | Mood: intense
   Reasons: energy similarity (+1.92), tempo similarity (+0.96), valence similarity (+0.63), danceability similarity (+0.71), acousticness similarity (+0.92)
'''
## Accuracy and Surprises

The recommendations mostly matched my expectations. For the Happy Pop 
Listener profile, Sunrise City ranked highly because it matched both 
the favorite genre and favorite mood while also being close to the 
target numerical values. For the Chill Lofi Listener profile, I 
expected songs like Library Rain, Midnight Coding, and Focus Flow 
to rank high because they are low-energy, chill, and acoustic. 
For the Deep Intense Rock Listener profile, I expected songs like 
Storm Runner, Beggin', and Helena to perform well because they 
have high energy and intense or rock-related features.

One interesting result was that songs from different genres could 
still rank well if their numerical features matched the user 
profile closely. This makes the recommender feel more flexible, 
but it also shows a possible weakness: a song can appear in the 
top results even if the genre or mood does not fully match the 
user’s intent. This means the weights matter a lot, especially 
the balance between genre, mood, and numerical similarity.

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

Small Data Experiment

For my small data experiment, I changed the scoring weights to test how 
sensitive the recommender was to energy. In the original version, a genre 
match was worth +2.0 points and energy similarity was worth up to +2.0 
points. For the experiment, I reduced the genre match to +1.0 point and 
increased energy similarity to up to +4.0 points.

After running the recommender again, the rankings changed. The system 
started giving more importance to songs that matched the target energy, 
even if they did not match the exact genre. For example, in the Happy 
Pop Listener profile, Rooftop Lights moved above some exact pop songs 
because it matched the happy mood and had very close energy, tempo, 
valence, danceability, and acousticness values. In the Deep Intense 
Rock Listener profile, Titanium and Helena ranked in the top five even 
though they were not exact rock/intense matches, because their energy 
levels were very close to the user’s target.

This made the recommendations different, but not always more accurate. 
The change helped the system find songs with a similar intensity level, 
but it also made some genre and mood mismatches rank higher. This showed 
me that recommendation systems are very sensitive to scoring weights. 
A small change in the algorithm can noticeably change which songs appear at the top.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

One limitation of this recommender is that it depends heavily on the weights 
I manually chose. When genre was weighted more strongly, the system favored 
exact genre matches and could create a filter bubble by recommending mostly 
songs from the same genre. When I increased the energy weight, the system 
became more flexible, but it also started ranking songs from unrelated 
genres higher if their energy level was close to the user’s target.

Another limitation is that the dataset is small, with only 20 songs. Some 
genres only have one or two examples, so the recommender does not have 
enough variety to represent every type of listener fairly. The system also 
treats genres as exact matches, so pop and indie pop are considered different 
even though they are related. Overall, this recommender is useful as a simple 
simulation, but it does not understand music deeply or learn from user behavior 
like skips, likes, or replays.

---

## Reflection

Read and complete 'model_card.md':

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

This project helped me understand how recommendation systems turn data into 
predictions. Instead of “knowing” what a user likes, the recommender compares 
a user profile to song features such as genre, mood, energy, tempo, valence, 
danceability, and acousticness. Each song receives a score based on how closely 
it matches the user’s preferences, and then the system ranks the songs from 
highest to lowest score. This showed me that even a simple scoring formula 
can feel like a recommendation because it turns raw data into a decision 
about what songs are most relevant.

I also learned that bias or unfairness can show up through the dataset and 
the scoring weights. If the dataset has too many songs from one genre, the 
recommender may over-represent that genre. If a feature like genre or energy 
is weighted too strongly, the system may ignore other songs that could still 
fit the user’s taste. For example, increasing the energy weight made the system 
better at finding songs with a similar intensity, but it also caused some 
genre and mood mismatches to rank higher. This showed me that recommendation 
systems are sensitive to design choices, and small changes in the algorithm 
can affect what users are exposed to.

