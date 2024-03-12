import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')

list_of_states = sorted(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title("India's Data Visuliazation")

selected_state = st.sidebar.selectbox('Select State',list_of_states)

primary = st.sidebar.selectbox("Select Primary parameter", sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select Secondary parameter", sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represents primary parameter')
    st.text('color represents secondary parameter')
    if selected_state == 'Overall India':
        # plot for india
        import plotly.express as px
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",size=primary, color=secondary,
                                color_continuous_scale=px.colors.cyclical.IceFire, size_max=15,
                                zoom=4, mapbox_style='carto-positron',hover_name='District',
                                height=500, width=800)
        st.plotly_chart(fig)
    else:
        # plot for state
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary,
                                color_continuous_scale=px.colors.cyclical.IceFire, size_max=15,
                                zoom=4, mapbox_style='carto-positron', hover_name='District',
                                height=500, width=800)
        st.plotly_chart(fig)