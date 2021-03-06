import requests


def getRecentMatches(playerId):

    response = requests.get('https://api.opendota.com/api/players/' + str(playerId) + '/recentMatches')

    return response

def getWinsAndLoses(playerId, since):
    
    output = {
        'wins': 0,
        'loses': 0
    }
    
    results = getRecentMatches(playerId)
    json = results.json()
    
    for match in json:
    
        if (match['start_time'] > since):
            
            # fatallik was radiant and won 
            if match['radiant_win'] == True and match['player_slot'] <= 127:          
                output['wins'] += 1

            # fatallik was radiant and lost
            elif match['radiant_win'] == True and match['player_slot'] >= 127:        
                output['loses'] += 1

            # fatallik was dire and won
            elif match['radiant_win'] == False and match['player_slot'] >= 128:      
                output['wins'] += 1

            # fatallik was dire and lost
            elif match['radiant_win'] == False and match['player_slot'] <= 128:       
                output['loses'] += 1 

    print(output['wins'])
    print(output['loses'])

    return output
    