from config import read_aws_access_keys, config
import boto3
from amazon_bedrock import converse_with_model, AmazonBedrockModels, create_system_messages, create_text_message, parse_response


aws_access_keys = read_aws_access_keys()

boto3.setup_default_session(aws_access_key_id=aws_access_keys.aws_access_key_id,
                            aws_secret_access_key=aws_access_keys.aws_secret_access_key)

bedrock_runtime_client = boto3.client("bedrock-runtime",
                                      region_name=config.amazon_bedrock.region)

response = converse_with_model(bedrock_runtime_client,
                               AmazonBedrockModels.CLAUDE_INSTANT,
                               [
                                   create_text_message("Hello, how are you?"),
                               ],
                               10,
                               create_system_messages("Please respond only with emoji."),
                               0.5, 0.5,
                               {"top_k": 200}
)

response = parse_response(response)

print(response.output_message["content"][0]["text"])
print(response.input_tokens, response.output_tokens)
