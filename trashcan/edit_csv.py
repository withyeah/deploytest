import csv
from pprint import pprint

with open('columns.csv', 'r+', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = ('id', 'title', 'vote_average', 'popularity', 'poster_path', 'original_language', 'original_title', 'overview', 'release_date', 'genres')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        pprint(row)
        genrelist = []
        for i in range(1, 7):
            if row[f"genre_ids__00{i}"]:
                genrelist.append(row[f"genre_ids__00{i}"])
        
        print(genrelist)
        writer.writerow({'id': row['id'], 'title': row['title'], 'vote_average': row['vote_average'], 'popularity': row['popularity'], 'poster_path': row['poster_path'], 'original_language': row['original_language'], 'original_title': row['original_title'], 'overview': row['overview'], 'release_date': row['release_date'], 'genres': genrelist})
        