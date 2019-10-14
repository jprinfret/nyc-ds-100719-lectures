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
    album_dict = list(reader)
#-------------------------------------#

#-------[create song dictionary]-------#
text_file = open('top-500-songs.txt', 'r')
lines = text_file.readlines()
songs = [lines[i].split('\t') for i in range(len(lines))] # removed '\t'
song_year = [songs[i][-1][:4] for i in range(len(songs))] # removed '\n'
        
        
song_dict = [{'rank': song[0], 
              'name': song[1], 
              'artist': song[2]} for song in songs]

for i in range(len(songs)):
    song_dict[i]['year'] = song_year[i]
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
    for album in album_dict:
        if album['album'] == album_name:
            return album
    return 'None'

def find_album_by_rank(ranking):
    ranking = str(ranking)
    for rank in album_dict:
        if rank['number'] == ranking:
            return rank
    return 'None'


def find_album_by_ranks(start_rank, end_rank):
    start_rank = int(start_rank)
    end_rank = int(end_rank)
    top_rankings = list(range(start_rank, end_rank + 1))    
    release = [album for album in album_dict if int(album['number']) in top_rankings]
    return release

def find_song_by_name(song_name):
    for song in song_dict:
        if song['name'] == song_name:
            return song
    return 'None'

def find_song_by_rank(ranking):
    ranking = str(ranking)
    for rank in song_dict:
        if rank['rank'] == ranking:
            return rank
    return 'None'

def find_song_by_ranks(start_rank, end_rank):
    start_rank = int(start_rank)
    end_rank = int(end_rank)
    top_rankings = list(range(start_rank, end_rank + 1))    
    release = [song for song in song_dict if int(song['rank']) in top_rankings]
    return release

def find_by_year(year, _dict):    
    release = [item for item in _dict if item['year'] == str(year)]
    return release  

def find_by_years(start_year, end_year, _dict):
    start_year = int(start_year)
    end_year = int(end_year)
    time_period = list(range(start_year, end_year + 1))
    release =[item for item in _dict if int(item['year']) in time_period]
    return release

def all_album_titles():
    album_titles = [album['album'].title() for album in album_dict]
    return album_titles

def all_song_titles():
    song_titles = [song['name'].title() for song in song_dict]
    return song_titles

def all_artists(_dict):
    artists = [item['artist'] for item in _dict]
    return artists

def most_albums():
    counter_dict = Counter(all_artists(album_dict))
    n = len(list(counter_dict.keys()))
    lst_keys = list(counter_dict.keys())
    lst_values = list(counter_dict.values())
    artists_with_most_albums = [lst_keys[i] for i in range(n) if int(lst_values[i]) == max(lst_values)]
    return artists_with_most_albums

def most_singles():
    counter_dict = Counter(all_artists(song_dict))
    n = len(list(counter_dict.keys()))
    lst_keys = list(counter_dict.keys())
    lst_values = list(counter_dict.values())
    artists_with_most_singles = [lst_keys[i] for i in range(n) if int(lst_values[i]) == max(lst_values)]
    return artists_with_most_singles

def most_pop_word_albums():
    lst_words = []
    for title in all_album_titles():
        lst_words += title.split()
    counter_dict = Counter(lst_words)
    n = len(list(counter_dict.keys()))
    lst_keys = list(counter_dict.keys())
    lst_values = list(counter_dict.values())
    most_popular_word_album = [lst_keys[i] for i in range(n) if int(lst_values[i]) == max(lst_values)]
    return most_popular_word_album

def most_pop_word_songs():
    lst_words = []
    for title in all_song_titles():
        lst_words += title.split()
    counter_dict = Counter(lst_words)
    n = len(list(counter_dict.keys()))
    lst_keys = list(counter_dict.keys())
    lst_values = list(counter_dict.values())
    most_popular_word_song = [lst_keys[i] for i in range(n) if int(lst_values[i]) == max(lst_values)]
    return most_popular_word_song

def histogram_by_decade(_dict):
    decades = [int(item['year']) for item in _dict]
    return plt.hist(decades, range=(1950, 2020),bins=7)


def graph_by_genre():
    genres = [album["genre"] for album in album_dict]
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
    album_with_most_top_songs = [lst_keys[i] for i in range(n) if int(lst_values[i]) == max(lst_values)][0]
    lst_artist = [album['artist'] for album in album_dict if album_with_most_top_songs == album['album']]
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
    songs_on_top_albums = [album['tracks'] for album in json_data if album['album'] in all_album_titles()]
    return songs_on_top_albums

# =============================================================================
# def top10AlbumsByTopSongs_hist():
# # -- start:
# # -- create a Counter with keys = album name
# #    and values = # of songs in top 500
#     albums = []
#     for album in json_data:
#         for track in album['tracks']:
#             if track in all_song_titles():
#                 albums.append(album['album'])
#     counter_dict = Counter(albums)
#     n = len(list(counter_dict.keys()))
#     lst_keys = list(counter_dict.keys())
#     lst_values = list(counter_dict.values())
# # -- end
#     
# # -- start:
# # -- create a list of the top 10 Counter values    
#     top10_largest_values = []
#     for i in range(10):
#         max1 = 0
#         for j in range(len(lst_values)):
#             if lst_values[j] > max1:
#                 max1 = lst_values[j]
#         lst_values.remove(max1)
#         top10_largest_values.append(max1)
#         unique_top_10 = set(top10_largest_values)
# # -- end:
#     
# # the 216 - 224 is very broken - error: "list index out of range"
# -- start:
# # -- create a list of albums whose Counter value is in the top 10
#     top10_albums = []
#     for value in unique_top_10:
#         for x in range(n):
#             if int(lst_values[x]) == value:
#                 top10_albums.append(lst_keys[x])
#     return top10_albums
# # -- end
# =============================================================================