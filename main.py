import sys
from runner import Runner
from config import Config
from parser import Parser
from collector import Collector
from exit_codes import EXIT_ERROR, EXIT_SUCCESS

config = Config()
parser = Parser()
collector = Collector()

runner = Runner(config, parser, collector)

#try:
runner.run()

#except TypeError:
#    print('Caught an exception in main thread!')
#    sys.exit(EXIT_ERROR)

sys.exit(EXIT_SUCCESS)
