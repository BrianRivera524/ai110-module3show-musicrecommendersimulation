from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs for a user profile."""
        scored_songs = []

        for song in self.songs:
            score = 0

            if song.genre == user.favorite_genre:
                score += 2.0

            if song.mood == user.favorite_mood:
                score += 1.5

            energy_similarity = 1 - abs(song.energy - user.target_energy)
            score += energy_similarity * 2.0

            if user.likes_acoustic:
                score += song.acousticness
            else:
                score += 1 - song.acousticness

            scored_songs.append((song, score))

        scored_songs.sort(key=lambda item: item[1], reverse=True)

        top_songs = []

        for song, score in scored_songs[:k]:
            top_songs.append(song)

        return top_songs

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song was recommended to the user."""
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("genre match")

        if song.mood == user.favorite_mood:
            reasons.append("mood match")

        energy_similarity = 1 - abs(song.energy - user.target_energy)
        reasons.append(f"energy similarity: {energy_similarity:.2f}")

        if user.likes_acoustic:
            reasons.append("user likes acoustic songs")
        else:
            reasons.append("user prefers less acoustic songs")

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file and converts numeric values.
    """
    songs = []

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"])
            }

            songs.append(song)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    """
    score = 0
    reasons = []

    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.5
        reasons.append("mood match (+1.5)")

    energy_similarity = 1 - abs(song["energy"] - user_prefs["target_energy"])
    energy_points = energy_similarity * 2.0
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    tempo_similarity = max(
        0,
        1 - abs(song["tempo_bpm"] - user_prefs["target_tempo_bpm"]) / 100
    )
    tempo_points = tempo_similarity * 1.0
    score += tempo_points
    reasons.append(f"tempo similarity (+{tempo_points:.2f})")

    valence_similarity = 1 - abs(song["valence"] - user_prefs["target_valence"])
    valence_points = valence_similarity * 1.0
    score += valence_points
    reasons.append(f"valence similarity (+{valence_points:.2f})")

    danceability_similarity = 1 - abs(
        song["danceability"] - user_prefs["target_danceability"]
    )
    danceability_points = danceability_similarity * 1.0
    score += danceability_points
    reasons.append(f"danceability similarity (+{danceability_points:.2f})")

    acousticness_similarity = 1 - abs(
        song["acousticness"] - user_prefs["target_acousticness"]
    )
    acousticness_points = acousticness_similarity * 1.0
    score += acousticness_points
    reasons.append(f"acousticness similarity (+{acousticness_points:.2f})")

    return score, reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """
    Scores, ranks, and returns the top k recommended songs.
    """
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)

    return scored_songs[:k]