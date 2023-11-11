import pandas as pd
pd.set_option('display.width',4000)
pd.set_option('max_colwidth',4000)
pd.set_option('max_rows',100)
pd.set_option('max_columns',200)

import numpy as np
from pathlib import Path
import sys
import datetime as dt

# import sklearn
# import matplotlib

import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
sys.path.insert(1,"../") # add dir with helper files

# save and load obj
from scripts.general_helpers import *



DATA = Path("../data")
CLEANED = DATA/"cleaned"
PLAY = Path("../data/play_by_play_data/regular_season")
five_all = pd.read_pickle(CLEANED/"fivethirtyeight_all.xz")

five_all['game_date'] = pd.to_datetime(five_all['game_date'])
five_pre = pd.read_pickle(CLEANED/"fivethirtyeight_pre.xz")

five_pre['game_date'] = pd.to_datetime(five_pre['game_date'])
games = pd.read_pickle(CLEANED/"games_basic_all.xz")
pbp_all = pd.read_pickle(CLEANED/"pbp_all.xz")

pbp_all['game_date'] = pd.to_datetime(pbp_all['game_date'])
#a `timeout` is `play_type` == `no_play`

pbp_pre = pd.read_pickle(CLEANED/"pbp_pre.xz")

pbp_pre['game_date'] = pd.to_datetime(pbp_pre['game_date'])
# can join to games
# has end of game / season info

fastr_all = pd.read_pickle(CLEANED/"fastr_all.xz")

fastr_all['game_date'] = pd.to_datetime(fastr_all['game_date']).dt.date
fastr_all['game_date'] = pd.to_datetime(fastr_all['game_date'])
fastr_pre = pd.read_pickle(CLEANED/"fastr_pre.xz")

fastr_pre['game_date'] = pd.to_datetime(fastr_pre['game_date']).dt.date
fastr_pre['game_date'] = pd.to_datetime(fastr_pre['game_date'])
fastr_standings = pd.read_pickle(CLEANED/"fastr_standings_all.xz")

merged_pbp_fastr = pbp_pre.merge(fastr_pre,
                                 how="outer",
                                 left_on=["game_id","home_team","away_team"],#"game_date"],
                                 right_on=["game_id","home_team","away_team"])#,#"game_date"],
                                 #indicator=True)
merged_pbp_fastr = merged_pbp_fastr.drop(columns=["game_date_x"])
merged_pbp_fastr.rename(columns={"game_date_y":"game_date"},inplace=True)

merged_pbp_fastr["game_date"] = pd.to_datetime(merged_pbp_fastr["game_date"]).dt.date
merged_pbp_fastr["game_date"] = pd.to_datetime(merged_pbp_fastr["game_date"])
