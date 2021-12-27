import pandas as pd

data = pd.read_csv('./dataset/changed/train.csv')

new_data = []
    
for index, row in data.iterrows():
    new_data.append(row['0'])
    
print(new_data[:10])