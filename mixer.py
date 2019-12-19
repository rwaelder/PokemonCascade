import pygame, sys
from musicList import get_song
from soundList import get_sound, get_attack_sound, get_pokemon_cry

class Mixer():
	def __init__(self):
		self.mixer = pygame.mixer
		self.mixer.init()
		self.SOUND_END = pygame.USEREVENT + 1 
		self.fxChannel = self.mixer.Channel(0)
		self.fxChannel.set_endevent(self.SOUND_END)
		self.mixer.init(channels=2)
		self.currentlyPlayingSong = None
		self.mixer.music.set_volume(0.7)
		self.queue = []


	def get_busy(self):
		return self.mixer.get_busy()

	def play_song(self, location, loops=-1):
		song = get_song(location)

		
		if song == None:
			print('Location not found.')
			return

		if song == self.currentlyPlayingSong:
			return

		else:
			# self.mixer.music.fadeout(100)
			self.mixer.music.load(song)
			self.currentlyPlayingSong = song
			self.mixer.music.set_volume(0.7)
			self.mixer.music.play(loops=loops)

	def play_sound(self, soundName):
		
		sound = get_sound(soundName)
		try:
			sound = self.mixer.Sound(file=sound)
		except:
			print('No sound found for: %s' % soundName)
			return

		if self.mixer.get_busy():
			self.fxChannel.queue(sound)
		else:
			self.fxChannel.play(sound)

	def play_attack_sound(self, attackName):
		sound = get_attack_sound(attackName)
		try:
			sound = self.mixer.Sound(file=sound)
		except:
			print('No sound found for attack: %s' % attackName)
			return
			
		if self.mixer.get_busy():
			self.queue.append(sound)
		else:
			self.mixer.Sound.play(sound)

	def play_cry_sound(self, pokemon):
		cry = get_pokemon_cry(pokemon)
		cry = self.mixer.Sound(file=cry)
		self.fxChannel.set_volume(0.8)
		if self.mixer.get_busy():
			self.fxChannel.queue(cry)
		else:
			self.fxChannel.play(cry)

	def try_play_queue(self, sound):
		if self.mixer.get_busy():
			return False
		else:
			self.mixer.Sound.play(sound)
			return True

	def play_next_sound(self):
		if len(self.queue) > 0:
			self.mixer.Sound.play(self.queue[0])
			self.queue.pop(0)

	def play_queue(self):
		if len(self.queue) > 0:
			if self.try_play_queue(self.queue[0]):
				self.queue.pop(0)


