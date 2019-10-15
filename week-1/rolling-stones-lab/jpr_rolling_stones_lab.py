#------[import]------#
import csv
import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
# -------------------#

#------[create album dictionary]------#
with open('data.csv') as f:
    reader = csv.DictReader(f)
    albums = list(reader)
#-------------------------------------#

#-------[create song dictionary]-------#
text_file = open('top-500-songs.txt', 'r')
lines = text_file.readlines()
songs_no_t = [lines[i].split('\t') for i in range(len(lines))] # removed '\t'
song_year = [songs_no_t[i][-1][:4] for i in range(len(songs_no_t))] # removed '\n'
        
        
songs = [{'rank': song[0], 
          'name': song[1], 
          'artist': song[2]} for song in songs_no_t]

for i in range(len(songs_no_t)):
    songs[i]['year'] = song_year[i]
#--------------------------------------#

#------[json]------#
file = open('track_data.json', 'r')
json_data = json.load(file)
#------------------#

#------[jpr - not asked for but test]------#
def find_by_artist(artist_name, _dict):
    lst = [artist for artist in _dict if artist['artist'] == artist_name]
    print(lst)
    print("# of albums:", len(lst))
#------------------------------------------#

#------[functions]-----#
def find_album_by_name(album_name):
    for album in albums:
        if album['album'] == album_name:
            return album
    return 'None'

def find_album_by_rank(ranking):
    ranking = str(ranking)
    for rank in albums:
        if rank['number'] == ranking:
            return rank
    return 'None'

def find_album_by_ranks(start_rank, end_rank):
    start_rank = int(start_rank)
    end_rank = int(end_rank)
    rankings = list(range(start_rank, end_rank + 1))  
    final_list = [find_album_by_rank(rank) for rank in rankings]
    return final_list

def find_song_by_name(song_name):
    for song in songs:
        if song['name'] == song_name:
            return song
    return 'None'

def find_song_by_rank(ranking):
    ranking = str(ranking)
    for rank in songs:
        if rank['rank'] == ranking:
            return rank
    return 'None'

def find_song_by_ranks(start_rank, end_rank):
    start_rank = int(start_rank)
    end_rank = int(end_rank)
    rankings = list(range(start_rank, end_rank + 1))    
    final_list = [find_song_by_rank(rank) for rank in rankings]
    return final_list

def find_by_year(year, lst):    
    release = [item for item in lst if item['year'] == str(year)]
    return release  

def find_by_years(start_year, end_year, lst):
    start_year = int(start_year)
    end_year = int(end_year)
    time_period = list(range(start_year, end_year + 1))
    release =[item for item in lst if int(item['year']) in time_period]
    return release

def all_album_titles():
    album_titles = [album['album'].title() for album in albums]
    return album_titles

def all_song_titles():
    song_titles = [song['name'].title() for song in songs]
    return song_titles

def all_artists(lst):
    artists = [item['artist'] for item in lst]
    return artists

def most_albums():
    counter_dict = Counter(all_artists(albums))
    n = len(list(counter_dict.keys()))
    lst_keys = list(counter_dict.keys())
    lst_values = list(counter_dict.values())
    artists_with_most_albums = [lst_keys[i] for i in range(n) if
                                int(lst_values[i]) == max(lst_values)]
    return artists_with_most_albums

def most_singles():
    counter_dict = Counter(all_artists(songs))
    n = len(list(counter_dict.keys()))
    lst_keys = list(counter_dict.keys())
    lst_values = list(counter_dict.values())
    artists_with_most_singles = [lst_keys[i] for i in range(n) if
                                 int(lst_values[i]) == max(lst_values)]
    return artists_with_most_singles

def most_pop_word_albums():
    lst_words = []
    for title in all_album_titles():
        lst_words += title.split()
    counter_dict = Counter(lst_words)
    n = len(list(counter_dict.keys()))
    lst_keys = list(counter_dict.keys())
    lst_values = list(counter_dict.values())
    most_popular_word_album = [lst_keys[i] for i in range(n) if
                               int(lst_values[i]) == max(lst_values)]
    return most_popular_word_album

def most_pop_word_songs():
    lst_words = []
    for title in all_song_titles():
        lst_words += title.split()
    counter_dict = Counter(lst_words)
    n = len(list(counter_dict.keys()))
    lst_keys = list(counter_dict.keys())
    lst_values = list(counter_dict.values())
    most_popular_word_song = [lst_keys[i] for i in range(n) if
                              int(lst_values[i]) == max(lst_values)]
    return most_popular_word_song

def histogram_by_decade(lst):
    decades = [int(item['year']) for item in lst]
    return plt.hist(decades, range=(1950, 2020),bins=7)


def graph_by_genre():
    genres = [album["genre"] for album in albums]
    parsed_genres = []
    for genre in genres:
        parsed_genres.append(genre.split(',')[0])
    pd.Series(parsed_genres).value_counts().plot('bar')
    
def albumWithMostTopSongs():
    albums_with_tracks_top500 = []
    for album in json_data:
        for track in album['tracks']:
            if track in all_song_titles():
                albums_with_tracks_top500.append(album['album'])
    counter_dict = Counter(albums_with_tracks_top500)
    n = len(list(counter_dict.keys()))
    lst_keys = list(counter_dict.keys())
    lst_values = list(counter_dict.values())
    album_with_most_top_songs = [lst_keys[i] for i in range(n) if
                                 int(lst_values[i]) == max(lst_values)][0]
    lst_artist = [album['artist'] for album in albums
                  if album_with_most_top_songs == album['album']]
    artist = lst_artist[0]         
    print("Album:", album_with_most_top_songs)
    print("Artist:", artist)
    print("No. Top Tracks:", counter_dict[album_with_most_top_songs])
    
def albumsWithTopSongs():
    albums_with_tracks_top500 = []
    for album in json_data:
        for track in album['tracks']:
            if track in all_song_titles():
                albums_with_tracks_top500.append(album['album'])
    return set(albums_with_tracks_top500)

def songsThatAreOnTopAlbums():
    songs_on_top_albums = [album['tracks'] for album in json_data
                           if album['album'] in all_album_titles()]
    return songs_on_top_albums

# =============================================================================
# #def top10AlbumsByTopSongs_hist():
# # -- start:
# # -- create a Counter with keys = album name
# #    and values = # of songs in top 500
# #    get n, lst_keys, and lst_values
# albums = []
# for album in json_data:
#     for track in album['tracks']:
#         if track in all_song_titles():
#             albums.append(album['album'])
# counter_dict = Counter(albums).items()
# albums_dict = {k:v for (k,v) in counter_dict}
# n = len(albums_dict)
# lst_keys = albums_dict.keys()
# lst_values = albums_dict.values()
# top10_largest_values = []
# values = list(lst_values)
# for i in range(10):
#     max1 = 0
#     for j in range(len(values)):
#         if values[j] > max1:
#             max1 = values[j]
#     values.remove(max1)
#     top10_largest_values.append(max1)
# 
# =============================================================================
# =============================================================================
# for album in albums_dict:
#     for i in range(n)
#     if album[i]
# =============================================================================