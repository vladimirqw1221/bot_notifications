from dotenv import load_dotenv
import os
from utils.http_metods import HttpMethods

load_dotenv()


class RunJobs:
    repo_owner = os.getenv('REPO_OWNER')
    repo_name = os.getenv('REPO_NAME')
    workflow_id = os.getenv('WORKFLOW_ID')
    BASE_URL = f'https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{workflow_id}/dispatches'

    def post_run_test(self):

        response = HttpMethods.post_token(self.BASE_URL)

        if response.status_code == 204:
            print("Workflow запущен успешно!")
        else:
            print(f"Ошибка: {response.status_code} - {response.text}")
