import streamlit as st
import opendal
import pandas as pd

op = opendal.Operator("fs", root="/tmp")

entries = [(entry.path, op.stat(str(entry))) for entry in op.list("/")]

df = pd.DataFrame([(path, str(entry.mode), entry.content_length) for (path, entry) in entries], columns=("filename", "mode", "size"))

st.write('Hello, the following table is files in /tmp!')
# st.table(df)
st.dataframe(df)
