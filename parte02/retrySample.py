from retry import retry
import requests as r


@retry()
def request_api():
    response = r.get('http://localhost:5000')
    if response.status_code != 200:
        raise Exception("Deu ruim")
    else:
        print(response.text)


if __name__ == "__main__":
    request_api()
