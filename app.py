import streamlit as st
Import fourthdown

OPTIONS = { "Team Decisions": teamdecisions,
           "Best Decisions": bestdecisions,
           "Worst Decisions": worsdecisions,
           "4th Down Ruling Teams": rulingteam
          }

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(OPTIONS.keys()))
OPTION = OPTIONS[selection]
OPTION.app()
