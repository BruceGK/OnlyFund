import json
import openai

import pandas as pd
import numpy as np
import os

import warnings
warnings.filterwarnings("ignore")


api_key ="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"
openai.api_key = api_key

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]



path = '/Users/vicky/Desktop/GitHub/Repo/OnlyFund/Data/EDGAR_download/Official_Insider_Data_2023Q2'


all_data = pd.DataFrame()
for filename in os.listdir(path):
    table = pd.read_csv(path + '/' + filename, sep='\t')
    
    all_data = pd.concat([all_data, table])

#all_data.info(memory_usage='deep')

prompt = f"""
You're an experienced trader with extensive knowledge equity market. 
Below has been provided the aggregated data of insider trading information reported on government website for 2023 Q2.

Please use your intuition and rationale thinking to identifiy noticeable trend or unusual buying or selling activites that can be use as predicator for future trading event.

Examples of noticeable signals:
- sudden increase buying or selling events
- correlated buying or selling activities from a group of broad member
- unsual trading pattern with market backdrop of the company at that given date


Review table of aggregate data: '''{all_data}'''

Please note that the table can be sorted base on identifier with name of ACCESSION_NUMBER

"""
response = get_completion(prompt)
print(response)