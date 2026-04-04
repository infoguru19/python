import requests
response = requests.get("https://api.github.com/users/lambda", verify = False)

data = response.json()
print(response.status_code)
print(type(data))

followers = data["followers"]
public_repos = data["public_repos"]
sum = int(followers) + int(public_repos)
print(f"Total = {sum}")
