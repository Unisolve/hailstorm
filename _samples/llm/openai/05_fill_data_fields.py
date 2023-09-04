#!/usr/bin/env python3
# name:    05_fill_data_fields.py
# process: Inject instructions into a prompt template to fill in fields in a data structure 
# Based on clever code from Arjan Egges: https://github.com/ArjanCodes/examples/tree/main/2023/langchain
# TODO:    Add exception hander

# The LLM is capable enough, lots of input possibilities are parsed corrctly.
#
# Enter the name of a country: South Sudan
# The capital of South Sudan is Juba.
#
# Enter the name of a country: Australia
# The capital of Australia is Canberra.
#
# Enter the name of a country: Down Under
# The capital of Australia is Canberra.
#
# Enter the name of a country: Kangaroo Land
# The capital of Australia is Canberra.
#
# Enter the name of a country: Only English speaking country in South America
# The capital of Guyana is Georgetown.

import os
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


# Define your desired data structure.
class Country(BaseModel):
    capital: str = Field(description="capital of the country")
    name: str = Field(description="name of the country")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


OPENAI_MODEL = "gpt-3.5-turbo"

PROMPT_COUNTRY_INFO = """
    Provide information about {country}.
    {format_instructions}
    """


def main():
    # Set up a parser + inject instructions into the prompt template.
    parser = PydanticOutputParser(pydantic_object=Country)

    # setup the chat model
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)
    message = HumanMessagePromptTemplate.from_template(
        template=PROMPT_COUNTRY_INFO,
    )
    chat_prompt = ChatPromptTemplate.from_messages([message])

    # get user input
    country_name = input("Enter the name of a country: ")

    # generate the response

    display_blue("---> start get_format_instructions()")

    display_green(parser.get_format_instructions())

    display_blue("---> end   get_format_instructions()")

    chat_prompt_with_values = chat_prompt.format_prompt(
        country=country_name, format_instructions=parser.get_format_instructions()
    )

    display_blue("---> start output")

    output = llm(chat_prompt_with_values.to_messages())
    display_green(output)

    display_blue("--->   end output")

    country = parser.parse(output.content)

    # print the response
    print(f"\nThe capital of {country.name} is {country.capital}.")


def display_blue(string):
    print()
    print(bcolors.OKBLUE + string + bcolors.ENDC)

def display_green(string):
    print(bcolors.OKGREEN + str(string).rstrip() + bcolors.ENDC)


if __name__ == "__main__":
    main()
