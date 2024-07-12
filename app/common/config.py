from dataclasses import dataclass


@dataclass
class AmazonBedrock:
    region: str


@dataclass
class Config:
    amazon_bedrock: AmazonBedrock


config = Config(
    amazon_bedrock=AmazonBedrock(
        region='us-east-1'
    )
)
