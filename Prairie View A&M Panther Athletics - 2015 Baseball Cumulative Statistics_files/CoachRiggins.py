import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

team_df_2017 = pd.read_csv('PvamuTeamStatics2017.csv')
team_df_2016 = pd.read_csv('PvamuTeamStatics2016.csv')

advance_metrics_df = team_df_2016.append(team_df_2017)
advance_metrics_df = advance_metrics_df[advance_metrics_df['ab'] > 35]

BB = advance_metrics_df['bb']
HBP = advance_metrics_df['hbp']
H = advance_metrics_df['h']
TwoB = advance_metrics_df['2b']
ThreeB = advance_metrics_df['3b']
HR = advance_metrics_df['hr']
AB = advance_metrics_df['ab']
SF = advance_metrics_df['sf']


wOBA_df = (0.713*(BB) + 0.742*HBP + 0.898*(H-TwoB-ThreeB-HR) + 1.257*TwoB + 1.580*ThreeB + 2.007*HR) / (AB + BB + SF + HBP)
# for i in advance_metrics_df.count():
advance_metrics_df['wOBA'] = wOBA_df

swing_metrics_df = advance_metrics_df.loc[:,['ab','avg','r','slg%','ob%','wOBA']]

print wOBA_df.head()
print advance_metrics_df.head()
print swing_metrics_df.head()

print(advance_metrics_df.corr())
ax = sns.heatmap(data=swing_metrics_df.corr(), square=True, cmap='RdYlGn', annot=True,)
data = 9