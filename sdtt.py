#!/usr/bin/env python3

import json
import requests
import sys

if len(sys.argv) < 2:
    print('You must pass a URL as the first argument.')
    exit(1)

# Variables
tool_origin='search.google.com'
tool_url='https://search.google.com/structured-data/testing-tool/validate'
tool_referer='https://search.google.com/structured-data/testing-tool'
user_agent='SDTT-Local/1.0 (+https://github.com/psychology-tools/sdtt/)'

# Headers
headers = {
    'User-Agent': user_agent,
    'Accept': 'application/json',
    'Referer': tool_referer,
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Origin': tool_origin,
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

# Get local source
local = requests.get( sys.argv[1] ).text

# Post source to tool
response = requests.post(url=tool_url, headers=headers, data={'html': local})

# Parse response
data = json.loads(response.text.split('\n')[1])    # response is broken json before the line break for some reason...
html = requests.utils.unquote('{}'.format(data.pop('html')))

# Print results
print('-----SUMMARY-----\nStructures: {}\nErrors: {}\nWarnings: {}\n'.format(
    data.get('numObjects'),
    data.get('totalNumErrors'),
    data.get('totalNumWarnings')
))

n = 0
# Loop errors
for error in data.get('errors'):
    code = html[error.get('begin'):error.get('end')]
    data['errors'][n]['code'] = code
    print('-----ERROR (#{})-----\n{}\n'.format(n, code))
    n = n + 1

# Dump the response (minus original HTML) as JSON
#print(json.dumps(data))

