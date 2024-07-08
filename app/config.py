from dataclasses import dataclass
import csv


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


@dataclass
class AwsAccessKeys:
    aws_access_key_id: str
    aws_secret_access_key: str


def read_aws_access_keys() -> AwsAccessKeys:
    with open('aws_access_keys.csv', mode='r') as file:
        reader = csv.DictReader(file)
        row = next(reader)
        file.close()
        for key, value in row.items():
            if 'Access key ID' in key:
                access_key_id = value
            elif 'Secret access key' in key:
                secret_access_key = value
        assert access_key_id and secret_access_key
        return AwsAccessKeys(
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key
        )
