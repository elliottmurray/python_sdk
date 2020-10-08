#!python

from open_analytics.open_analytics import *
import sys

if(len(sys.argv) < 2):
    print("Need a project id")
    exit(-1)

project_id = str(sys.argv[1])

print(f'Sending project event {project_id}')

send_event(project_id)

print(f'sent event')

