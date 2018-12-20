from dotenv import load_dotenv
import os
from gigu.data_handling import DataHandling

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
load_dotenv(os.path.join(BASE_PATH, '.env'))

github_token = os.getenv('GITHUB_TOKEN')
organisation = '4teamwork'


def main():
    instance = DataHandling(organisation, github_token)
    instance.collect_open_pull_request_data()
    instance.write_pull_info_to_file()


if __name__ == '__main__':
    main()
