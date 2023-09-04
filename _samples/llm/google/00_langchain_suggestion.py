#!/usr/bin/env python3
# name:    00_langchain_suggestion.py
# process: A command line test of langchain llms - Google PaLM 2
#          Assumes you have the google-generativeai python package installed, and your Google api
#          key in the environment variable GOOGLE_API_KEY
#          We set the temperature to a high (creative) value to get the model to explore 
#          more of its training data.
# author:  Simon Taylor

import os
api_key = os.getenv('GOOGLE_API_KEY')

from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm

llm = GooglePalm(temperature=0.9)

prompt = "Suggest a good name for a restauraunt located anywhere on a mountain!"
print(llm(prompt))
