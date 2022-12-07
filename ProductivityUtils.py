import streamlit as st
import datetime
import asyncio
from time import sleep
from threading import Thread

async def current_time(t: st._DeltaGenerator):
    while True:
        st.title(datetime.datetime.now().strftime("%I:%M %p"))
        await asyncio.sleep(1)
        st.experimental_rerun()

