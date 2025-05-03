movie_rank = [
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "Forrest Gump",
    "Fight Club",
    "Inception",
    "The Matrix",
    "Goodfellas",
    "Interstellar",
    "The Green Mile",
]

start_rank = int(input("Enter the start number of ranking: "))
end_rank = int(input("Enter the end number of ranking: "))
for i in range(start_rank, end_rank + 1):
    print(i, movie_rank[i])
