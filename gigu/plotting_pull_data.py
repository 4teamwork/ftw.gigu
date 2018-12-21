from gigu.data_handling import DataHandling
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import time


class PlottingTools:
    def __init__(self, file_path):
        self.pull_data = self.open_from_file(file_path)
        self.params = [el for el in mpl.rcParams.keys() if 'size' in el]

    def open_from_file(self, file_path):
        with open(file_path, 'r') as infile:
            data = json.load(infile)
        return data

    def get_creator_list(self):
        creators = list(set(list(map(lambda d: d['creator'], self.pull_data))))
        return creators

    def graph_pulls_per_week(self):
        pull_data_open = [x for x in self.pull_data
                          if x['pull_state'] == 'open']
        timestamps = [x['last_updated'] for x in pull_data_open]
        earliest = min(timestamps)

        ts = earliest
        i = 1
        list_x = []
        list_y = []
        while ts <= time.time():
            y = [x for x in pull_data_open
                 if ts <= x['last_updated'] < (ts + 604800)]
            list_x.append(i)
            list_y.append(len(y))
            i -= 1
            ts += 604800

        plt.figure(figsize=(10, 10))
        plt.bar(list_x[::-1], list_y)
        plt.title('Number of pulls in week now - x')
        plt.xlabel('x\'th week (0 is today)')
        plt.ylabel('unclosed pulls')
        plt.show()

    def average_time_pulls_open_per_user(self):
        x = self.get_creator_list()
        y = []
        for user in x:
            pulls_of_user = [p for p in self.pull_data
                             if p['creator'] == user]
            amount_pulls = len(pulls_of_user)
            time_from_open_to_close = [p['merged'] - p['created']
                                       for p in pulls_of_user
                                       if p['merged']]
            y.append(sum(time_from_open_to_close) / amount_pulls)

        plt.figure(figsize=(10, 14))
        plt.barh(x, y)
        plt.title('Average Time for pulls to merge per user')
        plt.xlabel('Username')
        plt.ylabel('Average time for pulls to merge')
        plt.show()

    def open_pulls_for_username(self):
        x = self.get_creator_list()
        y = []
        for user in x:
            u_pulls = [x for x in self.pull_data if x['creator'] == user
                       and x['pull_state'] == 'open']
            open_pulls = len(u_pulls)
            y.append(open_pulls)

        plt.figure(figsize=(10, 14))
        plt.barh(x, y)
        plt.title('Current open pulls per user')
        plt.xlabel('Username')
        plt.ylabel('Number of open pulls')
        plt.show()
