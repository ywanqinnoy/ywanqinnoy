import requests
import pandas as pd
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
resp

data = resp.json()
print(data)
data[0]['title']

issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
issues
