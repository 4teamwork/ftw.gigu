import os
import time
from github3 import login


class DataHandling:
    def __init__(self, organisation, github_token):
        self.pull_info = []
        self.file_path = None
        self.organisation = organisation
        self.github_token = github_token

    def collect_open_pull_request_data(self):
        """
        Create a list of dictionaries having info of each unclosed pull request.
        :return: None
        """
        gh = login(token=self.github_token)
        ftw = gh.organization(self.organisation)
        repos = ftw.repositories()
        for repo in repos:
            for pull in repo.pull_requests():
                if pull.state != 'open':
                    continue

                last_updated = pull.updated_at or pull.created_at

                self.pull_info.append({
                    'pull_title': pull.title,
                    'last_updated': last_updated,
                    'url': pull.html_url,
                    'creator': pull.user.login,
                    'assignees': [assignee.login for assignee in
                                  pull.assignees],
                    'reviewers': [reviewer.login for reviewer in
                                  pull.requested_reviewers],
                })

    def get_pull_info(self):
        """
        Getter function for unclosed pull request data.
        :return: list of dicts for each unclosed pull request.
        """
        return self.pull_info

    def write_pull_info_to_file(self):
        """
        Create a file containing the data from unclosed pull requests.
        :return: filepath of file created
        """
        filename = 'pull_info_{}.data'.format(
            time.strftime('%Y_%m_%d_%H%M%S', time.gmtime()))
        current_path = os.path.dirname(os.path.abspath(__file__))
        self.file_path = current_path + '/reports/' + filename

        with open(self.file_path, 'w+') as file_:
            file_.write(str(self.pull_info))

        return self.file_path
