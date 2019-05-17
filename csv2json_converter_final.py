import csv
import json

# https://docs.python.org/2/library/csv.html
file_name = 'finaldata.csv' # change to the csv file name that you are trying to upload
with open(file_name) as csvfile:
    csvfile = csv.DictReader(csvfile)
    app_name = 'movies' # change this to your Django app name
    model_name = 'Movie' # the name of you Django model
    field_1 = 'movie_id'
    field_2 = 'title'
    field_3 = 'vote_average'
    field_4 = 'popularity'
    field_5 = 'poster_path'
    field_6 = 'original_language'
    field_7 = 'original_title'
    field_8 = 'overview'
    field_9 = 'release_date'
    field_10 = 'genre'
    field_11 = 'backdrop_path'
    x = 0
    output = []
    for each in csvfile:
        x += 1
        row = {}
        row = {'model': app_name+'.'+model_name, 'pk': x, 'fields': ({field_1: each[field_1], field_2: each[field_2], field_3: each[field_3], field_4: each[field_4], field_5: each[field_5], field_6: each[field_6], field_7: each[field_7], field_8: each[field_8], field_9: each[field_9], field_10: each[field_10], field_11: each[field_11]})}
        output.append(row)
    json.dump(output, open('test500.json','w'), indent=4, sort_keys=False, ensure_ascii=False)