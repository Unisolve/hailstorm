# name:    01-api-client.py
# process: A test of the text-generation-webui, run from the runpod command line

import langchain
from langchain import PromptTemplate, LLMChain
from langchain.llms import TextGen

langchain.debug = True

template = """Question: {question}

Answer: Let's think step by step."""


prompt = PromptTemplate(template=template, input_variables=["question"])
llm = TextGen(model_url=model_url)
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "Suggest a clever name for a seaside resaurant"

llm_chain.run(question)

"""
 root@2344a19d8d12:/workspace ᐅ python api.py
[chain/start] [1:chain:LLMChain] Entering Chain run with input:
{
  "question": "Suggest a clever name for a seaside resaurant"
}
[llm/start] [1:chain:LLMChain > 2:llm:TextGen] Entering LLM run with input:
{
  "prompts": [
    "Question: Suggest a clever name for a seaside resaurant\n\nAnswer: Let's think step by step."
  ]
}
Question: Suggest a clever name for a seaside resaurant

Answer: Let's think step by step.  First, we need to come up with something that suggests the location of the restaurant (beach/ocean). How about "Oceana" or "Baywatch"? Or if you want to go more casual and beachy, how about "Surf & Turf" or "Sandbar".
"""
