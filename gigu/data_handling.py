from github3 import login
import json
import os
import time


class DataHandling:
    def __init__(self, organisation, github_token):
        self.pull_info = []
        self.file_path = None
        self.organisation = organisation
        self.github_token = github_token

    def collect_open_pull_request_data(self):
        """
        Create a list of dictionaries having info of each pull request.
        :return: None
        """
        gh = login(token=self.github_token)
        ftw = gh.organization(self.organisation)
        repos = ftw.repositories()
        for repo in repos:
            for pull in repo.pull_requests('all'):
                last_updated = pull.updated_at or pull.created_at

                self.pull_info.append({
                    'pull_state': pull.state,
                    'pull_title': pull.title,
                    'last_updated': last_updated.timestamp() if last_updated else None,
                    'url': pull.html_url,
                    'creator': pull.user.login,
                    'created': pull.created_at.timestamp() if pull.created_at else None,
                    'merged': pull.merged_at.timestamp() if pull.merged_at else None,
                    'assignees': [assignee.login for assignee in
                                  pull.assignees],
                    'reviewers': [reviewer.login for reviewer in
                                  pull.requested_reviewers],
                })

    def get_pull_info(self):
        """
        Getter function for pull request data.
        :return: list of dicts for each pull request.
        """
        return self.pull_info

    def write_pull_info_to_file(self):
        """
        Create a file containing the data from pull requests.
        :return: filepath of file created
        """
        filename = 'pull_info_{}.json'.format(
            time.strftime('%Y_%m_%d_%H%M%S', time.gmtime()))
        current_path = os.path.dirname(os.path.abspath(__file__))
        self.file_path = current_path + '/reports/' + filename

        with open(self.file_path, 'w+') as outfile:
            json.dump(self.pull_info, outfile)

        return self.file_path

    def open_from_file(self, filename=None):
        """
        Get pull request data from existing json file
        :param filename: json pull request data filename
        :return: pull request data
        """
        if filename is None:
            file_path = self.file_path
        else:
            current_path = os.path.dirname(os.path.abspath(__file__))
            file_path = current_path + '/reports/' + filename

        with open(file_path, 'r') as infile:
            data = json.load(infile)

        return data
