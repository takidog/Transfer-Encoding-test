import requests
import sys
if __name__ == "__main__":
    req = requests.get('http://127.0.0.1:{port}'.format(port=sys.argv[1]))
    print(req.status_code)
    print(req.text)
