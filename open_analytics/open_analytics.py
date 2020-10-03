"""Open Analytics main file."""

import requests
import os


DEFAULT_ENDPOINT = 'https://open-analytics-capture-2lcatg5vxq-ew.a.run.app/capture'

def send_event(project_id):
  project_id = str(project_id) # need to make this an int maybe?
  print("Sending {}".format(project_id))
  endpoint = os.environ.get('OA_CAPTURE_ENDPOINT', DEFAULT_ENDPOINT)

  payload = {"project_id": project_id, "platform": "linux", "version": "3.6.2"}
  r = requests.post(endpoint, json = payload)
  print(r)
  return r
