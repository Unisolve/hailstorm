#!/usr/bin/env python3
# name:    03_langchain_question.py
# process: A command line test of langchain llms - GooglePalm
#          Assumes you have the google-generativeai python package installed, and your Google api
#          key in the environment variable GOOGLE_API_KEY
#          Note: Work in progess - I have yet to understand how Vertex AI plays with LangChain / PaLM2
# author:  Simon Taylor

import os
api_key = os.getenv('GOOGLE_API_KEY')

from langchain.llms import GooglePalm

llm = GooglePalm(temperature=0.9)

text = "What is the capital city of Tonga?"

response = llm.generate(prompts=[text])

print(response.generations[0])
