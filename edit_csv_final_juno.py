import csv
from pprint import pprint

with open('result.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('finaldata.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ('movie_id', 'title', 'vote_average', 'popularity', 'poster_path', 'original_language', 'original_title', 'overview', 'release_date', 'genre', 'backdrop_path',)
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            # genrelist = []
            # for i in range(1, 7):
            #     if row[f"genre_ids__00{i}"]:
            #         genrelist.append(int(row[f"genre_ids__00{i}"]))
            writer.writerow({'movie_id': str(row['id']), 'title': str(row['title']), 'vote_average': str(row['vote_average']), 'popularity': str(row['popularity']), 'poster_path': str(row['poster_path']), 'original_language': str(row['original_language']), 'original_title': str(row['original_title']), 'overview': str(row['overview']), 'release_date': str(row['release_date']), 'genre': str(row['genre_ids__001']), 'backdrop_path': str(row['backdrop_path'])})
        