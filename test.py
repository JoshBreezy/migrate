import json
from operator import itemgetter
import pprint
from types import NoneType
from ytmusicapi import YTMusic
ytmusic = YTMusic('headers_auth.json')
pp = pprint.PrettyPrinter(indent=4)


listOfPlay = ytmusic.get_library_playlists(8)


def extractList(listOfL):
    for playL in listOfL:
        if 'count' not in playL:
            playL.update({'count': None})
        pp.pprint(playL)

extractList(listOfPlay)



#print(json.dumps(listOfPlay, sort_keys=True, indent=4))

#print(listOfPlay[0])
#fempop = ytmusic.get_playlist('PLN2vJjj3VWKD2p7EMV8_gJ45CIhAXlJEy', 107)

# newList = open('fempop.json', 'w')
# newList.write(json.dumps(listOfPlay, sort_keys=True, indent=4))
# newList.close()
