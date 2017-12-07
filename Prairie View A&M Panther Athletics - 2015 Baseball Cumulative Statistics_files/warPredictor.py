import pandas as pd
import matplotlib.pyplot as plt

##The goal of this project is predict the WAR projections for each during the 2017 season to see if aligns with the games
#Won for the Prairie View A&M University Team
#The difficult part about this is that these guys in college so some of the predictions don't translate over

prairieViewdF = pd.read_csv('PvamuTeamStatics2017.csv',)
gramblingdf = pd.read_csv('Grambling2017.csv')
tsudf = pd.read_csv('TSU2017.csv')
uapbdf = pd.read_csv('UAPB2017.csv')
southerndf = pd.read_csv('SouthernNoClean', delim_whitespace=True)

#new data frames to get ride of the last two rows
southernPlayers = southerndf.iloc[0:17]
pvamuPlayers = prairieViewdF.iloc[0:17]


