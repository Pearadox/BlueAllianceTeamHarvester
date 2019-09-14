import requests

baseURL = "https://www.thebluealliance.com/api/v3/"
header = {'X-TBA-Auth-Key':'BRa4UYcX7J2Q4YK8cUHYprsXQAWk8hd9WKUleE1ADEwka3lCujsuWo9KwFKCuQRl'}

def getTBA(url):
    request = requests.get(baseURL + url,headers = header).json()
    return request

def getTeams():
    teams = []
    currentPage = 0
    currentTeams = getTBA("teams/" + str(currentPage) + "")
    for team in currentTeams:
        teams.append(team)
    while currentTeams != []:
        print('Page: ' + str(currentPage))
        currentPage+=1
        currentTeams = getTBA("teams/" + str(currentPage) + "")
        for team in currentTeams:
            teams.append(team)
    print('The amount of teams are ' + str(len(teams)))
    return teams

def getAliveTeams():
    allAliveTeams = []
    count = 0
    allTeams = getTeams()
    #print('The amount of allTeams are ' + str(len(allTeams)))
    for team in allTeams:
        try:
            #if count == 49:
            #    break
            if getTBA("team/" + team['key'] + "/years_participated")[-1] == 2019:
                allAliveTeams.append(team)
                print(team['key'] + ' Teams')
                count+=1
                #update the result structure
                
        except:
            #print('ERROR!')
            pass
    print('The List of teams is ' + str(len(allAliveTeams)) + ' teams long')
    #print('The Count of teams is ' + str(otalTeams))
    return allAliveTeams

def countryCount():
    countryCountArray = []

    
x = getAliveTeams()
#x = getAllTeams()
#for rookieYear in range(2004, 2019): #last number not included)
#    totalTeams = 0
#    deadTeams = 0
#    print(str(rookieYear) + " Rookies" , end = "\t")
#    for team in x:
#        try:
#            if team['rookie_year'] == rookieYear:
#                totalTeams+=1
#                if getTBA("team/" + team['key'] + "/years_participated")[-1] == 2019:
#                    deadTeams+=1
#        except:
#            pass
#    print(str(deadTeams) + "\t" + str(totalTeams))
