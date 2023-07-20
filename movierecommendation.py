import requests
from bs4 import BeautifulSoup

def get_movies_by_emotion(emotion):
    genre_mapping = {
        "Sad": "drama",
        "Disgust": "musical",
        "Anger": "family",
        "Anticipation": "thriller",
        "Fear": "sport",
        "Enjoyment": "thriller",
        "Trust": "western",
        "Surprise": "film_noir",
    }

    genre = genre_mapping.get(emotion)
    if genre is None:
        print("Invalid emotion! Please try again.")
        return

    url = f"http://www.imdb.com/search/title?genres={genre}&title_type=feature&sort=moviemeter, asc"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    movie_titles = soup.find_all("h3", class_="lister-item-header")

    count = 0
    for title in movie_titles:
        movie_name = title.a.text
        print(movie_name)
        count += 1
        if count > 10 and emotion not in ["Disgust", "Anger", "Surprise"]:
            break

if __name__ == "__main__":
    emotion = input("Enter the emotion: ")
    get_movies_by_emotion(emotion)

