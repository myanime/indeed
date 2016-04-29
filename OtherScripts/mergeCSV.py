import pandas as pd
myfile1 = './out_cron.csv'
#myfile2 = './6.csv'
toclean = pd.read_csv(myfile1)
#print toclean
deduped = toclean.drop_duplicates('original_link')
deduped.to_csv('./out_cron.csv')

#df1 = pd.read_csv(myfile1)
#df2 = pd.read_csv(myfile2)
#df = pd.merge(df1,df2)
#df = pd.merge(df1,df2)
#df.to_csv('7.csv')
#print df1
