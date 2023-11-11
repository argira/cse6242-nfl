import numpy as np
from pathlib import Path
import sys
import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

def data_prep():
  DATA = Path("../data/training")
  CLEANED = DATA/"cleaned"
  #team_colors = pd.read_csv(DATA/"nflfastr/teamcolors.csv")
  pbp = pd.read_pickle(CLEANED/"pbp_all.xz")
  
  #identify real life data to load from another source
  
  
  return pbp
@st.cache

def team_colors():
  DATA = Path("../data/training")
  CLEANED = DATA/"cleaned"
  team_colors = pd.read_csv(DATA/"nflfastr/teamcolors.csv")
  
  return team_colors
@st.cache
