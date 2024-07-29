from openai import OpenAI
import os
from loguru import logger

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def generate_title(input_string: str, model: str = "gpt-4o-mini", temperature: float = 0, max_tokens: int = 60) -> str:
    """
    Generate a suitable title for a conversation using the OpenAI ChatGPT API.

    Args:
        input_string (str): The user input string based on which the title will be generated.
        model (str): The model to use for generating the title. Default is "gpt-4".
        temperature (float): Sampling temperature to use. Higher values mean the model will take more risks. Default is 0.7.
        max_tokens (int): The maximum number of tokens to generate. Default is 60.

    Returns:
        str: Generated title for the conversation.

    Raises:
        Exception: If there is an error while generating the title.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system",
                 "content": "Generate a concise, accurate title in a few words for the conversation based on the following user input."},
                {"role": "user", "content": input_string}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        title = response.choices[0].message.content.strip().strip('"')
        return title

    except Exception as e:
        raise Exception(f"Error generating title: {e}")
