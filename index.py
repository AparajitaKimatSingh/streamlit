import streamlit as st
import pandas as pd

# Load the dataset from a CSV file

def load_data():
   


    #csv_file = 'your_dataset.csv'
    return pd.read_csv('blood.csv')
    st.write("Loaded Data:")
    st.write(df)


def main():
    st.markdown("<h1 style='text-align: center; color: #9B59B6;'>Select Name from Dataset</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<h2 style='color: #008080;'>Dataset</h2>", unsafe_allow_html=True)
    show_dataset = st.sidebar.checkbox("Show Dataset")
    df = None

    if show_dataset:
    # Load the dataset
        df = load_data()
     # Display the dataset in the sidebar
        st.sidebar.subheader("Loaded Data:")
        st.sidebar.write(df)
      # Initialize selected_data outside the block
    selected_data = pd.DataFrame()
    # Create selectboxes for name
    selected_name = st.selectbox("Select your name:", df['Name'] if df is not None else [])
   

     # Submit button to trigger actions
    submitted = st.button("Submit") 
    if submitted and df is not None:

    # Filter the dataset based on the selected values
        selected_data = df[(df['Name'] == selected_name) ]

    # Display the filtered dataset
    st.write("Selected Data:")
    st.write(selected_data)

if __name__ == "__main__": 
    main()