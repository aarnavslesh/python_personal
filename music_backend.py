import pygame
from mutagen.mp3 import MP3
pygame.init()

#database?
#playback functions
def play_song(song_id):
    pygame.mixer.music.load(song_id)
    pygame.mixer.music.play()

def pause_song()
def next_song()
def previous_song()
