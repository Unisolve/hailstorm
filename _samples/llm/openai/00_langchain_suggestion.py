#!/usr/bin/env python3
# name:    00_langchain_suggestion.py
# process: A command line test of langchain llms OpenAI
#          Assumes you have the openai python package installed, and your openai api
#          key in the environment variable OPENAI_API_KEY
#          We set the temperature to a high (creative) value to get the model to explore 
#          more of its training data, choose the road less travelled etc!
# author:  Simon Taylor

import os
api_key = os.getenv('OPENAI_API_KEY')

from langchain.llms import OpenAI
llm = OpenAI(openai_api_key = api_key, temperature=0.9)

prompt = "Suggest a good name for a restauraunt located anywhere on a mountain!"
print(llm(prompt))

prompt = "Suggest a good name for a restauraunt located anywhere on a mountain. Explain why you chose the name"
print(llm(prompt))
