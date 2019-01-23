import requests

def shot_data(season='2018-19', game_id='', player_id=0, team_abb=''):
    team_dict = {'ATL': 1610612737, 'BOS': 1610612738,
                 'BKN': 1610612751, 'CHA': 1610612766, 
                 'CHI': 1610612741, 'CLE': 1610612739, 
                 'DAL': 1610612742, 'DEN': 1610612743, 
                 'DET': 1610612765, 'GSW': 1610612744, 
                 'HOU': 1610612745, 'IND': 1610612754,
                 'LAC': 1610612746, 'LAL': 1610612747, 
                 'MEM': 1610612763, 'MIA': 1610612748,
                 'MIL': 1610612749, 'MIN': 1610612750, 
                 'NOP': 1610612740, 'NYK': 1610612752,
                 'OKC': 1610612760, 'ORL': 1610612753, 
                 'PHI': 1610612755, 'PHX': 1610612756,
                 'POR': 1610612757, 'SAC': 1610612758,
                 'SAS': 1610612759, 'TOR': 1610612761,
                 'UTA': 1610612762, 'WAS': 1610612764,
                 '': 0
                 }
    full_url = 'https://stats.nba.com/stats/shotchartdetail?AheadBehind=&CFID=33&CFPARAMS=' + season + \
                '&ClutchTime=&Conference=&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&Division=&EndPeriod=10&EndRange=28800&GROUP_ID=&GameEventID=&GameID=' + game_id + \
                '&GameSegment=&GroupID=&GroupMode=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OnOff=&OpponentTeamID=0&Outcome=&PORound=0&Period=0&PlayerID=' + str(player_id) + \
                '&PlayerID1=&PlayerID2=&PlayerID3=&PlayerID4=&PlayerID5=&PlayerPosition=&PointDiff=&Position=&RangeType=0&RookieYear=&Season=' + season + \
                '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StartPeriod=1&StartRange=0&StarterBench=&TeamID=' + str(team_dict[team_abb]) + \
                '&VsConference=&VsDivision=&VsPlayerID1=&VsPlayerID2=&VsPlayerID3=&VsPlayerID4=&VsPlayerID5=&VsTeamID='
    json = requests.get(full_url, headers=headers).json()
    return(json)