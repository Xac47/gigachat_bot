import streamlit as st

from gigachat_api import get_access_token, send_prompt

st.title('Chat bot')

if 'access_token' not in st.session_state:
    try:
        st.session_state.access_token = get_access_token()
        st.toast('Токен  получен !')
    except Exception as e:
        st.toast(f'Токен не получен ! {e}', icon='🚨')

if 'messages' not in st.session_state:
    st.session_state.messages = [{'role': 'ai', 'content': 'Ассаламу Алейкум, Сугар г1улакх ийши хьун вош?'}]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

if user_input := st.chat_input():
    st.chat_message('user').write(user_input)
    st.session_state.messages.append({'role': 'user', 'content': user_input})

    with st.spinner('В процессе...'):
        response = send_prompt(user_input, st.session_state.access_token)

        st.chat_message('ai').write(response)
        st.session_state.messages.append({'role': 'ai', 'content': response})
