from NBALeagueChartUtil import NBARanking

chatname = 'NBALeagueChart'
myurl = 'https://www.nba.com/stats/teams/traditional/?sort=W_PCT&dir=-1&SeasonType=Regular%20Season&Season=2020-21'

nbalist = NBARanking(chatname, myurl)

soup = nbalist.getWebDriver()

saveData = list()

rank_list = soup.find('div', attrs={'class':'nba-stat-table__overflow'})
mytbodylist = rank_list.find('tbody')
mytrlist = mytbodylist.findAll('tr')

for onelist in mytrlist:
    mythlists = onelist.findAll('td')

    if(len(mythlists) > 1):

        teamname = onelist.select_one('td:nth-of-type(2)')
        teamname = teamname.a.string

        totalgames = onelist.select_one('td:nth-of-type(3)').string
        wingames = onelist.select_one('td:nth-of-type(4)').string
        losegames = onelist.select_one('td:nth-of-type(5)').string

        field_goal_pct = onelist.select_one('td:nth-of-type(11)').string
        threepoin_pct = onelist.select_one('td:nth-of-type(14)').string

        offensive_reb_avg = onelist.select_one('td:nth-of-type(18)')
        offensive_reb_avg = offensive_reb_avg.a.text.replace('\n', '').replace('            ','')

        defensive_reb_avg = onelist.select_one('td:nth-of-type(19)')
        defensive_reb_avg = defensive_reb_avg.a.text.replace('\n', '').replace('            ','')

        assist_avg = onelist.select_one('td:nth-of-type(21)')
        assist_avg = assist_avg.a.text.replace('\n', '').replace('            ','')

        turnover_avg = onelist.select_one('td:nth-of-type(22)')
        turnover_avg = turnover_avg.a.text.replace('\n', '').replace('            ','')

        steal_avg = onelist.select_one('td:nth-of-type(23)')
        steal_avg = steal_avg.a.text.replace('\n', '').replace('            ','')

        block_avg = onelist.select_one('td:nth-of-type(24)')
        block_avg = block_avg.a.text.replace('\n', '').replace('            ','')

        saveData.append([teamname, totalgames, wingames, losegames, field_goal_pct, threepoin_pct,
                         offensive_reb_avg, defensive_reb_avg, assist_avg,
                         turnover_avg, steal_avg, block_avg])

nbalist.save2Csv(saveData)