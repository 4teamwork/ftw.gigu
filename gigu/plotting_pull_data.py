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

    def plot_data(self, plot_data, plot_type, figsize, title, xlabel, ylabel):
        x = [el[0] for el in plot_data]
        y = [el[1] for el in plot_data]

        plt.figure(figsize=figsize)
        if plot_type == 'barh':
            plt.barh(x, y)
        else:
            plt.bar(x, y)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

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

        list_x = list_x[::-1]
        plot_data = [(x, list_y[i]) for i, x in enumerate(list_x)]
        title = 'Number of pulls in week now - x'
        xlabel = 'x\'th week (0 is today)'
        ylabel = 'unclosed pulls'
        self.plot_data(plot_data, 'bar', (10, 10), title, xlabel, ylabel)

    def average_time_pulls_open_per_user(self):
        plot_data = []
        for user in self.get_creator_list():
            pulls_of_user = [p for p in self.pull_data
                             if p['creator'] == user]
            amount_pulls = len(pulls_of_user)
            time_from_open_to_close = [p['merged'] - p['created']
                                       for p in pulls_of_user
                                       if p['merged']]
            av_time = sum(
                time_from_open_to_close) / amount_pulls / 60 / 60 / 24
            plot_data.append((user, av_time))

        title = 'Average Time for pulls to merge per user'
        xlabel = 'Average time for pulls to merge (d)'
        ylabel = 'Username'
        plot_data = filter(lambda item: item[1], plot_data)
        plot_data = list(sorted(plot_data, key=lambda item: item[1]))
        self.plot_data(plot_data, 'barh', (10, 14), title, xlabel, ylabel)

    def open_pulls_for_username(self):
        plot_data = []
        for user in self.get_creator_list():
            u_pulls = [x for x in self.pull_data if x['creator'] == user
                       and x['pull_state'] == 'open']
            open_pulls = len(u_pulls)
            plot_data.append((user, open_pulls))

        title = 'Current open pulls per user'
        xlabel = 'Number of open pulls'
        ylabel = 'Username'
        plot_data = filter(lambda item: item[1], plot_data)
        plot_data = list(sorted(plot_data, key=lambda item: item[1]))
        self.plot_data(plot_data, 'barh', (10, 14), title, xlabel, ylabel)
