import openai

# from jd_skill import summ_desc
openai.api_key = "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"


system_message = """
 Your task is to summarise given resume into sub fields wlike Education, Projects,Achievements, Skills\
 dont answer in lengthy text just ton the point bullet points\
 SUm up experience in few lines \
 Respond in json format for subfields of Job Description\
 Give output in dictionary with sub fields as keys\
 """

jd_system_message = """
Your task is to summarise given job description into sub fields like Responsibilities, Job brief , Skills and Requirements\
Respond in json format for subfields of Job Description\
Give output in dictionary with sub fields as keys\
"""


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


compare_system_message = """
You are a helpful assistant whose job is to enhance resumes of its users\
Respond in json format for SWOT \
You will be given what 1)current resume fields value 2) job description for the applying post in context. \
Tell the user a brief SWOT(Strength, weakness, opportunity, threats) analysis for this field without much explainations \
For Strengths just tell the skills which are
Give output in dictionary with SWOT as keys and values\
"""


def compare_completion_from_messages(
    messages, model="gpt-3.5-turbo", temperature=0.5, max_tokens=2000
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]
