from dotenv import load_dotenv
from gigu.data_handling import DataHandling
from gigu.plotting_pull_data import PlottingTools
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
load_dotenv(os.path.join(BASE_PATH, '.env'))

github_token = os.getenv('GITHUB_TOKEN')
organisation = '4teamwork'


def main():
    data_instance = DataHandling(organisation, github_token)
    data_instance.collect_open_pull_request_data()
    file_path = data_instance.write_pull_info_to_file()

    plot_instance = PlottingTools(file_path)
    plot_instance.graph_pulls_per_week()
    plot_instance.average_time_pulls_open_per_user()
    plot_instance.open_pulls_for_username()


if __name__ == '__main__':
    main()
