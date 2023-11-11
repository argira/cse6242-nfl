import streamlit as st
import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as sm
import altair as alt
from load_data import data_prep
from load_data import team_colors
from scipy import stats
from helpers import pearsonr_ci


def app():
  st.header("To do or not to do a 4th down conversion")
  df = data_prep()
  team_colors = teeam_colors()
  
  
  
