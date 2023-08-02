import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Welcome to Sample Dashboard Page 📊')
st.markdown(
    """
    This page has multiple tabs for the users to see the data. All of the visualizations are designed to be interactive.
    """
    )

def main():
    tab1, tab2, tab3 = st.tabs(['KPIs', 'Heatmap Vertical', 'Heatmap Horizontal'])
    
    def generate_data():
        chart_data1 = pd.DataFrame(
            np.random.randn(20, 2),
            columns=['2022', '2023'])
        chart_data2 = pd.DataFrame(
            np.random.randn(20, 2),
            columns=['2022', '2023'])
        chart_data3 = pd.DataFrame( 
            np.random.randn(20, 2),
            columns=['2022', '2023'])

        return chart_data1, chart_data2, chart_data3
    
    with tab1:   # KPI page
        ### Generating random df


        def tab1_display(chart_data1, chart_data2, chart_data3):
            rate1 = chart_data1['2023'].iloc[-1]
            rate2 = chart_data2['2023'].iloc[-1]
            rate3 = chart_data3['2023'].iloc[-1]
            
            ### setting up tab
            
            st.header('KPIs')
            kpi_row1 = st.columns(3)
            kpi_row1[0].metric(label='Rate1', value=f'{rate1:.2f}%', delta=str(round(chart_data1['2023'].iloc[-1]-chart_data1['2023'].iloc[-2],2))+'%')
            kpi_row1[1].metric(label='Rate2', value=f'{rate2:.2f}%', delta=str(round(chart_data2['2023'].iloc[-1]-chart_data2['2023'].iloc[-2],2))+'%')
            kpi_row1[2].metric(label='Rate3', value=f'{rate3:.2f}%', delta=str(round(chart_data3['2023'].iloc[-1]-chart_data3['2023'].iloc[-2],2))+'%')

            kpi_row2 = st.columns(3)
            # kpi_row2[0].line_chart(chart_data1)

            config = {'displayModeBar': False}


            chart_1 = px.line(chart_data1)
            chart_1.update_layout(xaxis_title=None, yaxis_title=None, height=350,legend=dict(orientation='h', yanchor='bottom', y=-0.38, xanchor='left', x=0))  
            
            chart_2 = px.line(chart_data2)
            chart_2.update_layout(xaxis_title=None, yaxis_title=None, height=350,legend=dict(orientation='h', yanchor='bottom', y=-0.38, xanchor='left', x=0))
            
            chart_3 = px.line(chart_data3)
            chart_3.update_layout(xaxis_title=None, yaxis_title=None, height=350,legend=dict(orientation='h', yanchor='bottom', y=-0.38, xanchor='left', x=0))


            kpi_row2[0].plotly_chart(chart_1, use_container_width=True, config=config)
            kpi_row2[1].plotly_chart(chart_2, use_container_width=True, config=config)
            kpi_row2[2].plotly_chart(chart_3, use_container_width=True, config=config)

            st.caption('Please note all these data are fake!')
        
        
        chart_data1, chart_data2, chart_data3 = generate_data()
        tab1_display(chart_data1, chart_data2, chart_data3)
        
        
        
      
        
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
