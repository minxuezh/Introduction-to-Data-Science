movie_title = input("請輸入電影名稱：")
movie_rating = input("請輸入電影評分：")
movie_rating = float(movie_rating)

if movie_rating > 7:
    print("去電影院看{}".format(movie_title))
elif movie_rating > 6:
    print("在家裡看{}".format(movie_title))
else:
    print("不要看{}".format(movie_title))