# name:    00-raw.py
# process: A raw test of the model, run from the runpod command line

from transformers import AutoTokenizer, pipeline, logging
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig

model_name_or_path = "TheBloke/Wizard-Vicuna-7B-Uncensored-GPTQ"
model_basename = "model"

use_triton = False

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

model = AutoGPTQForCausalLM.from_quantized(model_name_or_path,
        model_basename=model_basename,
        use_safetensors=True,
        trust_remote_code=True,
        device="cuda:0",
        use_triton=use_triton,
        quantize_config=None)

prompt = "Explain how a limerick is structured?"
prompt_template=f'''A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.

USER: {prompt}
ASSISTANT:
'''

print("\n\n*** Generate:")

input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
output = model.generate(inputs=input_ids, temperature=0.7, max_new_tokens=512)
print(tokenizer.decode(output[0]))


"""
Sample  output. It *knows* what a limerick is, it just can't write one ;-)

*** Generate:
<s> A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.

USER: Explain how a limerick is structured?
ASSISTANT:
A limerick is a five-line poem that follows a specific rhyme scheme. It typically has a humorous or nonsensical theme, and often includes wordplay and puns. The structure of a limerick is as follows:

1. The first line has a rhyme scheme of AABB.
2. The second line has a rhyme scheme of ABAAB.
3. The third line has a rhyme scheme of AABBA.
4. The fourth line has a rhyme scheme of AAAABB.
5. The fifth line has a rhyme scheme of AAAABBCC.

For example, here is a limerick:

There once was a man from Peru,
Whose navel was deep in his ear.
He stood there, and he stood there,
Till his ear dropped, and he bled.

In this limerick, the first line has a rhyme scheme of AABB, the second line has a rhyme scheme of ABAAB, the third line has a rhyme scheme of AABBA, the fourth line has a rhyme scheme of AAAABB, and the fifth line has a rhyme scheme of AAAABBCC.</s>
"""
