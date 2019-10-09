#!/usr/bin/env python3

import urllib.request
import json
import pprint
import sys

def human_size(size, decimal_places=3):
	for unit in ['Bytes','KiB','MiB','GiB','TiB']:
		if size < 1024.0:
			break
		size /= 1024.0
	return f"{size:.{decimal_places}g} {unit}"

rawResponse = urllib.request.urlopen('https://api.github.com/repos/MyHumanoid/MyHumanoid/releases').read()
releases = json.loads(rawResponse)
#pprint.pprint(releases[0])

latestRelease = releases[0]

with open('releases.html', 'w') as f:
	f.write('<!doctype html>\n')
	f.write('<head><link href="releases.css" rel="stylesheet"/></head>\n')
	f.write('<body>\n')
	f.write('<span>{}</span>\n'.format(latestRelease['created_at']))
	for asset in latestRelease['assets']:
		f.write('<a href="{}"><span class="asset-name">{}</span><span class="asset-size">{}</span></a>\n'.format(
			asset['browser_download_url'],
			asset['name'],
			human_size(asset['size'])))
	f.write('</body>\n')

print('Generated releases.html')
