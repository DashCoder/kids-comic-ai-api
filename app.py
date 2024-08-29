# Required Environment variables
# export AZURE_STORAGE_ACCOUNT=ukfilestore1
# export AZURE_STORAGE_CONTAINER=images
# export AZURE_STORAGE_ACCESS_EXPIRY=2024-08-30T12:00:42Z
# export AZURE_STORAGE_KEY=
# export AZURE_OPENAI_API_KEY=
# export AZURE_OPENAI_ENDPOINT=

import os
from openai import AzureOpenAI
import json
import requests
from fastapi import FastAPI
from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import generate_container_sas
from azure.storage.blob import ContainerSasPermissions
from azure.storage.blob import ContainerClient
from pydantic import BaseModel

class Picture(BaseModel):
    blobName: str
    prompt: str


app = FastAPI()


@app.post("/picture/")
async def create_image(pic: Picture):
	blob_storage_account = os.environ["AZURE_STORAGE_ACCOUNT"]
	blob_storage_container = os.environ["AZURE_STORAGE_CONTAINER"]
	ai_key = os.environ["AZURE_OPENAI_API_KEY"]
	blob_account_key = os.environ["AZURE_STORAGE_KEY"]
	blob_account_access_expiry = os.environ["AZURE_STORAGE_ACCESS_EXPIRY"]
	permission = ContainerSasPermissions(read=True, write=True, delete=False,
		list=True, delete_previous_version=False, tag=True)

	container_sas_token = generate_container_sas(
		account_name=blob_storage_account,
		container_name=blob_storage_container,
		account_key=blob_account_key,
		permission=permission,
		expiry=blob_account_access_expiry
	    )

	url = "https://"+blob_storage_account+".blob.core.windows.net/"+blob_storage_container
	container_client = ContainerClient.from_container_url(
		container_url=url,
		credential=container_sas_token
	)

	client = AzureOpenAI(
		api_version="2024-05-01-preview",
		azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
		api_key=os.environ["AZURE_OPENAI_API_KEY"],
	)

	result = client.images.generate(
		model="Dalle3", # name of your DALL-E 3 deployment
		prompt=pic.prompt,
		n=1
	)

	image_url = json.loads(result.model_dump_json())['data'][0]['url']

	img_data = requests.get(image_url).content
	# Optional: Save image locally
	# with open(pic.blobName, 'wb') as handler:
	#     handler.write(img_data)

	# Upload to blob storage
	blob_client = container_client.get_blob_client(blob = pic.blobName)
	blob_client.upload_blob(img_data, blob_type="BlockBlob") 

	return pic
