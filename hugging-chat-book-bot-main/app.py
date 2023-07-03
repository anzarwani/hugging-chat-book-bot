import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

from dotenv import load_dotenv
import os

load_dotenv()

# Access the environment variables
#email = os.getenv('EMAIL')
#passwd = os.getenv('PASSWORD')

email = st.secrets["email"]
passwd = st.secrets["passwd"]

sign = Login(email, passwd)
cookies = sign.login()

# Save cookies to usercookies/<email>.json
#sign.saveCookies()

sign.saveCookiesToDir()

st.set_page_config(page_title="Book Recommendation Bot - An LLM-powered Streamlit bot")


# header

st.header("Hugging Chat - Book Recommendation Bot")

st.divider()
moods = st.multiselect(
    'Select the mood',
    ['Happy', 'Sad', 'Suspenseful', 'Scary', 'Romantic', 
     'Adventure', 'Mystical', 'Funny', 'Inspirational', 
     'Dramatic', 'Thoughtful', 'Thrilling', 
     'Mysterious', 'Whimsical', 'Dark', "random"])

st.write("")

num_of_recom = st.selectbox(
    'Select number of recommendations',
    ('5', '10', '15'))

st.write("")

selected_moods = ' '.join(moods)

query = "Suggest " + num_of_recom + "books based on the mood " + selected_moods + ". Just give a list of books, no details."

def recom(query):
    
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    response = chatbot.chat(query)
    
    return response

gen = st.button("Generate")

if gen:
    try:
        bot_response = recom(query)
        st.text(bot_response)
    except:
        st.subheader("Please Try Again")
