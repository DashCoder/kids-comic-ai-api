# kids comic ai api
Kids Comic Generator API using Azure OpenAI, Python3.7, FastAPI

## Simple example of result generated from API 

*Use Postman, front-end app or included OpenAPI (prev. Swagger) page to send prompt over to API*
<img width="857" alt="openapi" src="https://github.com/user-attachments/assets/59b9f8e6-e8c8-4af1-9ace-ea9e3ef230c6">

*Example Prompt:*
"Context: whimsical comic about a software engineers called Peter and banker called Rob enjoy basking in the sun. Create page where Peter speach bubble reads no problem, rob speach bubble asking about will it be fixed today"

## Resulting image(s)
A comic strip should ideally be 5-10 images, however we here include a more simple illustration. Great for making slack workspaces alive!
![email_fixtoday_slack](https://github.com/user-attachments/assets/d05d16ea-ba5f-4108-83f2-707095c765f8)


## Setting up environment
We suggest creating a virtual environment with venv module that comes with Python.
```
python3 -m venv .venv
```
And run below commands every time starting a new terminal session to work on the project.
```
source .venv/bin/activate
which python
```

## Install requirements
```
pip install -r requirements.txt
```

## Set environment variables
```
export AZURE_STORAGE_ACCOUNT=ukfilestore1
export AZURE_STORAGE_CONTAINER=images
export AZURE_STORAGE_ACCESS_EXPIRY=2024-08-30T12:00:42Z
export AZURE_STORAGE_KEY=
export AZURE_OPENAI_API_KEY=
export AZURE_OPENAI_ENDPOINT=
```

## Start Application
```
uvicorn app:app --reload
```


# Common questions and issues with solutions

## Where do I find Azure Blob API Access Url, Keys, Expiry
Information can be found at settings, security + networking tabs for storage account in Microsoft Azure website

<img width="1248" alt="azure_blob_url" src="https://github.com/user-attachments/assets/6f11c03b-af49-490e-8b50-30cc207740ea">



