movie_title = input('請輸入電影的名稱:')
movie_rating = input('請輸入電影的評等:')
movie_rating = float(movie_rating)

if movie_rating > 7:
  print("{}的評等為{}分，值得去看!".format(movie_title, movie_rating))
else:
  print("{}的評等為{}分不值得去看，浪費時間!".format(movie_title, movie_rating))