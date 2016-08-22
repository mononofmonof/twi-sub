# -*- coding: utf-8 -*-

import tweepy

class TwiKey:

	__CONSUMER_KEY = 'CONSUMER_KEY'
	__CONSUMER_SECRET = 'CONSUMER_SECRET'
	__ACCESS_TOKEN = 'ACCESS_TOKEN'
	__ACCESS_SECRET = 'ACCESS_SECRET'

	def __init__(self):
		self._auth = tweepy.OAuthHandler(TwiKey.__CONSUMER_KEY, TwiKey.__CONSUMER_SECRET)
		self._auth.set_access_token(TwiKey.__ACCESS_TOKEN, TwiKey.__ACCESS_SECRET)
		self._api = tweepy.API(self._auth)

	@property
	def CONSUMER_KEY(self):
		return TwiKey.__CONSUMER_KEY

	@property
	def CONSUMER_SECRET(self):
		return TwiKey.__CONSUMER_SECRET

	@property
	def ACCESS_TOKEN(self):
		return TwiKey.__ACCESS_TOKEN
		
	@property
	def ACCESS_SECRET(self):
		return TwiKey.__ACCESS_SECRET

	@property
	def api(self):
		return self._api
