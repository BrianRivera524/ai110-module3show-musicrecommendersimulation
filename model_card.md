# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibeCompass 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

VibeCompass 1.0 is designed to generate simple music recommendations 
based on a user’s preferred genre, mood, and musical “vibe.” It recommends 
songs by comparing a user profile to a small catalog of songs and ranking 
the songs that seem most similar to the user’s preferences.

This recommender assumes that a user’s music taste can be represented 
using features like favorite genre, favorite mood, target energy, tempo, 
valence, danceability, and acousticness. This is not meant to be used 
for real users at scale. It is a classroom simulation meant to help 
explain how recommendation systems turn data into ranked predictions.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model uses content-based filtering, which means it recommends songs 
by comparing song features to user preferences. Each song has features 
such as genre, mood, energy, tempo, valence, danceability, and acousticness. 
The user profile stores target preferences for those same types of features.

The recommender gives points when a song matches the user’s favorite genre 
or mood. It also gives similarity points when numerical features, such as 
energy or danceability, are close to the user’s target values. After each 
song receives a score, the system sorts all songs from highest score to 
lowest score and returns the top recommendations.

From the starter logic, I expanded the scoring system so it does more 
than only check genre or energy. I added more song features, including 
valence, danceability, acousticness, and tempo. I also added explanations 
so each recommendation shows the reasons behind the score, such as genre 
match, mood match, or energy similarity.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset uses a catalog of 20 songs. The original starter file 
had 10 songs, and I added 10 more songs to make the catalog more 
diverse. The dataset includes features such as song title, artist, 
genre, mood, energy, tempo BPM, valence, danceability, and acousticness.

The catalog includes genres such as pop, lofi, rock, ambient, jazz,
synthwave, indie pop, bachata, salsa, Latin trap, chanson, emo, EDM, 
and alternative rock. It also includes moods such as happy, chill, 
intense, relaxed, moody, romantic, heartbroken, confident, dramatic,
melancholic, empowering, and uplifting.

Even though the dataset is more diverse than the starter version, 
it is still very small. Many genres only have one or two songs, 
so the recommender cannot fully represent all types of music taste. 
It also does not include lyrics, language preference, artist 
popularity, release year, user listening history, skips, likes, 
or playlist behavior.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well when the user profile is clear and matches songs 
that exist in the dataset. For example, the Happy Pop Listener profile 
gave reasonable results because songs like Sunrise City, Gym Hero, 
Chicago, and Rooftop Lights matched the user’s pop or happy direction 
and had similar numerical features.

The Chill Lofi Listener profile also worked well because the dataset 
has several calm, acoustic, low-energy songs like Library Rain, 
Midnight Coding, Spacewalk Thoughts, and Focus Flow. The recommender 
also did a good job recognizing intense, high-energy songs for the 
Deep Intense Rock Listener profile.

One strength of the system is that it does not only depend on genre. 
Songs from different genres can still rank well if their energy, tempo, 
valence, danceability, and acousticness are close to the user’s target 
profile. This makes the recommender feel more flexible.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One limitation of this recommender is that it depends heavily on the 
weights I manually chose. If genre is weighted too strongly, the system 
may create a filter bubble by mostly recommending songs from the same 
genre and ignoring songs with a similar vibe. If energy is weighted 
too strongly, songs from unrelated genres may rank highly just because 
they have a similar intensity.

The dataset is also small, with only 20 songs. Some genres only have 
one song, so users who prefer those genres may not get many accurate 
recommendations. The system also treats genres as exact matches, so 
pop and indie pop are considered different even though they are related.

Another limitation is that the recommender does not learn from real 
user behavior. It does not know if a user skipped a song, replayed it, 
liked it, or added it to a playlist. Because of this, it can only 
recommend based on the static song features in the CSV file.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I evaluated the recommender by testing several different user profiles. 
I tested a Happy Pop Listener, a Chill Lofi Listener, a Deep Intense Rock 
Listener, and an edge case profile called Sad High-Energy Listener. 
For each profile, I checked whether the top 5 recommendations matched 
what I would expect based on the genre, mood, and numerical features.

The Happy Pop Listener profile ranked Sunrise City first, which made 
sense because it matched both the favorite genre and favorite mood 
while also being close to the target values. The Chill Lofi Listener 
profile ranked calm and acoustic songs highly, which also matched my 
expectations. The Deep Intense Rock Listener profile ranked high-energy 
rock and intense songs near the top.

One surprising result happened with the Sad High-Energy Listener profile.
Helena ranked above My Immortal, even though My Immortal matched the 
favorite genre and mood more directly. This happened because the experiment 
increased the energy weight, and Helena had a much closer energy value to 
the user’s high-energy target. This showed that small changes in scoring 
weights can noticeably change the final recommendations.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

In the future, I would improve the recommender by adding more songs and 
making the dataset more balanced across genres and moods. I would also 
add more features, such as language, release decade, artist popularity, 
lyrical themes, and user listening history.

I would also improve the scoring logic so similar genres can be treated 
as related. For example, pop and indie pop should probably have partial 
similarity instead of being treated as completely different. Another 
improvement would be adding a diversity rule so the top recommendations 
do not all come from the same genre or artist.

Finally, I would improve the explanations by making them more natural. 
Instead of only listing score reasons, the system could say something like, 
“This song is recommended because it is upbeat, danceable, and close to 
your preferred happy pop vibe.”

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

This project helped me understand that recommendation systems do not 
magically know what someone likes. They turn data into predictions by 
comparing user preferences to item features, assigning scores, and 
ranking results. Even a simple scoring system can feel like a real 
recommendation when the features and weights are chosen carefully.

Something interesting I discovered is how sensitive recommendations 
are to small design choices. When I changed the weights to make energy 
more important and genre less important, the recommendations changed 
a lot. This helped me see how bias or unfairness can show up in real 
systems if certain features are over-prioritized or if the dataset 
does not represent enough variety. It made me think differently about 
music apps because their recommendations are shaped by both the data 
they collect and the assumptions built into their algorithms.