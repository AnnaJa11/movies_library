import random
from datetime import datetime

class Movies:
    def __init__(self, title, year, genre):
        self.title = title
        self.release_year = year
        self.genre = genre

        # Variables
        self._visits_number = 0

    def __str__(self):
        return f'{self.title} {self.release_year}'
    
    # def __repr__(self):
    #     return f'Movies(title={self.title} year={self.release_year} genre= {self.genre}'
    
    @property
    def play(self):
        return self._visits_number
    
    @play.setter
    def play(self, increased_visits):
        increased_visits = int(self._visits_number) + 1
        self._visits_number = increased_visits
        return self._visits_number
    
class Series(Movies):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode    

    def __str__(self):
        return f'{self.title} {self.season} {self.episode}'

    # def __repr__(self):
    #     return f'Movies(title={self.title} year={self.release_year} genre= {self.genre} episode={self.episode_number} season={self.season_number}'


def get_movies():   
    sorted_movies  = sorted(movies_list, key=lambda movie: movie.title)
    for item in range (0,len(sorted_movies)):
        print(sorted_movies)
        

def search(user_movie_choice):
        for m in range (0,len(movies_base)):
            if user_movie_choice == movies_base[m].title:
                print(movies_base[m].title)
            

def get_series():   
    sorted_series = sorted(series_list, key=lambda ser: ser.title)
    for item in range (0,len(sorted_series)):
        print(sorted_series)
my_list = []
def generate_views():
    random_movie = random.choice(movies_base)
    random_num = random. randint(1, 100)
    random_movie._visits_number = random_num
    result = f'{random_movie} - number of visits: {random_movie._visits_number}\n'
    print(result)
    my_list.append(result)
    return result
print(my_list)

def run_generate_views():
    for i in range(0,10):
        generate_views()

def top_titles(how_many):
    for i in range(0,how_many):
        print(my_list[i])
    

print((f"Biblioteka filmow \n").upper())

if __name__ == "__main__":
    movie1 = Movies(title='The Godfather', year = 1972, genre = 'crime') 
    movie2 = Movies(title='Pulp Fiction', year = 1994, genre = 'crime')
    movie3 = Movies(title='Forrest Gump', year = 1994, genre = 'drama')
    movie4 = Movies(title='Return To Legoland', year = 2021, genre = 'drama')
    movie5 = Movies(title='Lamborghini', year = 2022, genre = 'sport/drama')
    movie6 = Movies(title='#Alive', year = 2020, genre = 'action/horror')
    movie7 = Series(title='Our Planet', year=2008, genre='crime', season='S01', episode='E01')
    movie8 = Series(title='Cosmos', year=2014, genre='crime', season='S01', episode='E01')
    movie9 = Series(title='Breaking Bad', year=2019, genre='nature documentary', season='S01', episode='E01')

movies_list = [movie1, movie2, movie3, movie4, movie5, movie6]
series_list = [movie7, movie8, movie9]
movies_base = movies_list + series_list

print('Movies: \n')
for i in range (0,len(movies_list)):
    print(f'{movies_list[i]}\n')
print('Series: \n')
for i in range (0,len(series_list)):
    print(f'{series_list[i]}\n')

run_generate_views()

print(f"The most popular movies and series of the day {datetime.today().strftime('%d.%m.%Y')}\n")
top_titles(3)




# movie_type = int(input('If you would like choose movies tape "1" if series then type "2": '))

# if movie_type == 1: 
#     get_movies()
#     user_movie_choice = input('Enter the movie title: ')
#     search(user_movie_choice)
    
       
# elif movie_type == 2:
#    get_series()
#    user_movie_choice = input('Enter the movie title: ')

# else: 
#     print('This is not correct option.')    




