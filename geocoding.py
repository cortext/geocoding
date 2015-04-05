#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# by Antoine Mazières (http://mazier.es ; {github|twitter}@mazieres)
# Cortext Lab -- http://www.cortext.net/
#

import json
import sys
import requests
from time import sleep, gmtime, strftime

reload(sys) 
sys.setdefaultencoding("utf-8")


# You must provide an API_KEY to use this service: https://developers.google.com/maps/documentation/geocoding/#api_key
# You should also register the IP of the computer you whish to run this script from.
API_KEY = "YOUR_API_KEY"
API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'


def done_places():
	"""
	Returns a list of all places already geocoded from previous executions of the script and saved in places.json.
	"""
	f = open('places.json')
	done = set()
	for l in f:
		dat = json.loads(l)
		done.add(dat.keys()[0])
	f.close()
	print "Found {} places in ./places.json".format(len(done))
	return done

def new_places():
	"""
	Returns a list of the places description listed, one per line, in todo.txt, after making sure there are not already available in places.json.
	"""
	f = open('todo.txt')
	done = done_places()
	todos = {x.strip() for x in f}
	new_places = todos - done
	f.close()
	print "Found {} new places to check in ./todo.txt".format(len(new_places))
	return new_places

def update_places(todo, wait=True):
	"""
	Query Google Maps API for each of the place descriptions listed in todo.
	Params:
	- todo: a list of all places to be checked on Google Maps API
	- wait: If set to False, exit when the usage limit is reached. Wait for 25 hours if set to True.
	"""
	params = {"key": API_KEY}
	i = 0
	for loc in todo:
		print i, loc
		params["address"] = loc
		r = requests.get(API_URL, params=params)
		if r.status_code == 200:
			res = r.json()
			if res['status'] in ['OK', 'ZERO_RESULTS']:
				f = open('places.json', 'a')
				f.write("{}\n".format(json.dumps({loc: res})))
				f.close()
				sleep(1)
			elif res['status'] == "OVER_QUERY_LIMIT":
				t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
				print t, "OVER_QUERY_LIMIT"
				if not wait:
					return
				sleep(3600*25)
			else:
				print res
				sys.exit(1)
		else:
			print r.status_code
			print r.headers
			sys.exit(1)
		i += 1
	return


if __name__ == '__main__':
	todo = new_places()
	update_places(todo)



