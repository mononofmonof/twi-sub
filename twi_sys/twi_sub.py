# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
import tweepy
import twi_key

class TwiSub(twi_key.TwiKey):
	def __init__(self):
		super().__init__()

	#　なにかしら追加するため作った