import json
import os

import openai

# from jd_skill import summ_desc
openai.api_key = "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"


def get_completion_from_messages(
    messages, model="gpt-3.5-turbo", temperature=0.5, max_tokens=2000
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]


compare_system_message = """
You are a helpful assistant whose job is to enhance resumes of its users\
Respond in json format for SWOT \
You will be given what 1)current resume fields value 2) job description for the applying post in context. \
Tell the user a brief SWOT(Strength, weakness, opportunity, threats) analysis for this field without much explainations \
For Strengths just tell the skills which are
Give output in dictionary with SWOT as keys and values\
"""


def create_user_mssg(field=str, res_val=str):
    return f"""this is my resume's {field} value: {res_val}"""


user_message_1 = create_user_mssg(
    "skills",
    "python, openCV, Figma, kubernetes, Kafka, Redis, Linux, Dash,  Android Studio , pytorch,Biology,  Tableau, DSA , HTML, CSS , Javascript, embedded ML",
)

# job_info = summ_desc

job_info = "Bachelor’s/Master’s degree in a quantitative field, 3 to 5 years of professional experience in an analytical role, Proficiency with database, spreadsheet, and statistical tools, Advanced SQL experience, Experience analyzing large, complex data sets, Experience with Python or R, Ability to solve problems analytically and create actionable insights, Advanced ability to use reporting tools like Tableau and/or Excel, Strong written and verbal communication skills"

messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_message_1},
    {
        "role": "assistant",
        "content": f"""Relevant Job description information: \n
  {job_info}""",
    },
]


final_response = get_completion_from_messages(messages)
print(final_response)
