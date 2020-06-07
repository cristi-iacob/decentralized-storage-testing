import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, source):
        self.source = source
        self.x_axis = []
        self.y_axis = []
        self.mean = []

    def read_data(self):
        with open(self.source, 'r') as samples:
            cnt = 0
            for line in samples:
                cnt += 1
                self.x_axis += [cnt]
                self.y_axis += [int(line.split(',')[1])]

    def plot(self):
        self.read_data()
        plt.xlabel('Simulation index')
        plt.ylabel('Number of failed downloads')
        plt.plot(self.x_axis, self.y_axis)
        mean = [sum(self.y_axis) / len(self.y_axis)] * len(self.y_axis)
        plt.plot(self.x_axis, mean, label='Mean number of failures')
        plt.legend()
        plt.savefig(self.source + '.png')
