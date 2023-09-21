MOOD_TO_MUSIC = {
    "positive": "https://open.spotify.com/playlist/3dnXGas4EgEYxlphPZT6zF?si=693e001db1be4de2",
    "negative": "https://open.spotify.com/playlist/1SrVJGNLflPKKYOEwfUHHQ?si=4ad3288124724e54",
    "neutral": "https://open.spotify.com/playlist/6HmCUFtjSTocAqBp1e3pC6?si=ac662c80a29c4ae8",
}


def get_recommendation(mood: str) -> str:
    return MOOD_TO_MUSIC.get(mood, "Invalid mood")
