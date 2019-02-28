import re

str_a = '"objURL": "http://test.com.jpg"'
r = re.compile(r'"objURL": "(.*?)"')
res = re.findall(r, str_a)
print(res)
