#!/usr/bin/env python3
# name:     06_conversational_form.py
# process: 
# Based on: https://colab.research.google.com/drive/1asxfC-tsCjfmpWMqEi4x-zflg8CwnapM?usp=sharing#scrollTo=JgZPviRbJQoq
# TODO:     Add better exception handling

from langchain.chat_models import ChatOpenAI
from langchain.chains import create_tagging_chain, create_tagging_chain_pydantic
from langchain.chains import TransformChain, LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate

from enum import Enum
from typing import Optional, TypeVar
from pydantic import BaseModel, Field

# https://platform.openai.com/docs/models/overview
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
#llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo-0613")
#llm = ChatOpenAI(temperature=0,  model_name="gpt-4")

# Define a pydantic class for personal attributes we want to store

class PersonalDetails(BaseModel):
    first_name: Optional[str] = Field(
        ...,
        description="This is the first name of the user.",
    )
    last_name: Optional[str] = Field(
        ...,
        description="This is the last name or surname of the user.",
    )
    full_name: Optional[str] = Field(
        ...,
        description="Is the full name of the user ",
    )
    city: Optional[str] = Field(
        ...,
        description="The name of the city where someone lives",
    )
    email: Optional[str] = Field(
        ...,
        description="An email address that the person associates as theirs",
    )
    age: Optional[str] = Field(
        ...,
        description="The person's age in years",
    )
    #language: Optional[str] = Field(
        #..., enum=["spanish", "english", "french", "german", "italian"]
    #)

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

# Create a dummy user

user_123_personal_details = PersonalDetails(
    first_name="",
    last_name="",
    full_name="",
    city="",
    email="",
    age=""
)

#  A function to check which fields are empty and return them as a list

def check_what_is_empty(user_peronal_details):
    ask_for = []
    # Check if fields are empty
    for field, value in user_peronal_details.dict().items():
        if value in [None, "", 0]:  # You can add other 'empty' conditions as per your requirements
            print(f"Field '{field}' is empty.")
            ask_for.append(f'{field}')
    return ask_for


# Checking the response and adding it

def add_non_empty_details(current_details: PersonalDetails, new_details: PersonalDetails):
    non_empty_details = {k: v for k, v in new_details.dict().items() if v not in [None, ""]}
    updated_details = current_details.copy(update=non_empty_details)
    return updated_details

# Get the AI to prompt the user for each required item 

def ask_for_info(ask_for):
    # prompt template 1
    first_prompt = ChatPromptTemplate.from_template(
        "Below are some things to ask the user for in a conversational way. You should only ask one question at a time even if you don't get all the info \
        don't ask as a list! Don't greet the user! Don't say Hi. Explain you need to get some info. If the ask_for list is empty then thank them and ask how you can help them \n\n \
        ### ask_for list: {ask_for}"
    )

    # info_gathering_chain
    info_gathering_chain = LLMChain(llm=llm, prompt=first_prompt)
    ai_chat = info_gathering_chain.run(ask_for=ask_for)
    display_blue("---> start ai_chat")
    display_green(ai_chat)
    display_blue("---> end   ai_chat")
    return ai_chat

#

def filter_response(text_input, user_details ):
    chain = create_tagging_chain_pydantic(PersonalDetails, llm, verbose=True)
    display_blue("---> start tagging_chain")
    display_green(chain)
    display_blue("---> end   tagging_chain")

    try:
        res = chain.run(text_input)
    except OSError as err:
        print("--> OS error:", err)
    except ValueError:
        print("--> Saw a ValueError")
        ask_for = check_what_is_empty(user_details)
        return user_details, ask_for
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

    display_blue("---> start tagging_chain output")
    display_green(res)
    display_blue("---> end   tagging_chain output")
    # add filtered info to the user object
    user_details = add_non_empty_details(user_details,res)
    ask_for = check_what_is_empty(user_details)
    return user_details, ask_for


def display_blue(string):
    print()
    print(bcolors.OKBLUE + string + bcolors.ENDC)

def display_green(string):
    print(bcolors.OKGREEN + str(string).rstrip() + bcolors.ENDC)

# Create a chain that extracts information from a passage based on our pydantic schema

chain = create_tagging_chain_pydantic(PersonalDetails, llm)

ask_for = check_what_is_empty(user_123_personal_details)
print(ask_for)

print("Tell me a little about yourself")
text_input =  input()
print("Filtering reponse")
user_123_personal_details, ask_for = filter_response(text_input, user_123_personal_details)
print("Details now")
print(user_123_personal_details)
print("ask_for now")
print(ask_for)

while 1:
    if ask_for:
        print("Getting ai reponse")
        ai_response = ask_for_info(ask_for)
        print(ai_response)
        text_input = input()
        print("Filtering reponse")
        user_123_personal_details, ask_for = filter_response(text_input, user_123_personal_details)
        print("Details now")
        print(user_123_personal_details)
        print("ask_for now")
        print(ask_for)
    else:
        print("Thank you we have all the details")
        exit()


