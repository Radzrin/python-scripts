import requests

url = f"https://api.pjsek.ai/database/user/userHomeBanners?startAt[$lte]=1738688518486&endAt[$gte]=1738688518486&$sort[seq]=1"
response = requests.get(url)
print(response)



