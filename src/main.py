# """
# Command line runner for the Music Recommender Simulation.

# This file helps you quickly run and test your recommender.

# Implemented functions from recommender.py:
# - load_songs
# - score_song
# - recommend_songs
# """

# from recommender import load_songs, recommend_songs


# def main() -> None:
#     songs = load_songs("data/songs.csv")

#     print(f"Loaded songs: {len(songs)}")

#     # Starter example profile: Happy Pop Listener
#     user_prefs = {
#         "favorite_genre": "pop",
#         "favorite_mood": "happy",
#         "target_energy": 0.80,
#         "target_tempo_bpm": 120,
#         "target_valence": 0.85,
#         "target_danceability": 0.80,
#         "target_acousticness": 0.20
#     }

#     recommendations = recommend_songs(user_prefs, songs, k=5)

#     print("\nTop recommendations:\n")

#     for rec in recommendations:
#         # You decide the structure of each returned item.
#         # A common pattern is: (song, score, explanation)
#         song, score, explanation = rec

#         print(f"{song['title']} by {song['artist']} - Score: {score:.2f}")
#         print(f"Genre: {song['genre']} | Mood: {song['mood']}")
#         print(f"Because: {explanation}")
#         print()


# if __name__ == "__main__":
#     main()


"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

Implemented functions from recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    print(f"Loaded songs: {len(songs)}")

    # Starter example profile: Happy Pop Listener
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "target_tempo_bpm": 120,
        "target_valence": 0.85,
        "target_danceability": 0.80,
        "target_acousticness": 0.20
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nUser Profile: Happy Pop Listener")
    print("--------------------------------")
    print(f"Favorite genre: {user_prefs['favorite_genre']}")
    print(f"Favorite mood: {user_prefs['favorite_mood']}")
    print(f"Target energy: {user_prefs['target_energy']}")
    print(f"Target tempo: {user_prefs['target_tempo_bpm']} BPM")
    print(f"Target valence: {user_prefs['target_valence']}")
    print(f"Target danceability: {user_prefs['target_danceability']}")
    print(f"Target acousticness: {user_prefs['target_acousticness']}")

    print("\nTop Recommendations")
    print("-------------------")

    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec

        print(f"{index}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Genre: {song['genre']} | Mood: {song['mood']}")
        print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()
