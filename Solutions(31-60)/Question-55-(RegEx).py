import re

text = '2 cats and 3 dogs.'

ans = re.findall('\d', text)

print(ans)
