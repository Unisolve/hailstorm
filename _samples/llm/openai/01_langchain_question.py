#!/usr/bin/env python3
# nane: 00_langchain_simple_question.py
# process: 
# author: Simon Taylor

import os
api_key = os.getenv('OpenAI_KEY')

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI(openai_api_key = api_key)
chat_model = ChatOpenAI()

text = "What is the capital city of Tonga?"

print(llm.predict(text))
