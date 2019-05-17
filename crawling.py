import requests
import json
from pprint import pprint

# 200 개 가져오기
result = []

for i in range(25):
    pageNum = i + 1
    url = f'https://api.themoviedb.org/3/movie/popular?api_key=b9f6c4bdaf12e4ca3645a65a32d03591&region=^KR$&language=ko-KR&page={pageNum}'
    data = requests.get(url).json()
    movieData = data['results']
    for movie in movieData:
        movie['poster_path'] = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
        movie['backdrop_path'] = f"https://image.tmdb.org/t/p/w500{movie['backdrop_path']}"
        result.append(movie)

with open('data.json', 'w') as outfile:
    json.dump(result, outfile, ensure_ascii = False)       
# jsonData = json.dumps(result, ensure_ascii = False)
# pprint(jsonData)

