import pandas as pd
import numpy as np

class candidate_elimination():
    def __init__(self,data,target_column,target_positive_value) -> None:
        self.features=data.drop(columns=[target_column])
        self.targets = data[target_column]
        self.G=[["?" for _ in range(len(self.features.columns))] for _ in range(len(self.features.columns))]
        self.S=[None]*len(self.features.columns)
        self.target_positive_value=target_positive_value
        print(self.features)
        print(self.targets)
    
    def algo(self):
        num_records=len(self.features)
        num_cols=len(self.features.columns)
        for i in range(num_records):
            if(self.targets[i]==self.target_positive_value):
                for j in range(num_cols):
                    if(self.S[j]!=self.features.iloc[i][j]):
                        self.S[j]='?'
                        self.G[j][j] = "?"
            else:
                for j in range(num_cols):
                    if(self.features.iloc[i][j]!=self.S[j]):
                        self.G[j][j] = self.S[j]
                    else:
                        self.G[j][j] = '?'


data = pd.read_csv("1BM21AI004IML\likesport.csv")
print(data)
c=candidate_elimination(data,target_column="enjoysport",target_positive_value="yes")
c.algo()
print(c.S,c.G)