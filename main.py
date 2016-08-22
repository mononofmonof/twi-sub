# -*- coding: utf-8 -*-

import tkinter
import twi_sys.twi_sub
from tweepy.error import TweepError

i = twi_sys.twi_sub.TwiSub().api

def tweet_del():
	try:
		n = 0
		while True:
			i.destroy_status(i.user_timeline()[n].id_str)
			n += 1
	except (IndexError, TweepError):
		pass

if __name__ == '__main__':
	
	root = tkinter.Tk()
	root.title('hoge')

	twi_txtbox = tkinter.Entry(width='80')
	twi_txtbox.pack(padx='10', pady='10')

	twi_button_tweet = tkinter.Button(background='#fff', width='30', text='ツイート', command=lambda : i.update_status(twi_txtbox.get()) if twi_txtbox.get() != '' else twi_txtbox.insert(tkinter.END, '何か入力して下さい'))
	twi_button_tweet.pack(padx='20', pady='0')
	
	twi_button_del = tkinter.Button(background='#fff', width='30', text='ツイート削除', command=tweet_del)
	twi_button_del.pack(padx='20', pady='20')

	root.mainloop()