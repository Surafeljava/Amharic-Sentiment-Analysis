import pandas as pd
from amseg.amharicSegmenter import AmharicSegmenter

print(' - ' * 30)

print('Word Tokenizing from train.csv . . .\n')


data = pd.read_csv('./dataset/changed/train.csv')

new_data = []

sent_punct = []
word_punct = []
segmenter = AmharicSegmenter(sent_punct,word_punct)
    
for index, row in data.iterrows():
    word = segmenter.amharic_tokenizer(row['0'])
    words = []
    for w in word:
        words.append(w.text)
        
    new_data.append(words)
    
    if(index == 30):
        break
    
    
pos = pd.read_csv('./dataset/POS/cleaned/pos_train.csv')

pos_tag = {}

for index, row in pos.iterrows():
    pos_tag[row['0']] = row['1']
    
pos_tagged = []

for wds in new_data:
    pos_row = []
    for w in wds:
        tag = ""
        try:
            tag = pos_tag[w]
        except Exception as e:
            tag = 'UNKNOWN'
        pos_row.append((w, tag))
        
    pos_tagged.append(pos_row)
    
print(pos_tagged)