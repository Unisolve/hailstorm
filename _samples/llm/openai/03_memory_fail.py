#!/usr/bin/env python3
# name:    03_memory_fail.py
# process: A command line test of langchain llms OpenAI
#          Assumes you have the openai python package installed, and your openai api
#          key in the environment variable OpenAI_KEY
#          Uses ChatOpenAI chat model and the predict() method
#          This sample should fail to generate the correct answer to question 3
# author:  Simon Taylor

import os
api_key = os.getenv('OpenAI_KEY')

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI(openai_api_key = api_key)
chat_model = ChatOpenAI()

# First, ask a question about world football

text = "Who won the FIFA mens world cup in 2018?"
print(llm.predict(text))

# Second, change the topic

text = "What is 3 times 4?"
print(llm.predict(text))

# Third question, assumes memory of the context provided by the first. The correct answer
# is 'Hugo Lloris'.

text = "Who was their captain?"
print(llm.predict(text))
