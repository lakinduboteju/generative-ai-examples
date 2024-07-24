from enum import Enum
from dataclasses import dataclass

from langchain_openai import ChatOpenAI
from langchain_aws import ChatBedrock

from common.amazon_bedrock import AmazonBedrockModel
from common.config import config


class LLMModel(Enum):
    OPENAI_GPT4O = 0
    CLAUDE_3_5_SONNET = 1
    LLAMA_3 = 2
    MISTRAL = 3
    OPENAI_GPT4O_MINI = 4


@dataclass
class LLMCredentials:
    openai_api_key: str
    openai_org_id: str
    aws_profile: str | None


def create_llm_model(llm_model: LLMModel, llm_credentials: LLMCredentials, temperature: float, max_output_tokens: int):
    match llm_model:
        case LLMModel.OPENAI_GPT4O:
            llm_model = ChatOpenAI(
                model="gpt-4o",
                max_tokens=max_output_tokens,
                temperature=temperature,
                openai_api_key=llm_credentials.openai_api_key,
                openai_organization=llm_credentials.openai_org_id,
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
            if llm_credentials.aws_profile:
                params["credentials_profile_name"] = llm_credentials.aws_profile

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
            if llm_credentials.aws_profile:
                params["credentials_profile_name"] = llm_credentials.aws_profile

            llm_model = ChatBedrock(**params)

        case LLMModel.MISTRAL:
            params = dict(
                region_name=config.amazon_bedrock.region,
                model_id=str(AmazonBedrockModel.MISTRAL_MIXTRAL_8X7B),
                model_kwargs=dict(
                    temperature=temperature,
                    max_tokens=max_output_tokens,
                ),
            )
            if llm_credentials.aws_profile:
                params["credentials_profile_name"] = llm_credentials.aws_profile

            llm_model = ChatBedrock(**params)
        
        case LLMModel.OPENAI_GPT4O_MINI:
            llm_model = ChatOpenAI(
                model="gpt-4o-mini",
                max_tokens=max_output_tokens,
                temperature=temperature,
                openai_api_key=llm_credentials.openai_api_key,
                openai_organization=llm_credentials.openai_org_id,
            )

        case _:
            raise ValueError(f"Unknown LLM model: {llm_model}")

    return llm_model
