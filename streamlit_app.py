import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Sample data for the graphs
np.random.seed(42)
data = pd.DataFrame({'X': np.random.rand(10), 'Y': np.random.rand(10)})

chart_data1 = pd.DataFrame(
     np.random.randn(20, 2),
     columns=['2022', '2023'])
chart_data2 = pd.DataFrame(
     np.random.randn(20, 2),
     columns=['2022', '2023'])
chart_data3 = pd.DataFrame(
     np.random.randn(20, 2),
     columns=['2022', '2023'])

# Sample data for KPIs
osd_rate = chart_data1['2023'].iloc[-1]
warehouse_rate = chart_data2['2023'].iloc[-1]
street_rate = chart_data3['2023'].iloc[-1]
st.set_page_config(layout="wide")
# Create the Streamlit app
def main():
    tab1, tab2, tab3 = st.tabs(['Top', '123', 'adf'])

    

    with tab1:
        st.title('OSD Top KPIs')

        # First row - KPIs
        st.header('KPIs')
        kpi_row1 = st.columns(3)
        kpi_row1[0].metric(label='OSD Rate', value=f'{osd_rate:.2f}%')
        kpi_row1[1].metric(label='Warehouse Rate', value=f'{warehouse_rate:.2f}%')
        kpi_row1[2].metric(label='Street Rate', value=f'{street_rate:.2f}%')

        kpi_row2 = st.columns(3)
        kpi_row2[0].line_chart(chart_data1)
        kpi_row2[1].line_chart(chart_data2)
        kpi_row2[2].line_chart(chart_data3)

    with tab2:
        # Heat Map
        
        import plotly.express as px

        x = ['Team A', 'Team B', 'Team C']
        y = ['Game One', 'Game Two', 'Game Three']

        z = [[100, 30, 50],
            [100, 80, 60],
            [60, 40, 20]]

        z_text = [['Win', 'Lose', 'Win'],
                ['Lose', 'Lose', 'Win'],
                ['Win', 'Win', 'Lose']]

        fig = px.imshow(z, x=x, y=y, color_continuous_scale='RdBu', aspect="auto", text_auto=True, zmin=40, zmax=60)
        # fig.update_traces(text=z_text, texttemplate="%{text}")
        fig.update_xaxes(side="top")
        # fig.show()


        st.plotly_chart(fig, theme=None)






        # ax = sns.heatmap(heat_map, square=True)  # Plot heatmap using seaborn
        # fig = ax.get_figure()  # Create figure
        # st.write("Seaborn Heatmap")  # Show figure in Streamlit
        # st.pyplot(fig)

    with tab3:
        # Second row - Graphs
        st.header('Graphs')
        graph_row = st.columns(3)
        graph_row[0].plotly_chart(px.scatter(data, x='X', y='Y', title='Scatter Plot'))
        graph_row[1].plotly_chart(px.bar(data, x='X', y='Y', title='Bar Chart'))
        graph_row[2].plotly_chart(px.pie(data, names='X', values='Y', title='Pie Chart'))


if __name__ == '__main__':
    main()


import streamlit as st
import time

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")


