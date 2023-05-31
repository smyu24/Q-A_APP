import datetime
import sqlite3
import pandas as pd
from streamlit_tags import *
import streamlit as st
table_schema_1 = """
CREATE TABLE "UpdatedQuestionDetails" ("item_id" varchar(255), "section" varchar(255), "prompt" varchar(255), "body" varchar(255), "passage_directions" varchar(255), "passage_attribution" varchar(255), "passage_body" varchar(255), "style" varchar(255), "correct_choice" varchar(255), "rationale" varchar(255), "a" varchar(255), "b" varchar(255), "c" varchar(255), "d" varchar(255), "tags" varchar(255), "note" varchar(255), "issues" varchar(255), "datetime" varchar(255))
"""  # ADD QUESTION NUMBER; multiply that question number with 14 to get the correct sessionstate
table_schema_3 = """
CREATE TABLE "Tags_Primary" ("Per_topic_Main" varchar(255), "Per_topic_sub" varchar(255) , "ID" varchar(255))
"""
table_schema_4 = """
CREATE TABLE "Tags_Secondary" ("Math_Category" varchar(255), "Category_Two_Tags" varchar(255) , "ID" varchar(255))
"""
st.set_page_config(layout="wide", page_title="Q & A app")

conn = sqlite3.connect("satsuite.sqlite", isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

db_df = pd.read_sql_query(
    "SELECT * FROM questionDetails WHERE section='Math'", conn)

column_ID = []
for i in db_df.columns:
    column_ID.append(i)

row_data = []

# Initialization
if 'key' not in st.session_state:
    st.session_state.key = 0

last_page = len(db_df.index)

row1_1, row1_2, row1_3, row1_4 = st.columns((8, 1, 1, 1))
with row1_1:
    st.title("Q & A app")

with row1_2:
    prev = st.button("< Previous", key="prev", help="Regress By One Question")

with row1_3:
    next = st.button("Next >", key="next", help="Proceed By One Question")

with row1_4:
    pgNav = st.number_input("Page To Travel To", min_value=0, max_value=last_page, value=st.session_state.key, key="pageNav")
    saved = st.button("Save", key="save", help="Page Change Confirm")

if saved:
    st.session_state.key = pgNav

if next:  # and IS NOT AT THE END!!!
    if st.session_state.key + 1 > last_page:
        st.session_state.key = 0
    else:
        st.session_state.key += 1
if prev:  # AND IS NOT BELOW INDEX = 0
    if not st.session_state.key - 1 < 0:
        st.session_state.key -= 1

for i in range(14):
    row_data.append(db_df.at[st.session_state.key, column_ID[i]])

row2_1, row2_2, row2_3 = st.columns((0.75, 2.25, 2))

with row2_1:# row_data is an array that collects data from the database in repeatable chains of 14 (columns); # item_id,section,prompt,body,passage_directions,passage_attribution,passage_body,style,correct_choice,rationale,a,b,c,d
    st.markdown(f"**Item_id:** {row_data[0]}", unsafe_allow_html=True)
    st.markdown(f"**Section:** {row_data[1]}", unsafe_allow_html=True)
    st.markdown(
        f"**passage_directions:** {row_data[4]}", unsafe_allow_html=True)
    st.markdown(
        f"**passage_attribution:** {row_data[5]}", unsafe_allow_html=True)
    st.markdown(f"**passage_body:** {row_data[6]}", unsafe_allow_html=True)
    st.markdown(f"**style:** {row_data[7]}", unsafe_allow_html=True)

with row2_2:
    st.markdown(f"**prompt:** {row_data[2]}", unsafe_allow_html=True)
    st.markdown(f"**body:** {row_data[3]}", unsafe_allow_html=True)

with row2_3:
    cur.execute("SELECT item_id FROM UpdatedQuestionDetails WHERE item_id=:item_id", {'item_id': row_data[0]})
    tagged_status = cur.fetchall()

    cur.execute("SELECT tags FROM UpdatedQuestionDetails WHERE item_id=:item_id", {'item_id': row_data[0]})
    prev_tagged = cur.fetchall()
    st.write(prev_tagged)

    with st.form('ID', clear_on_submit=True):
        if len(tagged_status) != 0:
            st.write("This problem has already been tagged")

        cur.execute("SELECT Per_topic_Main, Per_topic_sub, ID FROM Tags_Primary")
        prim_query_tag = cur.fetchall()
        formattedTagger=[]
        for row in prim_query_tag:
            formattedTagger.append(f"{row[2]} - {row[1]} - {row[0]}")
        tags = st.multiselect('Category Tags', formattedTagger, key="tag")
        notes = st.text_area('Note')
        issue = st.radio('Issues?', ['No', 'Yes'], key="issues")
        if st.form_submit_button('Save'):
            tag2 = ', '.join(tags)
            cur.execute("SELECT item_id FROM UpdatedQuestionDetails WHERE item_id=:item_id", {'item_id': row_data[0]})
            select_statement = cur.fetchall()
            if len(select_statement) == 0:
                cur.execute("INSERT INTO UpdatedQuestionDetails (item_id,section,prompt,body,passage_directions,passage_attribution,passage_body,style,correct_choice,rationale,a,b,c,d,tags,note,issues,datetime) VALUES (:item_id,:section,:prompt,:body,:passage_directions,:passage_attribution,:passage_body,:style,:correct_choice,:rationale,:a,:b,:c,:d,:tags,:note,:issues,:datetime)",
                            {'item_id': row_data[0], 'section': row_data[1], 'prompt': row_data[2], 'body': row_data[3], 'passage_directions': row_data[4], 'passage_attribution': row_data[5], 'passage_body': row_data[6], 'style': row_data[7],
                             'correct_choice': row_data[8], 'rationale': row_data[9], 'a': row_data[10], 'b': row_data[11], 'c': row_data[12], 'd': row_data[13], 'tags': tag2, 'note': notes, 'issues': issue, 'datetime': datetime.datetime.now()})
            else: 
                cur.execute("UPDATE UpdatedQuestionDetails SET item_id=:item_id, section=:section, prompt=:prompt, body=:body,passage_directions=:passage_directions,passage_attribution=:passage_attribution,passage_body=:passage_body,style=:style,correct_choice=:correct_choice,rationale=:rationale,a=:a,b=:b,c=:c,d=:d,tags=:tags,note=:note,issues=:issues,datetime=:datetime",
                            {'item_id': row_data[0], 'section': row_data[1], 'prompt': row_data[2], 'body': row_data[3], 'passage_directions': row_data[4], 'passage_attribution': row_data[5], 'passage_body': row_data[6], 'style': row_data[7], 'correct_choice': row_data[8], 'rationale': row_data[9], 'a': row_data[10], 'b': row_data[11], 'c': row_data[12], 'd': row_data[13], 'tags': tag2, 'note': notes, 'issues': issue, 'datetime': datetime.datetime.now()})
            conn.commit()
            st.experimental_rerun()


row3_1, = st.columns((1))
with row3_1:
    st.markdown(f"**correct_choice:** {row_data[8]}", unsafe_allow_html=True)
    st.markdown(f"**rationale:** {row_data[9]}", unsafe_allow_html=True)
    st.markdown(f"**a:** {row_data[10]}", unsafe_allow_html=True)
    st.markdown(f"**b:** {row_data[11]}", unsafe_allow_html=True)
    st.markdown(f"**c:** {row_data[12]}", unsafe_allow_html=True)
    st.markdown(f"**d:** {row_data[13]}", unsafe_allow_html=True)

# TODO = "MAKE A REVERT TO ORIGINAL BUTTON; Create a db table. in it push db changes to it as modified version. make sure to keep in mind that if error, then call original version. Push everything from the problem, date of modification, notes, issues, time."
