import json
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage


def prompt_template_to_organize_a_medical_record() -> ChatPromptTemplate:
    system_message = " ".join([
        "You are an app that organizes a given medical history note written by a medical doctor into well organized format described by the user.",
        "Your response must strictly stick to user's output format instructions, and minify your output by avoiding unnecessary line breaks or white spaces. Most importantly, do not include any additional text apart from user specified format.",
    ])

    human_message = "\n".join([
        "A medical history of a patient written by a medical doctor is given below within XML tags (medical_history):",
        "<medical_history>",
        "{medical_history}",
        "</medical_history>",
        "",
        "Organize symptoms and diagnosis of each examination day in chronological order, without loosing any original information, without including information outside the original medical history and, without assuming anything apart from the original medical history.",
        "",
        "All details that should be included in your response and how they should be formatted are specified below:",
        "{output_format_instructions}",
    ])

    return ChatPromptTemplate.from_messages([
        SystemMessage(system_message),
        HumanMessagePromptTemplate.from_template(human_message),
    ])
