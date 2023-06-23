import sqlite3
import pandas as pd
from streamlit_tags import *
import html2text
import datetime

conn = sqlite3.connect(
        "./satsuite.sqlite", isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

def dashboard():
    @st.cache_data(show_spinner="Fetching data...")
    def db_read():
        db_df = pd.read_sql_query(
            sql="SELECT * FROM UpdatedQuestionDetails", con=conn)
        return db_df
    st.dataframe(db_read())
    
    # df.loc[(df['make']=make_choice) & (df['year']=year_choice) & (df['model']= model_choice) & (df[engine]=engine_choice)]

    # oh so like sorting per category tag? MAKE A DASHBOARD THAT LETS YOU SORT BY CATEGORY; filtering function

    
    return
