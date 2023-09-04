#!/usr/bin/env python3
# name:    01_list_models.py
# process: A command line test of langchain llms - Google PaLM 2
#          List models that offer the 'generateText' method
#          Assumes you have the google-generativeai python package installed, and your Google api
#          key in the environment variable GOOGLE_API_KEY
# author:  Simon Taylor

import os
api_key = os.getenv('GOOGLE_API_KEY')

import google.generativeai as palm

palm.configure(api_key=api_key)

model = 'models/text-bison-001'

prompt = """
You are an expert at reasoning.

Solve the following problem:

Today is Monday, tomorrow is Wednesday.

What is wrong with that statement?

Think about it step by step, and show your work.
"""

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

print(completion.result)
