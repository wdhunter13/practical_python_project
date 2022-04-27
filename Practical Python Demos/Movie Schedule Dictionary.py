current_movies = {'movie1':'10:00am',
                  'movie2':'11:00am',
                  'movie3':'1:00pm',
                  'movie4':'2:00pm'}


print("We're showing the following movies")

for key in current_movies:
    print(key)

movie = input('What movie would you like the showtime for?')

showtime = current_movies.get(movie)

if showtime == None:
    print("No Showtimes")

else:
    print(movie, "is playing at", showtime)