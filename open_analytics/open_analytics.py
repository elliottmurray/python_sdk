"""Open Analytics main file."""

import requests
import os
import platform

print(os.name)
DEFAULT_ENDPOINT = 'https://open-analytics-capture-2lcatg5vxq-ew.a.run.app/capture'

def send_event(project_id):
  import os
  import platform

  project_id = str(project_id) # need to make this an int maybe?
  print("Sending {}".format(project_id))
  endpoint = os.environ.get('OA_CAPTURE_ENDPOINT', DEFAULT_ENDPOINT)

  system = platform.system() #'Windows'
  os_release = platform.release()
  os_version = platform.version()
  os = {
    "platform": system,
    "release": os_release,
    "version": os_version,
  }
# 5.1.2600'
  print(endpoint)
  payload = {"project_id": project_id, "version": "3.6.2", "os": os}
  r = requests.post(endpoint, json = payload)
  print(r)
  return r
