import json, sys
d = json.load(sys.stdin)
print('Status:', d.get('status'))
print('URL:', d.get('html_url'))
if d.get('status') is None:
    print('Pages is being deployed... check again in a few minutes.')
else:
    print(f'Pages status: {d["status"]}')
