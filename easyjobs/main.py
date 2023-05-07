import threading

from linkedin import *
from indeed import *


class AutoApply(threading.Thread):
    def __init__(self, config):
        super(AutoApply, self).__init__()
        Indeed(config, name="Indeed").application_loop()
        LinkedIn(config, name="LinkedIn").application_loop()
        return
