# PROJECT TITLE: Career Intellect

## Startup Gateway Hackathon - MERCOR

## TEAM NAME: 3 Musketeers

1. Divyansh Tripathi
2. Sumit Dhiman
3. Hamna Qaseem

## Project Objective:

The objective of our project is to extract relevant information from resume and present it in structured format. This project involves various stages of data processing, analysis 
and integration to provide an efficient and effective solution for automating the recruitment process. 

Our project contains set of python scripts for extracting text from PDF resumes and performing TEXT summarization using the OpenAI API. 

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
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

Edit the .env file and fill in the required values for the environment variables.

## 5. Generate a new Alembic script
```
docker compose exec backend alembic revision --autogenerate
```

## 6. For Migration

```
docker compose exec backend alembic upgrade head

```

## 7. Start the development server:

```
python -m src.server

```


## Testing

- You can run tests by using following command:
    ```bash
    python -m src.tests.run
    ```
  
## Deployment

Following are the links for deployment.

- Link#1. (https://streamlit.hackathon.sumitdhiman.in/)

- Link#2. (https://hackathon.sumitdhiman.in/)






  
