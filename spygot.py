import requests

class jerk(object):
	def __init__(self, episode):
		#day episode was posted
		self.day = episode["day"]

		#episode version
		self.version = episode["version"]
		
		#characters appearing in episode
		self.players = episode["players"]
		
		#year episode was posted
		self.year = episode["year"]
		
		#url to episode
		self.url = "jerkcity.com/_" + episode["url"]
		
		#thumbnail url
		self.thumbnail = "jerkcity.com/" + episode["thumbnail"]
		
		#image url
		self.image = "jerkcity.com/" + episode["image"]
		
		#list of tags (if available)
		self.tags = episode["tags"]
		
		#episode title
		self.title = episode["title"]
		
		#episode number
		self.episodeNum = episode["episode"]
		
		#month episode was posted
		self.month = episode["month"]
		
		#list of dialog quotes in order, if available
		if "dialog" in episode:
			self.dialog = episode["dialog"]
		
	#parses dialog into an easily read list of strings, or tells you if no dialog has been included
	def parseDialog(self):
		try:
			strs = []
			for quotes in self.dialog:
				string = quotes[0] + ": " + quotes[1]
				strs.append(string)
				
			return strs
		except:
			print "dialog doesn't exist!"
		
#returns a jerk object
def grab(dong):
	dongRq = requests.get("http://jerkcity.com/json/" + str(dong) + ".json")
	if dongRq.status_code == 404:
		return "Post doesn't exist!"
	else:
		jsondong = dongRq.json()
		jerkObj = jerk(jsondong)
		return jerkObj
