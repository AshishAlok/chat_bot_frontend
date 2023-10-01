import streamlit as st
import requests
server_url = 'http://localhost:8000/query'  # Replace with your server's URL

# -------------------------------------------------------------------------------
def get_server_response(query):
    server_url = 'http://localhost:8000/query'  # Replace with your server's URL
    data = {'query': query}
    response = requests.post(server_url, json=data)
    if response.status_code == 200:
        return response.json().get('reply', 'Error: No reply from the server')
    else:
        return f"Error: Server returned status code {response.status_code}"

# Streamlit app header and instructions
st.title("AI Chatbot ")
st.markdown("Instructions:")
st.write("1. Type your query in the text area.")
st.write("2. Click the 'Send icon' button to get a response from the chatbot.")

# with st.chat_message(name = "user"):
#     st.write("Hello ")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Any query ?")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role":"user","content": prompt})
    
    # response = generate_response(prompt)
    response = get_server_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role":"assistant","content":response})
