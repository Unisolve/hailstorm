#!/usr/bin/env python3
# name:    02_langchain_sequential.py
# process: A proof of concept of two LLM queries chained together and controlled from 
#          a streamlit interface in a local browser.
#          Assumes you have the openai python package installed, and your openai api
#          key in the environment variable OPENAI_API_KEY
#          Assumes you have installed streamlit, a great package for running proof of concept ML apps
#          in your browser
# to run:  streamlit run 02_langchain_sequential.py
# author:  Simon Taylor

import os
import streamlit as st

api_key = os.getenv('OPENAI_API_KEY')

from langchain.llms    import OpenAI
from langchain.chains  import LLMChain
from langchain.chains  import SequentialChain
from langchain.prompts import PromptTemplate

#
# Define the get_tour_name_and_highlights() subroutine
#

def get_tour_name_and_highlights(region):

    llm = OpenAI(openai_api_key=api_key, temperature=0.9)

    prompt_template_name = PromptTemplate(
        input_variables = ['region'],
        template = "I want to promote a tour for adventurous tourists to {region}. Suggest a clever name for this tour"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='tour_name')

    prompt_template_items = PromptTemplate(
        input_variables = ['region', 'tour_name'],
        template = "Suggest a few highlights that a tourist should see when on the '{tour_name}' tour in {region}. Return them as a comma-separated list"
    )

    items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='tour_items')

    chain = SequentialChain(
        chains = [name_chain, items_chain],
        input_variables = ['region'],
        output_variables = ['tour_name', 'tour_items']
    )

    response = chain({'region': region})
    return response

# ----------------------------------------------------------------------------------------------------------

#
# Output a Streamlit title and sidebar, and if a region is chosen, execute the chain defined in
# get_tour_name_and_highlights()
#

llm = OpenAI(openai_api_key=api_key, temperature=0.9)

st.title("Design a tour!")

region = st.sidebar.selectbox(
    "Pick a country or region",
    (
        "France", "South of France", "Provence France", "Burgundy France",
        "India",
        "Italy", "Tuscany Italy", "Liguria Italy",
        "Japan",
        "Morocco",
        "Singapore",
        "Spain", "Basque Country Spain", "Andalusia Spain",
        "United States", "California United States", "Colorado United States", "New York United States",
        "Pennsylvania United States",
        "Australia", "New South Wales Australia", "Queensland Australia", "Victoria Australia",
    )
)

if region:
    # Define the leading and trailing characters we want to strip away from the LLM output
    lead_trail_chars = " \t\n\r.:123456789"

    # Get the reponse object from our sequential chain
    response = get_tour_name_and_highlights(region)

    # Output the tour name and highlights

    name = response['tour_name']
    #st.code(name, None, line_numbers=True)
    st.divider()
    #output_string = name.replace("tour", "").strip(lead_trail_chars)
    header = name.strip(lead_trail_chars)
    st.header(header)

    tour_items = response['tour_items'].strip(lead_trail_chars).split(",")

    "Tour Items"          # Any variable on a line by itself is handled by st.write()

    for item in tour_items:
        #st.code(item, None, line_numbers=True)
        st.write("-", item.strip(lead_trail_chars))

