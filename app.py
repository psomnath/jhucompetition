import streamlit as st
st.set_page_config(layout="wide") 

if 'user' not in st.session_state:
    st.session_state['user'] = ''

if 'password' not in st.session_state:
    st.session_state['password'] = ''
    
if 'login_clicked' not in st.session_state:
    st.session_state['login_clicked'] = ''
    
def button_clicked(name):
    if name == 'login':
        st.session_state['user'] = 'somnath'
    elif name == 'logout':
        st.session_state['user'] = ''
    

with st.sidebar:
        
    st.title('Welcome')
    if st.session_state['user'] == '':
        st.write('please login')
        st.button("login", on_click = button_clicked, args = ('login',))
    else:
        st.write('Welcome :', st.session_state['user'] )
        st.button("logout", on_click = button_clicked, args = ('logout',))
        
        
    
    
col1,col2,col3 =  st.columns([1,2,1])
with col1:
    st.write('in first column')

with col2:
    st.write('in second column')

with col3:
    st.write('in third column')
