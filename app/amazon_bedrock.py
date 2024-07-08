import boto3
from enum import StrEnum
from dataclasses import dataclass


class AmazonBedrockModels(StrEnum):
    CLAUDE_INSTANT = "anthropic.claude-instant-v1",
    CLAUDE_3_HAIKU = "anthropic.claude-3-haiku-20240307-v1:0",
    CLAUDE_3_5_SONNET = "anthropic.claude-3-5-sonnet-20240620-v1:0",
    LLAMA_3_8B = "meta.llama3-8b-instruct-v1:0",
    MISTRAL_7B = "mistral.mistral-7b-instruct-v0:2",


class AmazonBedrockClaudeModels(StrEnum):
    CLAUDE_INSTANT = str(AmazonBedrockModels.CLAUDE_INSTANT),
    CLAUDE_3_HAIKU = str(AmazonBedrockModels.CLAUDE_3_HAIKU),
    CLAUDE_3_5_SONNET = str(AmazonBedrockModels.CLAUDE_3_5_SONNET),


def converse_with_model(bedrock_runtime_client: boto3.client,
                        model: AmazonBedrockModels,
                        messages: list[dict],
                        max_tokens: int,
                        system_messages: list[dict] | None = None,
                        temperature: float = 0.0, top_p: float = 0.0,
                        model_specific_params: dict = None):
    args = {
        "modelId": str(model),
        "messages": messages,
        "inferenceConfig": {
            "maxTokens": max_tokens,
            "temperature": temperature,
            "topP": top_p,
        },
        "additionalModelRequestFields": model_specific_params,
    }

    if system_messages:
        args["system"] = system_messages

    return bedrock_runtime_client.converse(**args)


def create_system_messages(*texts: str):
    system_messages = []
    for text in texts:
        system_messages.append({
            "text": text,
        })
    return system_messages


def create_text_message(text: str, is_assistant: bool = False):
    return {
        "role": "assistant" if is_assistant else "user",
        "content": [
            {
                "text": text
            }
        ]
    }


@dataclass
class AmazonBedrockResponse:
    output_message: dict
    stop_reason: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    latency_ms: int


def parse_response(response: dict):
    return AmazonBedrockResponse(
        output_message=response['output']['message'],
        stop_reason=response['stopReason'],
        input_tokens=response['usage']['inputTokens'],
        output_tokens=response['usage']['outputTokens'],
        total_tokens=response['usage']['totalTokens'],
        latency_ms=response['metrics']['latencyMs'],
    )
