import boto3
from botocore.client import Config
from dotenv import load_dotenv

load_dotenv()
svc = boto3.client('s3',
                endpoint_url='https://fly.storage.tigris.dev',
                config=Config(s3={"addressing_style": "virtual"}))

response = svc.list_buckets()

def upload_prompts():
    # 업로드
    svc.upload_file('./prompts/prompt-page1.txt', 'repods-gpt','prompts/prompt-page1.txt')
    svc.upload_file('./prompts/prompt-page2.txt', 'repods-gpt','prompts/prompt-page2.txt')
    svc.upload_file('./prompts/prompt-page3.txt', 'repods-gpt','prompts/prompt-page3.txt')
    svc.upload_file('./prompts/prompt-page4.txt', 'repods-gpt','prompts/prompt-page4.txt')

def download_prompts():
    svc.download_file('repods-gpt', 'prompts/prompt-page1.txt', 'prompts/prompt-page1.txt')
    svc.download_file('repods-gpt', 'prompts/prompt-page2.txt', 'prompts/prompt-page2.txt')
    svc.download_file('repods-gpt', 'prompts/prompt-page3.txt', 'prompts/prompt-page3.txt')
    svc.download_file('repods-gpt', 'prompts/prompt-page4.txt', 'prompts/prompt-page4.txt')
