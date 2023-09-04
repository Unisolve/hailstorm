#!/usr/bin/env python3
# name:    01_list_models.py
# process: A command line test of langchain llms - Google PaLM 2
#          List models that offer the 'generateText' method
#          Assumes you have the google-generativeai python package installed, and your Google api
#          key in the environment variable GOOGLE_API_KEY
# author:  Simon Taylor

import os
api_key = os.getenv('GOOGLE_API_KEY')

import pprint
import google.generativeai as palm

palm.configure(api_key=api_key)

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)

