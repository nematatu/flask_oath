import streamlit as st
import requests
import json

page=st.sidebar.selectbox('choose your page',['registration','list'])

if page=='registration':
    st.title('create page')
    with st.form(key='registration'):
        content:str=st.text_input('memo',max_chars=100)
        data={
            'content':content
        }
        submit_button=st.form_submit_button(label='regist')

        if submit_button:
            url='http://127.0.0.1:8000/memos'
            res=requests.post(
                url,
                data=json.dumps(data)
            )
            if res.status_code==200:
                st.success('success!')
            st.json(res.json())
elif page=='list':
    st.title('list page')
    res=requests.get('http://127.0.0.1:8000/memos')
    records=res.json()
    for record in records:
        st.subheader('・'+record.get('content'))