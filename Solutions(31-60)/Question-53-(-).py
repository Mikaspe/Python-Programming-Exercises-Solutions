import re

email = input('Email address:')
pattern = '(\w+)@\w+.com'
ans = re.findall(pattern, email)
print(ans)