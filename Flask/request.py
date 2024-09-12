import requests

data1 = {'post_text': 'Today, I started learning Python. Exciting!'}
r = requests.post('http://bestblogever.com/posts', data=data1)
print(f"POST response: {r.status_code}, {r.text}")

data2 = {'post_text': 'some_updated_text'}
r = requests.put('http://bestblogever.com/posts/<post_id>', data=data2)
print(f"PUT response: {r.status_code}, {r.text}")

r = requests.delete('http://bestblogever.com/posts/<post_id>')
print(f"DELETE response: {r.status_code}, {r.text}")