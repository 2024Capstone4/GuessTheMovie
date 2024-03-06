#Goal: To pull from JSONbin.io
import requests
import json
import rottentomatoes as rt
url = 'https://api.jsonbin.io/v3/b/65d77e13266cfc3fde8ddeb7/latest/'
headers = {
    'X-Master-Key': '$2a$10$vaoE2zeHNzxtHNFsBwBw7uMzvHzDdHKlB2xwIn0yBJy3.0fKO0JhG',
    'X-Bin-Meta': 'false'
}
req = requests.get(url, headers=headers)

data = json.loads(req.text)


#If title isn't exact, will not return anything
def get_scores(title):
    critic_score = 0
    audience_score = 0
    imdb_score = 0
    for i in data:
        if i['name'] == title:
            critic_score = i['tomatometer']
            audience_score = i['audience_score']
            imdb_score= i['imdb_score']
            break
    return [critic_score, audience_score, imdb_score]

def calculate_score(title, critic_guess, audience_guess,imdb_guess):
    #Calculates the score based on the player's guesses
    
    #Parameters:
    #   movie(str): Title of the movie the player guessed for
    #   imdb_guess (double): The player's guess for what the movies IMDb rating is
    #   critic_guess (double): The player's guess for what the Rotten Tomatoes critic score is
    #   audience_guess (double): The player's guess for what the Rotten Tomatoes audience score is
    
    #Returns:
    #   total_score(double): the player's score based on how close their guesses were
    
    critic_actual = get_scores(title)[0]
    audience_actual = get_scores(title)[1]
    imdb_actual = get_scores(title)[2]
    imdb_score = 100 - abs((imdb_actual - imdb_guess))
    critic_score = 100 - abs((critic_actual - critic_guess))
    audience_score = 100 - abs((audience_actual - audience_guess))
    total_score = (imdb_score + critic_score + audience_score)/3
    return total_score

def play_game(title):
    critic_guess = int(input("What do you think the Rotten Tomatoes critic score of " + title + " is? (0-100) "))
    audience_guess = int(input("What do you think the Rotten Tomatoes audience score of " + title + " is? (0-100) "))
    imdb_guess = int(input("What do you think the IMDb rating of " + title + " is? (0-100) "))
    
    print(calculate_score(title, critic_guess, audience_guess, imdb_guess))
play_game('Jurassic Park')
