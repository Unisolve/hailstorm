# Running Wizard-Vicuna-7B-Uncensored-GPTQ on runpod.io

## Model Name

TheBloke/Wizard-Vicuna-7B-Uncensored-GPTQ

## Installation

  * runpod.io: 
    - Click the "Connect" button on your pod
    - Click on "Connect to HTTP service [Port 7860]"
  * text-generation-ui:
    - Click in "Model" tab
    - Enter the model name (TheBloke/Wizard-Vicuna-7B-Uncensored-GPTQ) in the "Download model or LoRA" field and click download
    - In the top left, click the refresh icon next to Model
    - In the Model dropdown list choose the model you just downloaded: TheBloke_Wizard-Vicuna-7B-Uncensored-GPTQ
    - In the "Model Loader" field choose "ExLlama" (this is critical)
    - Click on "Load" - be patient, it'll take a few seconds before the loading interface at the right registers any change...

## Hardare Notes

I ran this on a much larger setup than necessary:

    2 x L40
    4 vCPU 500 GB RAM
    
but the answers sure did appear quickly!    
