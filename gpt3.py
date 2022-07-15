import openai
import streamlit as st
openai.api_key = st.secrets["SECRET_KEY"]


st.title('The Stoned Ape')

st.text('This is an experiment of prompt designing by using GPT-3, a neural network trained and hosted by OpenAI.')
prompt_text = st.text_input(label="Ask something...", value="Add here few words")
response = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    prompt=prompt_text,
    max_tokens=500,
    prompt="Expand the blog section in to a detailed professional , witty and clever explanation.\n\n {}".format(prompt_text),
    temperature=0.7,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
st.text('Output:')
st.text(response["choices"][0]["text"])

