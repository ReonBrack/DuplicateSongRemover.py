#imports
import os

#globals
music_folder_path = ''

#funcions
def prepare():
	music_folder_path = os.path.expanduser('~/Music')

#def compare_name(file1, file2):
	
def create_neutral_string(file):
	common_audio_types = ['wav', 'mp3', 'ogg', 'flac', 'wma', 'aac', 'msv']
	#cut file extention
	lower = str(file).lower()
	clean_string = ''.join(e for e in lower if e.isalnum())
	return clean_string

#start
print create_neutral_string("Master_of+Puppets! 2.mp3")
