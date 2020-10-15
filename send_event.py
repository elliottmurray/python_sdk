#!python

import open_analytics
import time


open_analytics.install_start_event(4, 'pip')

time.sleep(3)

open_analytics.install_end_event(4, 'pip')

