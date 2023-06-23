import streamlit as st
from st_on_hover_tabs import on_hover_tabs

import sqlite3
import pandas as pd
from streamlit_tags import *
import html2text
import datetime

from pages.dash import dashboard
from pages.app2 import app2

st.set_page_config(layout="wide", page_title="Q & A app", initial_sidebar_state="expanded")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
# if allowed, else; st.markdown('<style>' + open('./style_sidebar.css').read() + '</style>', unsafe_allow_html=True)
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)


with st.sidebar: # ADD A TOGGLEABLE SIDE BAR(through st.states); ADD A CALENDER EMBED
    tabs = on_hover_tabs(tabName=['Dashboard', 'Tagger'], 
                            iconName=['dashboard', 'assignment'],
                            styles = {'navtab': {'background-color':'#111',
                                                'color': '#818181',
                                                'font-size': '18px',
                                                'transition': '.05s',
                                                'white-space': 'nowrap',
                                                'text-transform': 'uppercase'},
                                    'iconStyle':{'position':'fixed',
                                                'left':'7.5px',
                                                'text-align': 'left'},
                                    'tabStyle' : {'list-style-type': 'none',
                                                    'margin-bottom': '30px',
                                                    'padding-left': '30px'}},
                            key="1", default_choice=0)


if tabs=="Dashboard":
    dashboard()

elif tabs=="Tagger":
    app2()

else:
    st.write("Pick a Valid Tab Please!")


_ = """PARAMETER DEF/DESCRIPTION ;;;;; ADD A TOGGLEABLE BUTTON ON THE BOTTOM OF THE NAVBAR that IS SEPARATE FROM THE NAVBAR (BLOCK) THAT DISABLES THE JS SLIDING/EXTENDING
tabName: This is the name of the tab
iconName: This is the name of the icon you wish to use in the sidebar
styles: Borrowed an implementation from the wonderful Victoryhb implementation. It just has four html elements with css styles which you can adapt as you would if you were in a css file. It employs styles from glamor which allows for other implementations like hover, active etc as demonstrated below. Now you can create your own navigation bar and customize the tabs to meet the specs of your custom tab.
    'navtab' which is the div container that contains the tabs
    'tabOptionsStyle' which is the span container that contains the icons and tabName
    'iconStyle' which is the icon tag that contains the icons
    'tabStyle' which is the list contains the tabName
"""