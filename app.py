from config import vuln_app
from flask import Flask, send_from_directory
import os

'''
 Decide if you want to server a vulnerable version or not!
 DO NOTE: some functionalities will still be vulnerable even if the value is set to 0
          as it is a matter of bad practice. Such an example is the debug endpoint.
'''
vuln = int(os.getenv('vulnerable', 1))
# vuln=1
# token alive for how many seconds?
alive = int(os.getenv('tokentimetolive', 60))

app = vuln_app
@app.route('/openapi_specs/openapi3.yml')
def serve_openapi_spec():
    return send_from_directory('openapi_specs', 'openapi3.yml')


# start the app with port 5000 and debug on!
if __name__ == '__main__':
    vuln_app.run(host='0.0.0.0', port=5000, debug=True)
