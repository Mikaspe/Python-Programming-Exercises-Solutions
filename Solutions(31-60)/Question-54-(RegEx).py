import re

email = 'john@google.com'

ans = re.findall('\w+@(\w+)', email)

print(ans)
