import streamlit as st
import csv

st.set_page_config(layout="wide", page_title="Q & A app")

labels = ["safe","unsafe","social","educational"]

def update_count(count):
  with open("counter", "w") as f:
    f.truncate()
    f.write(f"{count}")

def write_label(w,label,notes,count):
  with open('labeled-dataset.csv','a') as fd:
    fd.write(f"{w},{label},{notes},{count}\n")

def insert_button(columns,labels,i,label_buttons):
  with columns[i]:
    b = st.button(l)
    label_buttons.append(b)

import pandas as pd
import sqlite3

conn = sqlite3.connect("satsuite.sqlite", isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
db_df = pd.read_sql_query("SELECT * FROM questionDetails WHERE section='Math'", conn)
column_ID=[]
for i in db_df.columns:
    column_ID.append(i)

row_data=[]
tick=0
for row,index in db_df.iterrows():
    # Process the row data
    # print(index)
    print(row)
    for i in range(len(column_ID)):
        # print(db_df.at[row, column_ID[i]])
        row_data.append(db_df.at[row, column_ID[i]])
        #item_id,section,prompt,body,passage_directions,passage_attribution,passage_body,style,correct_choice,rationale,a,b,c,d
    if tick==0:
        break
    else:
        tick=tick+1

st.title("Q & A app")
    

row2_1, row2_2, row2_3, row2_4 = st.columns((0.75, 2.25, 1, 1))

# row_data is an array that collects data from the database in repeatable chains of 14 (columns)
for i in range(len(row_data) // 14):
  #item_id,section,prompt,body,passage_directions,passage_attribution,passage_body,style,correct_choice,rationale,a,b,c,d
  with row2_1:
    st.markdown(f"**Item_id:** {row_data[(i*14)+0]}", unsafe_allow_html=True)
    st.markdown(f"**Section:** {row_data[(i*14)+1]}", unsafe_allow_html=True)

  with row2_2:
    st.markdown(f"**prompt:** {row_data[(i*14)+2]}", unsafe_allow_html=True)
    st.markdown(f"**body:** {row_data[(i*14)+3]}", unsafe_allow_html=True)

  with row2_3:
    st.markdown(f"**passage_directions:** {row_data[(i*14)+4]}", unsafe_allow_html=True)
    st.markdown(f"**passage_attribution:** {row_data[(i*14)+5]}", unsafe_allow_html=True)
    st.markdown(f"**passage_body:** {row_data[(i*14)+6]}", unsafe_allow_html=True)
    st.markdown(f"**style:** {row_data[(i*14)+7]}", unsafe_allow_html=True)

  with row2_4:
    st.markdown(f"**correct_choice:** {row_data[(i*14)+8]}", unsafe_allow_html=True)
    st.markdown(f"**rationale:** {row_data[(i*14)+9]}", unsafe_allow_html=True)
    st.markdown(f"**a:** {row_data[(i*14)+10]}", unsafe_allow_html=True)
    st.markdown(f"**b:** {row_data[(i*14)+11]}", unsafe_allow_html=True)
    st.markdown(f"**c:** {row_data[(i*14)+12]}", unsafe_allow_html=True)
    st.markdown(f"**d:** {row_data[(i*14)+13]}", unsafe_allow_html=True)
  
  "\n\n\n\n\n"
  
st.button("_")



with open("counter", "r") as f:
  count = int(f.readline())

websites,label_buttons = [],[]

with open('websites.csv', newline='') as csvfile:
  for temp in csv.reader(csvfile):
    websites.append(temp[0])
  websites.append("DONE")

if count<len(websites):
  w = websites[count]
  if w=="DONE":
      st.balloons()
      if st.button("Reset"):
        update_count(1) 
  else:    
    st.markdown(f'## [{w}]({w})')
    columns = st.columns(len(labels))

    for i,l in enumerate(labels):
        insert_button(columns,labels,i,label_buttons)

    notes=st.text_input("Notes")

    for i,b in enumerate(label_buttons):
      if b:
        write_label(websites[count-1],labels[i],notes,count-1)
        count += 1
        update_count(count)
