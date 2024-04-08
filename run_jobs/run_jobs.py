from utils.http_metods import HttpMethods
from utils.config import DataProject


class RunJobs:
    secrets = DataProject()

    repo_owner = secrets.REPO_OWNER
    repo_name = secrets.REPO_NAME
    workflow_id = secrets.WORKFLOW_ID
    repo_name_api = secrets.REPO_NAME_API
    workflow_id_api = secrets.WORKFLOW_ID_API
    BASE_URL = f'https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{workflow_id}/dispatches'
    BASE_URL_API = (f'https://api.github.com/repos/'
                    f'{repo_owner}/{repo_name_api}/actions/workflows/{workflow_id_api}/dispatches')

    def post_run_test(self):

        response = HttpMethods.post_token(self.BASE_URL)

        if response.status_code == 204:
            print("Workflow запущен успешно!")
        else:
            print(f"Ошибка: {response.status_code} - {response.text}")

    def post_run_api_test(self):
        response = HttpMethods.post_token(self.BASE_URL_API)

        if response.status_code == 204:
            print("Workflow запущен успешно!")
        else:
            print(f"Ошибка: {response.status_code} - {response.text}")

