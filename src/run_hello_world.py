import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.callbacks import StdOutCallbackHandler

from common.llms import LLMModel, LLMCredentials, create_llm_model
from hello_world.prompt_templates import hello_prompt_template


# Credentials
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_org_id = os.getenv("OPENAI_ORG_ID")
aws_profile = os.getenv("AWS_PROFILE")

# Create the LLM model
llm_model = create_llm_model(
    LLMModel.MISTRAL,
    LLMCredentials(
        openai_api_key,
        openai_org_id,
        aws_profile
    ),
    temperature=1,
    max_output_tokens=100
)

# Invoking hello prompt on the LLM model and parse the output as a string
chain = hello_prompt_template | llm_model | StrOutputParser()

output = chain.invoke(
    {
        "name": "Lakindu",
    },
    {
        # Callback to print the events to the console
        "callbacks": [StdOutCallbackHandler()],
    },
)

print(output)
