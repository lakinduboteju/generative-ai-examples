import os
import json
from config import config
from file_utils import read_file_as_string
from enum import Enum
from langchain_openai import ChatOpenAI
from langchain_aws import ChatBedrock
from amazon_bedrock import AmazonBedrockModel
from langchain_core.callbacks import StdOutCallbackHandler
from prompt_templates import prompt_template_to_organize_a_medical_record_into_json
from langchain_core.output_parsers import StrOutputParser


class LLMModel(Enum):
    OPENAI_GPT4O = 0
    CLAUDE_3_5_SONNET = 1
    LLAMA_3 = 2
    MISTRAL = 3


# LLM model to use, and its parameters
llm_model = LLMModel.MISTRAL
temperature = 1
max_output_tokens = 1024

# Credentials
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_org_id = os.getenv("OPENAI_ORG_ID")
aws_profile = os.getenv("AWS_PROFILE")

# Create the LLM model
match llm_model:
    case LLMModel.OPENAI_GPT4O:
        llm_model = ChatOpenAI(
            model="gpt-4o",
            max_tokens=max_output_tokens,
            temperature=temperature,
            openai_api_key=openai_api_key,
            openai_organization=openai_org_id,
        )

    case LLMModel.CLAUDE_3_5_SONNET:
        params = dict(
            region_name=config.amazon_bedrock.region,
            model_id=str(AmazonBedrockModel.CLAUDE_3_5_SONNET),
            model_kwargs=dict(
                temperature=temperature,
                max_tokens=max_output_tokens,
            ),
        )
        if aws_profile:
            params["credentials_profile_name"] = aws_profile

        llm_model = ChatBedrock(**params)

    case LLMModel.LLAMA_3:
        params = dict(
            region_name=config.amazon_bedrock.region,
            model_id=str(AmazonBedrockModel.LLAMA_3_70B),
            model_kwargs=dict(
                temperature=temperature,
                max_gen_len=max_output_tokens,
            ),
        )
        if aws_profile:
            params["credentials_profile_name"] = aws_profile

        llm_model = ChatBedrock(**params)

    case LLMModel.MISTRAL:
        params = dict(
            region_name=config.amazon_bedrock.region,
            model_id=str(AmazonBedrockModel.MISTRAL_7B),
            model_kwargs=dict(
                temperature=temperature,
                max_tokens=max_output_tokens,
            ),
        )
        if aws_profile:
            params["credentials_profile_name"] = aws_profile

        llm_model = ChatBedrock(**params)

chain = prompt_template_to_organize_a_medical_record_into_json() | llm_model | StrOutputParser()

output = chain.invoke(
    {
        # Medical history note was taken from : https://www.youtube.com/watch?v=BmQppGzk78A
        "medical_history": read_file_as_string(os.path.join("inputs", "medical_history_note.txt")),
    },
    {
        "callbacks": [StdOutCallbackHandler()],
    },
)

output = json.loads(output)

print(json.dumps(
    output,
    indent=2
))
