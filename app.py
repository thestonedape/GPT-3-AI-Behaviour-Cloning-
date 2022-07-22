
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

#select the response
if st.button('Select Response'):
    st.text(response.choices[0].text)
    st.text(response.choices[1].text)
    st.text(response.choices[2].text)
    st.text(response.choices[3].text)
    st.text(response.choices[4].text)
    st.text(response.choices[5].text)
    st.text(response.choices[6].text)
    st.text(response.choices[7].text)
    st.text(response.choices[8].text)
    st.text(response.choices[9].text)
    st.text(response.choices[10].text)
    st.text(response.choices[11].text)
    st.text(response.choices[12].text)
    st.text(response.choices[13].text)
    st.text(response.choices[14].text)
    st.text(response.choices[15].text)
    st.text(response.choices[16].text)
    st.text(response.choices[17].text)
    st.text(response.choices[18].text)
    st.text(response.choices[19].text)
    st.text(response.choices[20].text)
    st.text(response.choices[21].text)
    st.text(response.choices[22].text)
    st.text(response.choices[23].text)
    st.text(response.choices[24].text)
    st.text(response.choices[25].text)
    st.text(response.choices[26].text)
    st.text(response.choices[27].text)
    st.text(response.choices[28].text)
    st.text(response.choices[29].text)
    st.text(response.choices[30].text)
    st.text(response.choices[31].text)
    st.text(response.choices[32].text)
    st.text


if st.button('Generate'):
    st.markdown(response["choices"][0]["text"]*1)
    



