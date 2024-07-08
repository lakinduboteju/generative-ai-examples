import json
import boto3
from amazon_bedrock import converse_with_model, AmazonBedrockClaudeModels, create_system_messages, create_text_message, parse_response


def organize_medical_record_with_claude(bedrock_runtime_client: boto3.client,
                                        claude_model: AmazonBedrockClaudeModels,
                                        medical_history: str) -> list[dict]:
    system_message = " ".join([
        "You are an app that organizes a given medical history note written by a medical doctor into well formatted JSON.",
        "Your response must include only the JSON, without line breaks or unnecessary white spaces and, most importantly without any additional text apart from the JSON.",
    ])

    prompt = "\n".join([
        "Following is a medical history of a patient written by a medical doctor:",
        "<medical_history>",
        medical_history,
        "</medical_history>",
        "",
        "Organize symptoms and diagnosis for each examination day in chronological order, without loosing any original information, without including information outside the original medical history and, without assuming anything apart from the original medical history.",
        "",
        "All details that should be included in your response are specified below. Strictly stick to the following output JSON format:",
        "<output_json_format>",
        json.dumps([
            {
                "date": "Date in mm/dd/yyyy format",
                "title": "Concise title for this examination day that briefing symptoms and diagnosis",
                "symptoms": [
                    "Symptom 1 in a sentence", "Symptom 2 in a sentence", "and so on..."
                ],
                "diagnosis": "Diagnosis in a paragraph"
            },
        ]),
        "</output_json_format>",
    ])

    max_tokens = 4000
    temperature = 0.0
    top_p = 0.0
    top_k = 200
    assistant_start = '[{"date":'

    response = converse_with_model(
        bedrock_runtime_client,
        str(claude_model),
        [
            create_text_message(prompt),
            create_text_message(assistant_start, True),
        ],
        max_tokens,
        create_system_messages(system_message),
        temperature, top_p,
        {
            "top_k": top_k,
        }
    )

    response = parse_response(response)

    print(response.input_tokens, response.output_tokens)

    output_json = assistant_start + response.output_message["content"][0]["text"]
    return json.loads(output_json)
