import openai
import streamlit as st
streamlit_style = """
			<style>
            @import url('https://fonts.googleapis.com/css2?family=Cutive+Mono&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Cutive Mono', monospace;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html = True)

openai.api_key = st.secrets["SECRET_KEY"]
#toggle button to witch between dark and light mode
st.sidebar.title("Style")
style = st.sidebar.selectbox("Select a style", ["Dark", "Light"])
if style == "Dark":
    st.markdown("""
            <style>
            body {
            background-color: #1a1a1a;
            color: white;
            }
            </style>
            """, unsafe_allow_html = True)
elif style == "Light":
    st.markdown("""
            <style>
            body {
            background-color: #f0f0f0;
            color: black;
            }
            </style>
            """, unsafe_allow_html = True)
            


        
st.title('The Stoned Ape')
st.caption('Backed by Inside Labs')

st.markdown('This is an experiment of prompt designing by using GPT-3(A Transformer based model), a neural network trained and hosted by OpenAI.')
st.caption('Tips: Try to ask specific detaied questions, like "Who are you?')
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
    st.markdown(response["choices"][0]["text"]*1)

