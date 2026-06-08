import sys
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Create a built-in dataset of movies and their genres
movies_data = {
    'Movie_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Title': [
        'The Dark Knight', 'Inception', 'Interstellar', 
        'The Hangover', 'Superbad', 'Toy Story', 
        'Finding Nemo', 'The Conjuring', 'Hereditary', 'The Notebook'
    ],
    'Genres': [
        'Action Crime Drama', 'Action Sci-Fi Thriller', 'Adventure Drama Sci-Fi',
        'Comedy', 'Comedy', 'Animation Adventure Comedy',
        'Animation Adventure Family', 'Horror Mystery Thriller', 'Horror Mystery', 'Drama Romance'
    ]
}

# Load data into a Pandas DataFrame
df = pd.DataFrame(movies_data)

def get_recommendations(movie_title, num_recommendations=2):
    # Convert input to title case to match our dataset titles
    movie_title = movie_title.strip().title()
    
    if movie_title not in df['Title'].values:
        return None

    # 2. Convert text genres into a matrix of token counts
    vectorizer = CountVectorizer()
    genre_matrix = vectorizer.fit_transform(df['Genres'])

    # 3. Compute the Cosine Similarity matrix based on genres
    similarity_matrix = cosine_similarity(genre_matrix, genre_matrix)

    # Get the index of the movie that matches the title
    movie_idx = df[df['Title'] == movie_title].index[0]

    # Get a list of similarity scores for this movie with all other movies
    similarity_scores = list(enumerate(similarity_matrix[movie_idx]))

    # Sort the movies based on the similarity scores in descending order
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Exclude the first movie (the selected movie itself) and fetch top recommendations
    recommended_indices = [item[0] for item in sorted_scores[1:num_recommendations+1]]
    
    # Return titles and corresponding genres
    return df.iloc[recommended_indices][['Title', 'Genres']]

def main():
    print("==================================================")
    print("     🎬 MOVIE RECOMMENDATION SYSTEM (AI) 🎬      ")
    print("        Content-Based Filtering Engine            ")
    print("==================================================")
    
    print("\nAvailable Movies in the Database:")
    for title in df['Title']:
        print(f" • {title}")
    
    print("\n--------------------------------------------------")
    print("Type 'exit' or 'bye' to quit the program.")
    print("--------------------------------------------------")

    while True:
        try:
            user_input = input("\nEnter a movie title from the list: ").strip()
            
            if user_input.lower() in ['exit', 'bye']:
                print("Thank you for using the recommendation system. Goodbye!")
                break
                
            recommendations = get_recommendations(user_input)
            
            if recommendations is not None:
                print(f"\n🎯 Because you liked '{user_input.title()}', we recommend:")
                for idx, row in recommendations.iterrows():
                    print(f" -> {row['Title']} [Genres: {row['Genres']}]")
            else:
                print("❌ Movie not found in the database. Please check the spelling and try again!")
                
        except (KeyboardInterrupt, EOFError):
            print("\nProgram closed. Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()