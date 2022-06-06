import requests
import time
from faker import Faker


def voter(fake_ip):
    fake_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        'Referer': 'https://pubgesports.com/pnc2022/cn/promotion',
        'x-forwarded-for': fake_ip,
    }
    url = "https://pubgesports.com/v1/pnc/postClickCountry?country=china"
    data = {
        "country": "china",
    }
    se = requests.session()
    se.headers.update(fake_header)
    res = se.post(url, json=data)
    if res.status_code == 200:
        if res.json()['result'] == 1:
            print("票数+1")
            return 0
        print("此ip暂时不能投票")
        return -1
    print(f"error code:{res.status_code}")
    return -1


if __name__ == "__main__":
    num_to_vote = 100   # 票数
    fake = Faker()
    for i in range(num_to_vote):
        num_to_vote += voter(fake.ipv4_public())
        time.sleep(0.1)  # 间隔0.1s
    print(f"共为中国队投出{num_to_vote}票")
