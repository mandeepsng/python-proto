from urllib.request import urlopen
import json

url = "https://www.googleapis.com/youtube/v3/videos?id=7blNxSScSQc&key=AIzaSyB_75RYJDTHiqBdtsBpnwZzeyrnVAkl_b8&fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics"
response = urlopen(url)
data_json = json.loads(response.read())
print(data_json)



