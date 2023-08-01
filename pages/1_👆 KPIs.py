import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Welcome to KPIs Page 👆')
st.markdown(
    """
    This page has multiple tabs for the users to see the data. All of the visualizations are interactive.
    """
    )

def main():
    tab1, tab2, tab3 = st.tabs(['KPIs', 'Heatmap Vertical', 'Heatmap Horizontal'])

    with tab1:   # KPI page
        ### Generating random df
        chart_data1 = pd.DataFrame(
            np.random.randn(20, 2),
            columns=['2022', '2023'])
        chart_data2 = pd.DataFrame(
            np.random.randn(20, 2),
            columns=['2022', '2023'])
        chart_data3 = pd.DataFrame( 
            np.random.randn(20, 2),
            columns=['2022', '2023'])
        
        rate1 = chart_data1['2023'].iloc[-1]
        rate2 = chart_data2['2023'].iloc[-1]
        rate3 = chart_data3['2023'].iloc[-1]
        
        ### setting up tab
        
        st.header('KPIs')
        kpi_row1 = st.columns(3)
        kpi_row1[0].metric(label='Rate1', value=f'{rate1:.2f}%')
        kpi_row1[1].metric(label='Rate2', value=f'{rate2:.2f}%')
        kpi_row1[2].metric(label='Rate3', value=f'{rate3:.2f}%')

        kpi_row2 = st.columns(3)
        kpi_row2[0].line_chart(chart_data1)
        kpi_row2[1].line_chart(chart_data2)
        kpi_row2[2].line_chart(chart_data3)

        st.caption('Please note all these data are fake!')

    with tab2:   # Heatmap page

        st.markdown("This a vertical heatmap is changes made WoW")
        ### Generating random df
        x = ['Corporate', 'Team A', 'Team B', 'Team C', 'Team D']
        y = [
            'Total KPI', 
            'KPI 1 - A', 'KPI 1 - B', 'KPI 1 - C', 
            'KPI 2 - A', 'KPI 2 - B', 'KPI 2 - C', 
            'KPI 3 - A', 'KPI 3 - B', 'KPI 3 - C',
            'KPI 4 - A', 'KPI 4 - B', 'KPI 4 - C']
            
        
        num_cols = len(x)
        num_rows = len(y)

        np.random.seed(42)  # Set a seed for reproducibility
        data = np.random.randint(-30, 30, size=(num_rows, num_cols))

        df = pd.DataFrame(data, columns=x, index=y)
        z_values = df.values

        # Plot using Plotly Express
        fig = px.imshow(
            z_values, x=x, y=y, 
            labels={'y': 'Division', 'x': 'Metrics'},
            color_continuous_scale='RdBu', 
            aspect='equal',
            text_auto=True, 
            zmin=-10, zmax=10,
            height=800
            )

        fig.update_xaxes(side="top")
        
        # fig.update_yaxes(ticksuffix = "  ")

        st.plotly_chart(fig, theme=None)

        st.caption('Please note all these data are fake!')

    with tab3:   # Heatmap page

        st.markdown("This horizontal heatmap is changes made WoW")
        ### Generating random df
        y = ['Corporate', 'Team A', 'Team B', 'Team C', 'Team D']
        x = [
            'Total KPI', 
            'KPI 1 - A', 'KPI 1 - B', 'KPI 1 - C', 
            'KPI 2 - A', 'KPI 2 - B', 'KPI 2 - C', 
            'KPI 3 - A', 'KPI 3 - B', 'KPI 3 - C',
            'KPI 4 - A', 'KPI 4 - B', 'KPI 4 - C']
            
        
        num_cols = len(x)
        num_rows = len(y)

        np.random.seed(42)  # Set a seed for reproducibility
        data = np.random.randint(-30, 30, size=(num_rows, num_cols))

        df = pd.DataFrame(data, columns=x, index=y)
        z_values = df.values

        # Plot using Plotly Express
        fig = px.imshow(
            z_values, x=x, y=y, 
            labels={'y': 'Division', 'x': 'Metrics'},
            color_continuous_scale='RdBu', 
            aspect='equal',
            text_auto=True, 
            zmin=-10, zmax=10
            # height=800
            )

        fig.update_xaxes(side="top")
        
        # fig.update_yaxes(ticksuffix = "  ")

        st.plotly_chart(fig, theme=None)

        st.caption('Please note all these data are fake!')
main()
