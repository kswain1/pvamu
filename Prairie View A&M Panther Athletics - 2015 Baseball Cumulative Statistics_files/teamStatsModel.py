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

## Features and targets
# X = player_df['Launch Angle'].dropna()
# Y = player_df['Distance'].dropna()

# Y = Y.values.reshape(-1,1)
# X = X.values.reshape(-1,1)

# ##Machine learning for Regression Modelling
# reg = LinearRegression()

# #Create prediction space
# prediction_space = np.linspace(min(X), max(X)).reshape(-1,1)

# #fit the model to the data

# reg.fit(X,Y)

# #compute predictions over predictions sapce
# y_pred = reg.predict(prediction_space)

# y_scatter = reg.predict(X)


# #Print R^2
# print(reg.score(X,Y))

# plt.scatter(X,Y)
# #plt.plot(prediction_space,y_pred,color='black',linewidth =3)
# plt.scatter(X,y_scatter)

# plt.show()

data = 0
