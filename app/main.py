import os
import json
from config import read_aws_access_keys, config
import boto3
from file_utils import read_file_as_string
from amazon_bedrock import AmazonBedrockClaudeModels
from organize_medical_record_with_claude import organize_medical_record_with_claude


aws_access_keys = read_aws_access_keys()

boto3.setup_default_session(aws_access_key_id=aws_access_keys.aws_access_key_id,
                            aws_secret_access_key=aws_access_keys.aws_secret_access_key)

bedrock_runtime_client = boto3.client("bedrock-runtime",
                                      region_name=config.amazon_bedrock.region)

organized_medical_history = organize_medical_record_with_claude(
    bedrock_runtime_client,
    AmazonBedrockClaudeModels.CLAUDE_3_5_SONNET,
    read_file_as_string(
        # Medical history note was taken from : https://www.youtube.com/watch?v=BmQppGzk78A
        os.path.join("inputs", "medical_history_note.txt")
    )
)

print(json.dumps(
    organized_medical_history,
    indent=4
))