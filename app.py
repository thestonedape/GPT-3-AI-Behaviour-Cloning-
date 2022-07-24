
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

response0 = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    max_tokens=500,
    prompt="Expand the prompt text in to a detailed philosophical and creative explanation.\n\n {}".format(prompt_text),
    temperature=0.8,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

response1 = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    max_tokens=500,
    prompt="Expand the prompt text into a full chad response.\n\n {}".format(prompt_text),
    temperature=0.8,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
response2 = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    max_tokens=500,
    prompt="Expand the prompt text into a Playboy type of response.\n\n {}".format(prompt_text),
    temperature=0.8,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )    
response3 = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    max_tokens=500,
    prompt="Expand the prompt text into a funny, dank and roasting response.\n\n {}".format(prompt_text),
    temperature=0.8,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
response4 = openai.Completion.create(
    engine="davinci-instruct-beta-v3",
    max_tokens=500,
    prompt="Create a creative Poem with strict rhyme scheme for \n{}".format(prompt_text),
    temperature=0.8,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

st.text('Output:')

#sidebar
st.sidebar.title('Behavioral Cloning')
st.sidebar.text('Choose a behaviour to clone:')
response_type = st.sidebar.selectbox('Behaviour types', ['Default', 'Denk', 'CowBoy', 'Philosopher', 'Poet'])

if st.button('Generate'):
  if response_type == 'Default':
     st.markdown(response0.choices[0].text)
  elif response_type == 'Denk':
     st.markdown(response1.choices[0].text)
  elif response_type == 'CowBoy':
     st.markdown(response2.choices[0].text)
  elif response_type == 'Philosopher':
     st.markdown(response3.choices[0].text)
  elif response_type == 'Poet' :
     st.markdown(response4.choices[0].text)   
  else:
     st.markdown('Please select a behaviour to clone.')




