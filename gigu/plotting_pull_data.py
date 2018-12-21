from gigu.data_handling import DataHandling
import time
import matplotlib.pyplot as plt


class PlottingTools:
    def __init__(self):
        instance = DataHandling('empty', 'empty')
        self.pull_data = instance.open_from_file(
            'pull_info_2018_12_21_012300.json')

    def graph_pulls_per_week(self):
        timestamps = [x['last_updated'] for x in self.pull_data]
        earliest = min(timestamps)

        ts = earliest
        i = 1
        list_x = []
        list_y = []
        while ts <= time.time():
            y = [x for x in self.pull_data
                 if ts <= x['last_updated'] < (ts + 604800)]
            list_x.append(i)
            list_y.append(len(y))
            i -= 1
            ts += 604800

        plt.plot(list_x[::-1], list_y)
        plt.xlabel('Weeks in past')
        plt.ylabel('unclosed pulls')
        plt.show()

    def output_sorted_by_date(self):
        # data_sorted = sorted(self.pull_data, key=lambda k: k['last_updated'])
        return self.pull_data

instance = PlottingTools()
# instance.graph_pulls_per_week()
print(instance.output_sorted_by_date())
print(len(instance.output_sorted_by_date()))
