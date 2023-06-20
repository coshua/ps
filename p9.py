word_dict = {}

while True:
    movie = input("Enter the name of movie: ")
    if movie == "q":
        break

    word_lst = movie.split(" ")
    for i in range(len(word_lst)):
        word = word_lst[i].lower()
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1

for key in word_dict:
    print(key, word_dict[key])
