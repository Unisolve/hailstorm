#!/usr/bin/env python3
# name:    01_langchain_question.py
# process: A command line test of langchain llms OpenAI
#          Assumes you have the openai python package installed, and your openai api
#          key in the environment variable OPENAI_API_KEY
#          Uses ChatOpenAI chat model and the predict() method
# author:  Simon Taylor

import os
api_key = os.getenv('OPENAI_API_KEY')

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI(openai_api_key = api_key)
chat_model = ChatOpenAI()

text = "What is the capital city of Tonga?"

print(llm.predict(text))
