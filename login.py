import argparse
from furryposter.websites import sofurry, weasyl, furaffinity
from furryposter.websites.website import Website
import http.cookiejar


def initParser():
	parser = argparse.ArgumentParser(prog="furry_login", description="Login to furry websites")
	#site flags
	parser.add_argument('-F','--furaffinity', action='store_true', help="Flag for whether FurAffinity should be tried")
	parser.add_argument('-S','--sofurry', action='store_true', help="Flag for whether SoFurry should be tried")
	parser.add_argument('-W','--weasyl',action='store_true', help="Flag for whether Weasyl should be tried")
	
	return parser

def site_login(cj_path: str, site: Website):
	cj = http.cookiejar.MozillaCookieJar()
	site.load(cj)
	
	username = input('Please enter a username: ')
	password = input('Please enter a password: ')
	site.login(username, password)
	cj.save(cj_path)
	

def main(args):
	if args.furaffinity:
		file = "furaffinitycookies.txt"
		site_login(file, furaffinity.FurAffinity())
		
	if args.sofurry:
		file = "sofurrycookies.txt"
		site_login(file, sofurry.SoFurry())
		
	if args.weasyl:
		file = "weasylcookies.txt"
		site_login(file, weasyl.Weasyl())
	

if __name__ == '__main__':
	parser = initParser()
	args = parser.parse_args()
	main(args)