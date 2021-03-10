import requests
import os

class Player:
    def __init__(self, player_id):

        response = requests.get('https://api.opendota.com/api/players/' + str(os.environ['PLAYER_ID']))
        info = response.json()

        self.player_id = info
        self.local_name = info['profile']['personaname']
        self.local_mmr = info['mmr_estimate']['estimate'] 
        self.local_last_login = info['profile']['last_login']

    def name(self):

        return self.local_name

    def mmr(self):

        return self.local_mmr

    def lastLogin(self):

        return self.local_last_login