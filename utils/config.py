from dotenv import load_dotenv
import os


class DataProject:
    load_dotenv()

    TOKEN_GITHUB = os.getenv('TOKEN_GITHUB')
    TOKEN_BOT = os.getenv('TOKEN_GITHUB')
    REPO_NAME = os.getenv('REPO_NAME')
    REPO_OWNER = os.getenv('REPO_OWNER')
    WORKFLOW_ID = os.getenv('WORKFLOW_ID')
    DBNAME = os.getenv('DBNAME')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    USER_NAME = os.getenv('USER_NAME')
    REPO_NAME_API = os.getenv('REPO_NAME_API')
    WORKFLOW_ID_API = os.getenv('WORKFLOW_ID_API')
