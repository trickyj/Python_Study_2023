#here is the dictionary.
current_movies = {'Ring':'Starting at 11:15am', 
                  'beautifullife': 'Starting at 12:30', 
                  'Laksh': 'starting at 3:00pm',
                  'paranormal':'playing at 10:00pm'}
print ('This weeks show list: \n')
#Forloop to print the list of movie.
for key in current_movies:
    print('Now Playing: ', key)
#Store userinput in movie variable.
movie = input('\nWhat movie would you like the showtime for? \n')
#Get user input and put it into the variabe showtime
showtime = current_movies.get(movie)
#If else block.
if showtime == None:
    print("Requested movie isn't playing today\n")
else:
    print('movie Name: ', movie, 'Is start at', showtime)