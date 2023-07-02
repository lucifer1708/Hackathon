import streamlit as st
import os
from dotenv import load_dotenv
import openai
from time import sleep 
import rs_dict
import rs_pdf
from compare import create_mssg_final , swot
from rs_pdf import read_pdf2
from jd_skill import jd_final, create_message_jd
from rs_dict import rs_final
from rs_dict import create_message_rs
from st_Demo import display_ans, display_dictionary, display_dictionary2
import json



def main():
    load_dotenv()  # Load environment variables from .env file
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    st.title("Resume Parser App")

    # Add file uploader to allow users to upload resumes
    uploaded_file = st.file_uploader("Upload Resume", type="pdf")
    job_desc = st.text_area("Job Description")

    resume = False
    job = False

    col1, col2 = st.columns(2)

    # uploaded_jd = st.file_uploader("Upload Resume", type="pdf")
    if uploaded_file:
        # Display uploaded file details
        st.write("Uploaded file:", uploaded_file.name)

        # Parse resume and extract information
        resume_text = rs_pdf.read_pdf2(uploaded_file)
        # st.write("Resumed file:", resume_text)

        messages = create_message_rs(resume_text)
        # st.write( "messages:", messages)
        parsed_info = rs_dict.rs_final(messages, model="gpt-3.5-turbo", temperature=0.5, max_tokens=2000)

        # st.spinner("Processing...")
        # dict show kru?
        # resume_dict = json.loads(parsed_info)
        # with col1:
        #     st.write("Parsed Resume Information")
        #     display_dictionary(resume_dict)
        # Display parsed information
        # st.header("Parsed Information")
        # st.write(parsed_info)
        resume = True

    if job_desc:
        # st.write("Job Description:" , job_desc)
        mess = create_message_jd(job_desc)
        parsed_jd = jd_final(mess)
        # job_info_dict = json.loads(parsed_jd)
        # with col2:
        #     st.write("Parsed Job Information")
        #     display_dictionary2(job_info_dict)
        # st.header("Parsed Job Description:")
        # st.write(parsed_jd)
        job = True

    if resume and job:
        inp = create_mssg_final(parsed_info, parsed_jd)
        ans = swot(inp,model="gpt-3.5-turbo", temperature=0.5, max_tokens=2000)
        # print(type(ans))
        st.markdown("# SWOT Analysis for resume")
        ans_dict = json.loads(ans)
        # type(ans_dict)
        display_ans(ans_dict["SWOT"])
        # st.write("SWOT Analysis")



if __name__ == "__main__":
    main()