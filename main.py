# Summary df for n_session within 4 moving period, each period is 4 weeks

df_n_session = df_p[df_p.period.isin([1,2,3,4])]
ds_n_session = df_n_session.groupby(['userId','period'])['sessionId'].count()

# turn groupby output to dataframe
df_n_session_count = pd.DataFrame(ds_n_session).reset_index()
df_n_session_count.columns = ['userId', 'period', 'n_session']
df_n_session_count.head(10)