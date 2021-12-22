# project_churn_spark
exploring in mini set locally before go to Spark Cluster (DataBricks workspace)

### Data Source (Event Data):
- (mini 120MB) s3n://udacity-dsnd/sparkify/mini_sparkify_event_data.json
- (full 12GB) s3n://udacity-dsnd/sparkify/sparkify_event_data.json


### metrics (per interval)
- number of like #
- number of songplay # 
- number of dislike #
- number of addplaylist #
- number of addfriend # 
- number of adview #
- number of session #
- total listen duration #
- average duration / day
- average duration / session #
- tenure (from tenure_from to ob_datetime) #

- rate of dislike (ratio: n_dislike / n_songplay) #
- rate of ad per play (ratio: adview / n_songplay) #
- rate of addplaylist (ratio: add / n_songplay) #
- diversity of artist? n distinct artist # 
- rolling change of songlike. % #


### u churn

[13,
 28,
 29,
 35,
 53,
 54,
 61,
 70,
 92,
 109,
 131,
 100007,
 100008,
 100014,
 100015,
 100016,
 100018,
 200003,
 200017,
 300001,
 300004]

