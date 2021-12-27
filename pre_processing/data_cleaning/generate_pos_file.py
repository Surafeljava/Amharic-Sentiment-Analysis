import pandas as pd

print(' - ' * 30)

print('Generating POS Tag file . . .\n')

pos_data = {}
pos = pd.read_csv('./dataset/POS/train_set.tsv', sep='\t')
for index, row in pos.iterrows():
    if(row[0] != None):
        pos_data[row[0]] = row[1]
    else:
        print(row[0])
        
pos_csv = []
for key in pos_data:
    pos_csv.append([key, pos_data[key]])
    
new_df = pd.DataFrame(pos_csv)
new_df.to_csv('./dataset/POS/cleaned/pos_train.csv', index=False)

print('DONE!')