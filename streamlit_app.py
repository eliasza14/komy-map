import streamlit as st
import geopandas

APP_TITLE= 'KOMMY MAP VISUALIZATION'
APP_SUB_TITLE='CMT PROOPTIKI 2022'

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)

    merge2= geopandas.read_file('periferies.json')
    st.write(merge2)

if __name__ == "__main__":
    main()