#coding=utf-8

__author__ = "Lisl"

import json

class GameStats(object):
	"""docstring for GameStats"""
	def __init__(self, ai_settings):
		super(GameStats, self).__init__()
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		


	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
		try:
			with open("high_score.txt") as high_score_file:
				self.high_score = json.load(high_score_file)
		except IOError as e:
			self.high_score = 0
		
		 