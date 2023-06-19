import spacy

nlp = spacy.load('en_core_web_md')

#open the file
file_path = r"C:\Users\yutzu\Dropbox\SL23030008361\Data Science (Fundamentals)\T21\movies.txt"
with open(file_path, "r") as movie_file:
    file_content = movie_file.read()

#create a list
movies =[]
movie_descriptions = file_content.split('Movie ')
for description in movie_descriptions:
    #movie, desc = description.split(':', 1)
    #movies[movie.strip()] = desc.strip()
    movies.append(description)

#calculate similarities
Planet_Hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""
watched_movie = nlp(Planet_Hulk)
similarities = []
for movie in movies:
    similarity = nlp(movie).similarity(watched_movie)
    print("Movie " + movie + " - ", similarity)
    similarities.append((movie, similarity)) 

#find the most similar movie
most_similar_movie = max(similarities, key=lambda x: x[1])
print("Next movie: ", "Movie " + most_similar_movie[0])