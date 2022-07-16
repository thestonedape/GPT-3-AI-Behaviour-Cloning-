import openai
import streamlit as st
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Cutive+Mono&display=swap" rel="stylesheet');

			html, body, [class*="css"]  {
			font-family: 'Cutive Mono', monospace;
            color: white;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=1)


openai.api_key = st.secrets["SECRET_KEY"]

st.title('The Stoned Ape')

st.markdown('This is an experiment of prompt designing by using GPT-3(a transformer model), a neural network trained and hosted by OpenAI.', unsafe_allow_html=0)
st.markdown('tips: Try to ask specific detaied questions, like "What is the meaning of "the" in "the meaning of life"?', unsafe_allow_html=0)
prompt_text = st.text_input(label="Input" , value="Ask me anything!")
response = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    max_tokens=500,
    prompt="Expand the prompt text in to a detailed philosophical and creative explanation.\n\n {}".format(prompt_text),
    temperature=0.8,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
st.text('Output:')
#on click, the response is displayed

if st.button('Generate'):
    st.markdown(response["choices"][0]["text"])

