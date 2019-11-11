import twint

c = twint.Config()
c.Limit = 1000
c.Search = 'diagnosed with depression'
c.Near = 'Manila'
c.Pandas = True

twint.run.Search(c)

df = twint.storage.panda.Tweets_df

with open('diagnosed_depression.csv', 'a+') as f:
    df.to_csv(f, sep = "\t", index = False)

