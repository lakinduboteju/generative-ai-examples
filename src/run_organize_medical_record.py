import os
import json

from langchain_core.output_parsers import StrOutputParser
from langchain_core.callbacks import StdOutCallbackHandler

from common.llms import LLMModel, LLMCredentials, create_llm_model
from organize_medical_record.prompt_templates import prompt_template_to_organize_a_medical_record_into_json
from common.file_utils import read_file_as_string


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
    temperature=0,
    max_output_tokens=1024
)

chain = prompt_template_to_organize_a_medical_record_into_json() | llm_model | StrOutputParser()

output = chain.invoke(
    {
        # Medical history note was taken from : https://www.youtube.com/watch?v=BmQppGzk78A
        "medical_history": read_file_as_string(os.path.join("/assets", "medical_history_note.txt")),
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