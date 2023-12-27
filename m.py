from langchain.llms import Ollama
from langchain.prompts.chat import ChatPromptTemplate

ollama = Ollama(base_url='http://localhost:11434',
model="llama2")

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "good morning"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")
while True:
    print(ollama(input("")))
    print('Beep boop')
