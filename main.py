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
        return f'{self.title} {self.season_number} {self.episode_number}'

    # def __repr__(self):
    #     return f'Movies(title={self.title} year={self.release_year} genre= {self.genre} episode={self.episode_number} season={self.season_number}'
print(("Filmy i seriale ").upper())

if __name__ == "__main__":
    movie1 = Movies(title='The Godfather', year = 1972, genre = 'crime') 
    movie2 = Movies(title='Pulp Fiction', year = 1994, genre = 'crime')
    movie3 = Movies(title='Forrest Gump', year = 1994, genre = 'drama')
    movie4 = Series(title='Breaking Bad', year=2008, genre='crime', season='S01', episode='E01')
    movie5 = Series(title='Cosmos', year=2014, genre='crime', season='S01', episode='E01')
    movie6 = Series(title='Our Planet', year=2019, genre='nature documentary', season='S01', episode='E01')

movies_list = [movie1, movie2, movie3]
series_list = [series1, series2, series3]
movies_base = [movie1, movie2, movie3, series1, series2, series3]


movie_type = int(input('If you would like choose movies tape "1" if series then type "2": '))

if movie_type == 1: 
    sorted_movies  = sorted(movies_list, key=lambda movie: movie.title)
    for item in range (0,len(sorted_movies)):
        print(sorted_movies[item])
elif movie_type == 2:
   sorted_series = sorted(series_list, key=lambda ser: ser.title)
   for item in range (0,len(sorted_series)):
        print(sorted_series[item])
else: 
    print('This is not correct option. Please enter "1" or "2": ')        

