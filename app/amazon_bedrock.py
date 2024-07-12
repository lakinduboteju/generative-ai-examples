from enum import StrEnum


class AmazonBedrockModel(StrEnum):
    CLAUDE_INSTANT = "anthropic.claude-instant-v1",
    CLAUDE_3_HAIKU = "anthropic.claude-3-haiku-20240307-v1:0",
    CLAUDE_3_5_SONNET = "anthropic.claude-3-5-sonnet-20240620-v1:0",
    LLAMA_3_70B = "meta.llama3-70b-instruct-v1:0",
    MISTRAL_7B = "mistral.mistral-7b-instruct-v0:2",
