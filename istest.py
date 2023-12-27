import requests
URL = 'https://i.instagram.com/api/v1/users/176702683/info/'
headers = {'User-Agent':'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)'}
# samsung mobile user-agent

response = requests.get(URL, headers=headers)

print(response.json())