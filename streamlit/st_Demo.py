import streamlit as st
import pandas as pd

dictionary = { "SWOT": { "Strengths": [ "Project Management", "Information Design", "Relationship Building", "Information Technology", "Excellent communication ability", "Outstanding organizational and time-management skills", "In depth understanding of diverse computer systems and networks" ], "Weaknesses": [ "Lack of specific experience as an IT Technician" ], "Opportunities": [ "Proven experience in managing projects and relationships can be leveraged to effectively communicate and collaborate with users", "Education in Management Information Systems provides a strong foundation in information technology and problem-solving skills", "Experience in information design can contribute to creating user-friendly interfaces and systems" ], "Threats": [ "Competition from candidates with specific experience as an IT Technician", "Certification as IT Technician may be required for some positions" ] } }



# # Iterate over the dictionary and extract keys and values
# for key, value in dictionary["SWOT"].items():
#     keys.append(key)
#     values.append(value)

# # Create a DataFrame from the lists
# data = {'Key': keys, 'Value': values}
# df = pd.DataFrame(data)

# # Display the DataFrame
# st.table(df)
def display_dictionary(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            st.markdown(f"## {key}")
            display_dictionary(value)
        elif isinstance(value, list):
            st.markdown(f"## {key}")
            for item in value:
                st.write("- ", item)
        else:
            st.write(f"**{key}:** {value}")

def display_dictionary2(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, list):
            st.markdown(f"## {key}")
            for item in value:
                st.write("- ", item)
        else:
            st.write(f"**{key}:** {value}")

def display_ans(dictionary):
    for category, data in dictionary.items():
        st.subheader(category)
        for item in data:
            st.write("- ", item)

