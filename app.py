import streamlit as st
import json
import marqo

st.set_page_config(
    page_title="E-Commerce Inventory Search",
    initial_sidebar_state="expanded",
)

header = st.container()
dataset = st.container()
text_search = st.container()
image_search = st.container()
search = st.container()

endpoint = "http://127.0.0.1:8882"
hidden = []
top_k = 10

with header:
    st.title('E-Commerce Inventory Tensor Search - Powered By Marqo!')
    st.write("Marqo is an open-source tensor search framework for the development of multi-modal search solutions. "
             " Solutions may be deployed locally, or on the cloud. In this demo, Marqo is used to index and search "
             "thorugh inventory data.")

with dataset:
    st.subheader('Dataset')
    st.markdown(
        "Find the e-commerce dataset uses in this demo "
        "[here](https://github.com/algolia/datasets/tree/master/ecommerce).")
    f = open('data/data.json', encoding='utf-8')
    data = json.load(f)
    st.json(data[0:3])

with search:
    search_option = st.selectbox('Select your preferred search type', ('Text Search', 'Image Search'))
    if search_option == 'Text Search':
        st.header('Text Search')
        if "endpoint" not in hidden:
            endpoint = st.text_input("Endpoint", endpoint)

        query = st.text_input("Enter query", placeholder="SanDisk")

        if "top_k" not in hidden:
            top_k = st.slider("Max results", 1, top_k, int(top_k / 2))

        button = st.button("Search")

        if button:
            mq = marqo.Client(url=endpoint)
            results = mq.index("inventory").search(query)
            st.write(results)

    elif search_option == 'Image Search':
        st.header('Image Search')
        if "endpoint" not in hidden:
            endpoint = st.text_input("Endpoint", endpoint)

        file = st.file_uploader("Upload image")
        # encode file -- Image search not functional

        if "top_k" not in hidden:
            top_k = st.slider("Results", 1, top_k, int(top_k / 2))

        button = st.button("Search")

        if button:
            mq = marqo.Client(url=endpoint)
            results = mq.index("inventory").search(file)
            st.write(results)



