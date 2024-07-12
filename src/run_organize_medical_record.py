import os
import json

from langchain_core.callbacks import StdOutCallbackHandler
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

from common.llms import LLMModel, LLMCredentials, create_llm_model
from organize_medical_record.prompt_templates import prompt_template_to_organize_a_medical_record
from common.file_utils import read_file_as_string


# Credentials
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_org_id = os.getenv("OPENAI_ORG_ID")
aws_profile = os.getenv("AWS_PROFILE")

# Create the LLM model
llm_model = create_llm_model(
    LLMModel.OPENAI_GPT4O,
    LLMCredentials(
        openai_api_key,
        openai_org_id,
        aws_profile
    ),
    temperature=0,
    max_output_tokens=1024
)

# Following classes defines the structure of the output
class MedicalExaminationDay(BaseModel):
    date: str = Field(description="Date of medical examination day in mm/dd/yyyy format")
    title: str = Field(description="Concise title for this medical examination day that briefing symptoms and diagnosis")
    symptoms: list[str] = Field(description="List of symptoms identified on the medical examination day in a sentence each")
    diagnosis: str = Field(description="Diagnosis of the medical examination day in a paragraph")

class MedicalHistory(BaseModel):
    title: str = Field(description="Concise title that briefing the patient's medical history")
    medical_history: list[MedicalExaminationDay] = Field(description="List of medical examination days in chronological order")

output_parser = PydanticOutputParser(pydantic_object=MedicalHistory)

chain = prompt_template_to_organize_a_medical_record() | llm_model | output_parser

output = chain.invoke(
    {
        # Medical history note was taken from : https://www.youtube.com/watch?v=BmQppGzk78A
        "medical_history": read_file_as_string(os.path.join("/assets", "medical_history_note.txt")),
        "output_format_instructions": output_parser.get_format_instructions(),
    },
    {
        "callbacks": [StdOutCallbackHandler()],
    },
)

print(output.json(indent=2))
