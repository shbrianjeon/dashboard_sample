import streamlit as st
import pandas as pd
import numpy as np


st.title('Welcome to Data Entry Page ⌨️')
st.markdown(
    """
    Below is an editable table - editable columns have a mark on the left side of the column header. Hover on the column header for more information.

    You can also copy and paste the table values (and vice versa) to other software, such as Excel and Google Sheet. Convenient, right?
    """
    )


df = pd.DataFrame(
    [
       {"item": "product 1", "rating": 4, "bought": True, "sales": 300, "other note":"We are okay for now..."},
       {"item": "product 2", "rating": 5, "bought": False, "sales": 730, "other note":"We are okay for now..."},
       {"item": "product 3", "rating": 3, "bought": True, "sales": 1200, "other note":"Order more of this!"},
   ]
)

st.data_editor(
    df, 
    hide_index=True,
    column_config={
        'item': st.column_config.TextColumn(
            disabled=True,
            help="You can disable edits for columns too!"
            ),
        
        'rating': st.column_config.NumberColumn(
            help="Go ahead and change the rating!"
            ),
        
        'bought': st.column_config.CheckboxColumn(
            help="To check or to be unchecked?"
            ),
        
        'other note': st.column_config.SelectboxColumn(
            options=["Order more of this!", "We are okay for now..."],
            help="Doubleclick to look at options!"
            ),
        
        "sales": st.column_config.ProgressColumn(
            "Sales volume",
            help="The sales volume in USD",
            format="$%f",
            min_value=0,
            max_value=1000,
            ),
    
    },
    )

st.caption('')
