import os
import shutil
import json
import time


class Collector:

    OUTPUT_DIRECTORY = os.path.join(os.path.dirname(__file__), 'reports', str(int(time.time())))

    data = {}

    def __init__(self):
        if os.path.isdir(self.OUTPUT_DIRECTORY):
            shutil.rmtree(self.OUTPUT_DIRECTORY)
        os.makedirs(self.OUTPUT_DIRECTORY)

    def collect(self, key, data):
        self.data[key] = data

    def write_report(self):

        if not self.data:
            print('Nothing to write!')
            os.rmdir(self.OUTPUT_DIRECTORY)
            return

        print('Writing report to ' + self.OUTPUT_DIRECTORY)
        try:
            with open(os.path.join(self.OUTPUT_DIRECTORY, 'data.json'), 'w') as f:
                json.dump(self.data, f, indent=4)
        except IOError:
            print('Failed to save data.json!!!')
        print('Finished writing report!')
