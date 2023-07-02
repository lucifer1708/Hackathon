import openai
from rs_pdf import extracted_text

openai.api_key = "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"

system_message = f"""
Your task is to summarise given resume into sub fields wlike Education, Projects,Achievements, Skills\
dont answer in lengthy text just ton the point bullet points\
SUm up experience in few lines \
Respond in json format for subfields of Job Description\
Give output in dictionary with sub fields as keys\
"""

data = extracted_text

messages = [
    {"role": "system", "content": system_message},
    {
        "role": "assistant",
        "content": f"""Relevant resume content: \n
  {data}""",
    },
]


def get_completion_from_messages(
    messages, model="gpt-3.5-turbo", temperature=0.5, max_tokens=2000
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=500,
    )
    return response.choices[0].message["content"]


# print()
summ_res = get_completion_from_messages(messages)
print(summ_res)
