import pandas as pd

class find_s:
    def __init__(self,data,target_column,target_positive_value):
        self.features=data[data[target_column]==target_positive_value].drop(columns=[target_column])
        self.targets = data[target_column]
        self.hypo=self.features.iloc[0]
    def find_s_algo(self):
        num_features=len(self.features.iloc[0])
        num_rows=len(self.features)
        for i in range(1,num_rows):
            for j in range(num_features):
                if(self.hypo[j]!=self.features.iloc[i][j]):
                    if(self.hypo[j]!="?" or self.features.iloc[i][j]!="?"):
                        self.hypo[j]="?"
        return self.hypo


data=[
    ["morning","sunny","warm","yes","mild","strong","yes"],
    ["evening","rainy","cold","no","mild","normal","no"],
    ["morning","sunny","moderate","yes","normal","normal","yes"]
]

data=pd.DataFrame(data=data,columns=["TIme","Weather","Temp","Company","Humid","Wind","Walk"])
print(data) 
s = find_s(data=data,target_column="Walk",target_positive_value="yes")
print(list(s.find_s_algo()))

