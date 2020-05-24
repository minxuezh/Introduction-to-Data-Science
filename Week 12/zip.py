avengers = ["The Avengers", "Avengers: Age of Ultron", "Avengers: Infinity War", "Avengers: Endgame"]
years = [2012, 2015, 2018, 2019]
for year, movie in zip(years, avengers):
  print("{}上映的年份是{}".format(movie, year))