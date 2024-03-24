from utils.http_metods import HttpMethods
from utils.config import DataProject


class RunJobs:
    secrets = DataProject()

    repo_owner = secrets.REPO_OWNER
    repo_name = secrets.REPO_NAME
    workflow_id = secrets.WORKFLOW_ID
    BASE_URL = f'https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{workflow_id}/dispatches'

    def post_run_test(self):

        response = HttpMethods.post_token(self.BASE_URL)

        if response.status_code == 204:
            print("Workflow запущен успешно!")
        else:
            print(f"Ошибка: {response.status_code} - {response.text}")
