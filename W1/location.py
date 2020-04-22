import requests

def get_location_info():
	return requests.get("https://ipapi.co/8.8.8.8/json/").json()


if __name__ == "__main__":
	print(get_location_info())