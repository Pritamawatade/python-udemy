import os
import json

FILE_NAME = "movies.json"

def load_movies():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding='utf-8') as f:
        return json.load(f)

def save_movies(movies):
    with open(FILE_NAME, "w", encoding='utf-8') as f:
        json.dump(movies, f, indent=2)


def save(movies):
    title = input("Enter movie title: ").strip().lower()
    
    # with open(FILE_NAME, 'r', encoding="utf-8") as f:
    if any(movie["title"] == title  for movie in movies):
        print("movie already exists")
    
    genre = input("Enter genre").strip().lower()
        
    try:
        rating = float(input("Enter rating (0-10): ").strip())
        if rating < 0 or rating > 10:
            raise ValueError("Rating must be between 0 and 10.")
        movies.append({"title": title, "genre": genre, "rating": rating})
        save_movies(movies)
    except ValueError:
        print("Invalid rating. Please enter a number between 0 and 10.")
        return
        

def search_movies(movies):
    term = input("Enter the title or movies : ").lower()
    
    results = [
        movie for movie in movies
        if term in movie['title'].lower() or term in movie['genre'].lower()
    ]
    
    if not results:
        print("No matching match")
        return
    print(f"found {len(results)} in movies")
    for i, result in enumerate(results, start=1):
        print(f"result {i} : title : {result['title']} genre : {result['genre']}")
        
def view_all_movies(movies):
    
    if not movies:
        print("no movies found")
        return
    
    for i , movie in enumerate(movies):
        print(f"\nmovie {i} : Title : {movie['title']} and Genre: {movie['genre']} ")
def run_movies():
    movies = load_movies()
    print(movies)
    while True:
        print("Select option\n")
        print("1. add movies \n 2. search movies\n 3. view all movies : \n")
        option = int(input("Enter your choice: "))
        
        match(option):
            case 1: 
                save(movies)
            case 2:
                search_movies(movies)
            case 3: view_all_movies(movies)
            case _:
                print("Please enter valid option\n")
                
                
if __name__ == '__main__':
    run_movies()