from os import sep
import pandas as pd


data = []
with open('./dataset/corpus/test.txt', encoding='utf8') as f:
    for line in f:
        if(line != ""):
            snt = line.split('\n')
            data.append(str(snt[0]))
    
        
new_df = pd.DataFrame(data)

new_df.to_csv('./dataset/changed/train.csv', index=False)