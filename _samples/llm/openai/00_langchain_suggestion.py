#!/usr/bin/env python3
# nane: 00_langchain_simple_question.py
# process: 
# author: Simon Taylor

import os
api_key = os.getenv('OpenAI_KEY')

from langchain.llms import OpenAI
llm = OpenAI(openai_api_key = api_key, temperature=0.9)

prompt = "Suggest me a good name for an ice cream parlour that is located on a beach!"
print(llm(prompt))
