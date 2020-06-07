import os

import command_file_executor as exec
import command_file_generator as gen
from plotter import Plotter
from request_handler import Requests as req


class MassExecutor:
    def __init__(self, name, simulation_number, probs=None):
        self.name = name
        self.simulation_number = simulation_number
        try:
            os.mkdir(name[:4])
        except Exception:
            pass

        self.result_file = open(os.path.join(name[:4], self.name + 'res'), 'w')
        self.probs = probs

    def generate_command_files(self):
        for i in range(self.simulation_number):
            generator = gen.SimmulationGenerator(self.name[:4] + '/' + self.name + str(i), self.probs)
            generator.simulate()

    def write_execution_result(self, executor):
        self.result_file.write(str(executor.good_downloads) + ',' + str(executor.bad_downloads) + ',' + str(executor.uploads) + '\n')
        self.result_file.flush()

    def execute_command_files(self):
        for i in range(self.simulation_number):
            req.send_all_offline_request()
            executor = exec.Executor(self.name[:4] + '/' + self.name + str(i))
            executor.execute_commands()
            self.write_execution_result(executor)
        self.generate_chart(self.name[:4] + '/' + self.name)

    def generate_chart(self, name):
        plotter = Plotter(name + 'res')
        plotter.plot()
