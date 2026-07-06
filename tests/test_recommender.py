from src.recommender import (
    Song,
    UserProfile,
    Recommender,
    score_song,
    recommend_songs,
)


def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def make_song_dicts():
    return [
        {
            "id": 1,
            "title": "Test Pop Track",
            "artist": "Test Artist",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "tempo_bpm": 120,
            "valence": 0.9,
            "danceability": 0.8,
            "acousticness": 0.2,
        },
        {
            "id": 2,
            "title": "Chill Lofi Loop",
            "artist": "Test Artist",
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.4,
            "tempo_bpm": 80,
            "valence": 0.6,
            "danceability": 0.5,
            "acousticness": 0.9,
        },
    ]


def make_user_prefs():
    return {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "target_tempo_bpm": 120,
        "target_valence": 0.85,
        "target_danceability": 0.8,
        "target_acousticness": 0.2,
    }


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)

    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_score_song_returns_score_and_reasons():
    user_prefs = make_user_prefs()
    song = make_song_dicts()[0]

    score, reasons = score_song(user_prefs, song)

    assert isinstance(score, float)
    assert isinstance(reasons, list)
    assert len(reasons) > 0
    assert any("genre match" in reason for reason in reasons)
    assert any("mood match" in reason for reason in reasons)


def test_score_song_rewards_better_match():
    user_prefs = make_user_prefs()
    songs = make_song_dicts()

    pop_score, _ = score_song(user_prefs, songs[0])
    lofi_score, _ = score_song(user_prefs, songs[1])

    assert pop_score > lofi_score


def test_recommend_songs_returns_top_k_ranked_results():
    user_prefs = make_user_prefs()
    songs = make_song_dicts()

    results = recommend_songs(user_prefs, songs, k=1)

    assert len(results) == 1

    song, score, explanation = results[0]

    assert song["title"] == "Test Pop Track"
    assert isinstance(score, float)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_oop_recommender_respects_k_limit():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()

    results = rec.recommend(user, k=1)

    assert len(results) == 1


def test_acoustic_preference_changes_score_direction():
    songs = [
        Song(
            id=1,
            title="Acoustic Song",
            artist="Test Artist",
            genre="folk",
            mood="calm",
            energy=0.5,
            tempo_bpm=90,
            valence=0.6,
            danceability=0.4,
            acousticness=0.95,
        ),
        Song(
            id=2,
            title="Electronic Song",
            artist="Test Artist",
            genre="folk",
            mood="calm",
            energy=0.5,
            tempo_bpm=90,
            valence=0.6,
            danceability=0.4,
            acousticness=0.05,
        ),
    ]

    rec = Recommender(songs)

    acoustic_user = UserProfile(
        favorite_genre="folk",
        favorite_mood="calm",
        target_energy=0.5,
        likes_acoustic=True,
    )

    non_acoustic_user = UserProfile(
        favorite_genre="folk",
        favorite_mood="calm",
        target_energy=0.5,
        likes_acoustic=False,
    )

    acoustic_results = rec.recommend(acoustic_user, k=2)
    non_acoustic_results = rec.recommend(non_acoustic_user, k=2)

    assert acoustic_results[0].title == "Acoustic Song"
    assert non_acoustic_results[0].title == "Electronic Song"