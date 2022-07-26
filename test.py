import json
from operator import itemgetter
import pprint
from types import NoneType
from ytmusicapi import YTMusic
import requests
ytmusic = YTMusic('headers_auth.json')
pp = pprint.PrettyPrinter(indent=4)


listOfPlay = ytmusic.get_library_playlists(8)
spotId = 12151119078


def extractList(listOfL):
    bigList = []
    for playL in listOfL:
        playL.update({'count': 200})
        listId = playL['playlistId']
        bigList.append(ytmusic.get_playlist(listId))
    return bigList
        

bigL = extractList(listOfPlay)
outList = open('bigList.json', 'w')
outList.write(json.dumps(bigL, sort_keys=True, indent=4))

reqTrack = requests('post', )


#print(json.dumps(listOfPlay, sort_keys=True, indent=4))

#print(listOfPlay[0])
#fempop = ytmusic.get_playlist('PLN2vJjj3VWKD2p7EMV8_gJ45CIhAXlJEy', 107)

# newList = open('fempop.json', 'w')
# newList.write(json.dumps(listOfPlay, sort_keys=True, indent=4))
# newList.close()
