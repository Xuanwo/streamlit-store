import streamlit as st
import opendal
import pandas as pd
import asyncio
import io
from urllib.parse import urlparse

async def main():
    st.write("Please input a csv file url here")
    st.write("for example: `https://repo.databend.rs/dataset/stateful/ontime_2006_200.csv`")

    file_url = st.text_input('File URL', placeholder="https://repo.databend.rs/dataset/stateful/ontime_2006_200.csv")
    if file_url:
        url = urlparse(file_url)
        op = opendal.AsyncOperator("http", endpoint=f"{url.scheme}://{url.netloc}")
        bs = await op.read(url.path)
        df = pd.read_csv(io.BytesIO(bs))
        st.dataframe(df)

asyncio.run(main())
