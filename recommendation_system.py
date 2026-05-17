import math

# Sample Dataset: Movies with their genre weights
movies = [
    {"title": "The Matrix", "genres": {"Action": 1.0, "Sci-Fi": 1.0, "Thriller": 0.5}},
    {"title": "Inception", "genres": {"Action": 0.8, "Sci-Fi": 1.0, "Thriller": 0.9}},
    {"title": "Interstellar", "genres": {"Adventure": 0.8, "Drama": 0.9, "Sci-Fi": 1.0}},
    {"title": "The Dark Knight", "genres": {"Action": 1.0, "Crime": 0.9, "Drama": 0.8}},
    {"title": "Avengers: Endgame", "genres": {"Action": 1.0, "Adventure": 0.9, "Sci-Fi": 0.8}},
    {"title": "Pulp Fiction", "genres": {"Crime": 1.0, "Drama": 0.8, "Comedy": 0.5}},
    {"title": "The Shawshank Redemption", "genres": {"Drama": 1.0, "Crime": 0.3}},
    {"title": "Forrest Gump", "genres": {"Drama": 1.0, "Romance": 0.9, "Comedy": 0.6}},
    {"title": "Jurassic Park", "genres": {"Adventure": 1.0, "Sci-Fi": 0.8, "Thriller": 0.7}},
    {"title": "Toy Story", "genres": {"Animation": 1.0, "Adventure": 0.8, "Comedy": 0.9}}
]

available_genres = ["Action", "Sci-Fi", "Thriller", "Adventure", "Drama", "Crime", "Comedy", "Romance", "Animation"]

def calculate_similarity(user_profile, item_profile):
    """Calculates cosine similarity between user profile (ratings) and item profile."""
    dot_product = 0.0
    user_magnitude_sq = 0.0
    item_magnitude_sq = 0.0
    
    all_genres = set(user_profile.keys()).union(set(item_profile.keys()))
    
    for genre in all_genres:
        # Get rating/weight or default to 0.0 if not present
        u_val = user_profile.get(genre, 0.0)
        i_val = item_profile.get(genre, 0.0)
        
        dot_product += u_val * i_val
        user_magnitude_sq += u_val ** 2
        item_magnitude_sq += i_val ** 2
        
    if user_magnitude_sq == 0 or item_magnitude_sq == 0:
        return 0.0
        
    return dot_product / (math.sqrt(user_magnitude_sq) * math.sqrt(item_magnitude_sq))

def get_recommendations(user_profile, top_n=3):
    """Gets top N recommended movies based on user profile."""
    recommendations = []
    
    for movie in movies:
        # Calculate similarity score
        score = calculate_similarity(user_profile, movie["genres"])
        
        if score > 0:
            recommendations.append({
                "title": movie["title"], 
                "score": score, 
                "genres": list(movie["genres"].keys())
            })
            
    # Sort recommendations by similarity score in descending order
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations[:top_n]

def main():
    print("=============================================")
    print(" 🎬 Welcome to the AI Movie Recommender! 🎬 ")
    print("=============================================")
    print("Please rate your interest in the following genres from 1 to 5.")
    print("(Press Enter to skip a genre if you have no preference)\n")
    
    user_profile = {}
    
    # Take user input and build their preference profile
    for genre in available_genres:
        while True:
            rating_input = input(f"Rate '{genre}' (1-5): ").strip()
            if not rating_input:
                break # User skipped this genre
                
            try:
                rating = float(rating_input)
                if 1 <= rating <= 5:
                    user_profile[genre] = rating
                    break
                else:
                    print("  -> Please enter a number between 1 and 5.")
            except ValueError:
                print("  -> Invalid input. Please enter a valid number.")
                
    if not user_profile:
        print("\nYou didn't rate any genres. Exiting...")
        return
        
    print("\n🔍 Calculating similarity scores and finding matches...\n")
    recs = get_recommendations(user_profile, top_n=4)
    
    # Display the recommended items
    if not recs:
        print("Sorry, no recommendations found based on your ratings.")
    else:
        print("Top Recommendations for you:")
        print("-" * 45)
        for i, rec in enumerate(recs, 1):
            score_percentage = round(rec['score'] * 100)
            genres_str = ", ".join(rec['genres'])
            print(f"{i}. {rec['title']}")
            print(f"   Similarity Match: {score_percentage}%")
            print(f"   Genres: {genres_str}\n")

if __name__ == "__main__":
    main()
