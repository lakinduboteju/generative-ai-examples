from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage


hello_prompt_template = ChatPromptTemplate.from_messages([
    SystemMessage("Respond only in English and use emojis excessively"),
    HumanMessagePromptTemplate.from_template("Hello, I'm {name}. How are you today?"),
])
