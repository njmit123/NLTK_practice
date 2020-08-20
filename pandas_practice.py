import pandas as pd 

df = pd.read_csv('/home/njeyepatch/Computer Science/Machine Learning/NLP/NLTK_practice/pokemon_data.csv')
# print(df)
# print(df.head(3)) - 5 rows if no parameter
# print(df.tail())

#print(df.columns)

# print(df[['Name','HP']][0:5])

# print(df.iloc[2,1])
# for index,row in df.iterrows():
    #print(index,row)

# print(df.loc[df['Type 1']=='Fire'])
# print(df.describe())
# print(df.info())

# print(df.sort_values('Name').head())
# print(df.sort_values(['Name','HP']).head())
# df['Total'] = df['HP'] + df["Attack"] + df['Defense']
# print(df)
cols = list(df.columns)
# df = df[[cols[-1]]+cols[0:12]]
# print(df)