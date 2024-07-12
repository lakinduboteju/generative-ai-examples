import json
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, PromptTemplate
from langchain_core.messages import SystemMessage


def prompt_template_to_organize_a_medical_record_into_json() -> ChatPromptTemplate:
    json_object = {
        "date": "Date in mm/dd/yyyy format",
        "title": "Concise title for this examination day that briefing symptoms and diagnosis",
        "symptoms": [
            "Symptom 1 in a sentence", "Symptom 2 in a sentence", "and so on...",
        ],
        "diagnosis": "Diagnosis in a paragraph",
    }

    json_object_string = "{" + json.dumps(json_object) + "}"

    system_message = " ".join([
        "You are an app that organizes a given medical history note written by a medical doctor into well formatted JSON.",
        "Your response must include only the JSON string, without line breaks or unnecessary white spaces and, most importantly without any additional text apart from the JSON.",
    ])

    human_message = "\n".join([
        "Following is a medical history of a patient written by a medical doctor:",
        "<medical_history>",
        "{medical_history}",
        "</medical_history>",
        "",
        "Organize symptoms and diagnosis for each examination day in chronological order, without loosing any original information, without including information outside the original medical history and, without assuming anything apart from the original medical history.",
        "",
        "All details that should be included in your response are specified in following output json format. Your output must strictly stick to the following output JSON format, which is a JSON array with JSON objects within:",
        "<output_json_format>",
        f"[{json_object_string}, ...]",
        "</output_json_format>",
    ])

    return ChatPromptTemplate.from_messages([
        SystemMessage(system_message),
        HumanMessagePromptTemplate.from_template(human_message),
    ])
