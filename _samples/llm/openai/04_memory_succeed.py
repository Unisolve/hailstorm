#!/usr/bin/env python3
# name:    04_memory_succeed.py
# process: A command line test of langchain llms OpenAI
#          Assumes you have the openai python package installed, and your openai api
#          key in the environment variable OPENAI_API_KEY
#          Uses ChatOpenAI chat model and memory provided by ConversationBufferWindowMemory
#          This sample should successfully generate the correct answer to question 3
# author:  Simon Taylor

import os
api_key = os.getenv('OPENAI_API_KEY')

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain

llm = OpenAI(openai_api_key = api_key)
chat_model = ChatOpenAI()

conversation = ConversationChain(
   llm=llm,
   memory=ConversationBufferWindowMemory(k=3)
)

# First, ask a question about world football

text = "Who won the FIFA mens world cup in 2018?"
print(conversation.predict(input=text))

# Second, change the topic

text = "What is 3 times 4?"
print(conversation.predict(input=text))

# Third question, assumes memory of the context provided by the first. The correct answer
# is 'Hugo Lloris'.

text = "Who was their captain?"
print(conversation.predict(input=text))
