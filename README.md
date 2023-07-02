# PROJECT TITLE: Career Intellect

## Startup Gateway Hackathon - MERCOR

## TEAM NAME: 3 Musketeers

1. Divyansh Tripathi
2. Sumit Dhiman
3. Hamna Qaseem

## Project Objective:

The objective of our project is to extract relevant information from resume and present it in structured format. This project involves various stages of data processing, analysis 
and integration to provide an efficient and effective solution for automating the recruitment process. 

# RESUME PDF TEXT EXTRACTION AND SUMMARIZATION

Our project contains set of python scripts for extracting text from PDF resumes and performing TEXT summarization using the OpenAI API. 

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Configuration](#project-configuration)
- [Testing](#testing)
- [Deployment](#deployment)

## Prerequisites
- Python 
- Docker
- Postgres

## Installation

To install and run the Project Name, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/lucifer1708/Hackathon.git
   cd Hackathon

## 1. Setting up virtual enviroment

```
python-m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate.bat
```

## 2. Install the required dependencies

```
pip install -r requirements.txt
```

## 3. Start the Docker containers:

```
docker-compose up  --build -d
```

## 4. Set up the project configuration:

Copy the .env.example file and rename it to .env.
Edit the .env file and fill in the required values for the environment variables.

## 5. Generate a new Alembic script
```
docker compose exec backend alembic revision --autogenerate
```

## 6. For Migration

```
docker compose exec backend alembic upgrade head

```

## 6. Start the development server:

```
python -m src.server

```

# Project Configuration

The project can be configured by modifying the following files:

- 'settings.py': Contains the project's settings and configurations.
- 'docker-compose.yaml': Defines the Docker services and configurations.

# Following are the files:

**File#1: compare.py**

This file compare resumes and perform analysis using OpenAI API.

# Dependencies: 

We imported json and os

- 'json': used for handling JSON data
- 'os': used for interacting with operating system

# Overview:

This file comparing resumes by analyzing skills in relation to specific job description. It is using OpenAI API to generate response based on conversation 
between the user, system and assistant. Our code setup the necessary functions and variables, creating conversation messages and then retrieve the final response.

- **File#2: rs_pdf.py**

  This file is basically used for reading text from resumes and it will iterate through each page of resume and then return the extracted text from PDF as a string.

  # Dependencies:

  - 'PyPDF2': This is used to read text from Resumes

  # Overview:

  This file is using the python library i.e. PyPDF2. It opens the pdf files, iterate each page of pdf and then extract text from them. We can easily access text from pdf.

- **File#3: jd_skill.py**

In this file, we used code that performs summarization of job descrition using OpenAI API.

# Dependencies:

- 'openai': interacting with OpenAI API

# Overview:

It setup the necessary API key, define a function to interact with API and then provide job description data. Then call API function with provided job description
data to generate summarized version. This will help us in quickly understandings the key points and requirements of job without reading the entire description.


- **File#4: rs_dict.py**

This file is basically performing summarization of resume into subfield using OpenAI API.

# Dependencies:

- 'openai': interacting with Openai
- 'rs_pdf': It contains extracted text variable that store text that we extracted from resumes.

# Overview:

It setup the API key, import extracted resume text from module i.e. rs_pdf. Then system and user messages are defined that are representing the resume subfield.
This will help us quickly understanding the key information in different section of resume.

## Testing

- You can run tests by using following command:
    ```bash
    python -m src.tests.run_test
    ```
  
## Deployment

Following are the links for deployment.

- Link#1. (https://streamlit.hackathon.sumitdhiman.in/)

- Link#2. (https://hackathon.sumitdhiman.in/)

  
