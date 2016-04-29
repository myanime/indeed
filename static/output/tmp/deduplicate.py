import pandas as pd
myfile1 = './dick.csv'
toclean = pd.read_csv(myfile1)
deduped = toclean.drop_duplicates('url')
deduped.to_csv('./out_cron_deduped.csv')
