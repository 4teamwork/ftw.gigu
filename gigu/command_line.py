from dotenv import load_dotenv
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
load_dotenv(os.path.join(BASE_PATH, '.env'))

github_token = os.getenv('GITHUB_TOKEN')

def main():
    pass


if __name__ == '__main__':
    main()
