
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
st.selectbox('Select a response', response["choices"])
st.text('Source:')
st.text('[OpenAI](https://openai.com/)')
st.text('[GPT-3](https://openai.com/blog/gpt-3/)')
st.text('[Inside Labs](https://insidelibrary.weebly.com/)')
st.text('[GPT-3](https://openai.com/blog/gpt-3/)')
st.text('[Inside Labs](https://insidelibrary.weebly.com/)')
st.text('[GPT-3](https://openai.com/blog/gpt-3/)')
st.text('[Inside Labs](https://insidelibrary.weebly.com/)')
st.text('[GPT-3](https://openai.com/blog/gpt-3/)')
st.text('[Inside Labs](https://insidelibrary.weebly.com/)')
st.text('[GPT-3](https://openai.com/blog/gpt-3/)')
st.text('[Inside Labs](https://insidelibrary.weebly.com/)')
st.text('[GPT-3](https://openai.com/blog/gpt-3/)')
st.text('[Inside Labs](https://insidelibrary.weebly.com/)')
st.text('[GPT-3](https://openai.com/blog/gpt-3/)')
st.text('[Inside Labs](https://insidelibrary.weebly.com/)')
st.text('[GPT-3](https://openai.com/blog/gpt-3/)')
st.text('[Inside Labs](https://insidelibrary.weebly.com/)')
st.text('[GPT-3](https://openai.com/blog/gpt-3/)')
st.text('[Inside Labs](https://insidelibrary.weebly.com/)')
st.text('[GPT-3](https://openai.com/blog/gpt-3/)')
st.text('[Inside Labs](https://insidelibrary.


if st.button('Generate'):
    st.markdown(response["choices"][0]["text"]*1)


