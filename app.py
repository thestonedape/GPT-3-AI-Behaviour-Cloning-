
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
#text on the bottom position of the page







        
st.title('The Stoned Ape')
st.caption('Still in development.')
st.caption('Backed by [Inside Labs](https://insidelibrary.weebly.com/)')

st.markdown('This is an experiment of prompt designing by using GPT-3(A Transformer based model), a neural network trained and hosted by OpenAI.')
st.caption('Tips: Try to ask specific detaied questions, like "Who are you?"')
prompt_text = st.text_input(label="Input" , value="Ask me anything!")
response1 = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    max_tokens=500,
    prompt="Expand the prompt text in to a creative chad and dank manner.\n\n {}".format(prompt_text),
    temperature=0.8,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
response2 = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    max_tokens=500,
    prompt="Expand the prompt text Playboy response.\n\n {}".format(prompt_text),
    temperature=0.8,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )    
response3 = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    max_tokens=500,
    prompt="Expand the prompt text funny Dank and roasting response.\n\n {}".format(prompt_text),
    temperature=0.8,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

st.text('Output:')


option = st.selectbox(
     'Choose the behaviour of Stoned Ape.',
     ('Chad', 'PlayBoy', 'Denk'))

if st.button('Generate'):

 if option == 'Chad':
    st.text('How u doin?')
    st.markdown(response1["choices"][0]["text"]*1)

 if option == 'PlayBoy':
    st.text('Yo!!')
    st.markdown(response2["choices"][0]["text"]*1)

 if option == 'Denk':
    st.text('Yo!!')
    st.markdown(response2["choices"][0]["text"]*1)






