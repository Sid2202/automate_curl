import json
import requests
import argparse

def load_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError as e:
        print("Error: ", e)


def make_curl_request(url, method, headers=None, params=None):
    try:
        if method == "POST":
            response = requests.post(url, headers=headers, params=params)
        elif method == "PUT":
            response = requests.put(url, headers=headers, params=params)
        response.raise_for_status()
        print("Response: ", response.text)
        print ("Response status code: ", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error: ", e)

def parse_args():
    parser = argparse.ArgumentParser(description="Make a curl request")
    parser.add_argument("file_path", help="JSON file path")
    parser.add_argument("url", help="request url")
    parser.add_argument("method", choices=["POST", "PUT"], help="POST/PUT")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    data = load_json_file(args.file_path)
    # https://httpbin.org/post
    if data:
        make_curl_request(args.url, args.method, headers=None, params=data)