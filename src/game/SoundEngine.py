from pygame import mixer

from ..settings import Settings


class SoundEngine:
	def __init__(self):
		# Initialize mixer
		mixer.init()

		# Map sound files to dict
		self.music_files = {
			'background_1': 'resources/music/Background.mp3'
		}

		self.sound_effects = {
			'pickup': 'resources/sounds/pickup.mp3',
			'nick_sound': 'resources/sounds/nick.wav',
			'jose_sound': 'resources/sounds/joseph.wav',
			'sean_sound': 'resources/sounds/sean.wav',
		}

	def play_music(self, music_file, repeat=-1):
		mixer.music.load(self.music_files[music_file])
		mixer.music.set_volume(Settings.music_volume)
		mixer.music.play(repeat)

	def play_sound_effect(self, effect_name):
		sound_effect = mixer.Sound(self.sound_effects[effect_name])
		sound_effect.set_volume(Settings.sound_effect_volume)
		sound_effect.play()

	def update_volume(self):
		mixer.music.set_volume(Settings.music_volume)
