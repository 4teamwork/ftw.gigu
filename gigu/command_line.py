from dotenv import load_dotenv
import os
from github3 import login

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
load_dotenv(os.path.join(BASE_PATH, '.env'))

github_token = os.getenv('GITHUB_TOKEN')

PULL_INFO = []


def main():
    gh = login(token=github_token)
    ftw = gh.organization('4teamwork')
    repos = ftw.repositories()
    for repo in repos:
        for pull in repo.pull_requests():
            if pull.state != 'open':
                continue

            last_updated = pull.updated_at or pull.created_at

            PULL_INFO.append({
                'pull_title': pull.title,
                'last_updated': last_updated,
                'url': pull.html_url,
                'creator': pull.user.login,
                'assignees': [assignee.login for assignee in
                              pull.assignees],
                'reviewers': [reviewer.login for reviewer in
                              pull.requested_reviewers],
            })
    print(PULL_INFO)


if __name__ == '__main__':
    main()
