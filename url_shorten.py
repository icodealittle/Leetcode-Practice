"""
2. How do you design a URL Shortening service like goo.gl or bit.ly? (solution)
This one is another common System design question. You have given a (typically)
 long URL, how would you design a service that would generate a shorter and unique alias for it?
  If you are not familiar with URL shortener service have a look at some of the popular ones
  like goo.gl from Google and bit.ly which is used by Twitter.

"""
import os.path
import random
import json
fp = './test.json'
random.seed(random.randint(1, 500))
example_urls = ['https://medium.com/javarevisited/25-software-design-interview-questions-to-crack-any-programming-and'
                '-technical-interviews-4b8237942db0',
                'https://www.bbc.com/news/world-australia-63699882', 'https://www.bestbuy.com/site/samsung-24-led-fhd'
                                                                     '-amd-freesync-monitor-with-bezel-less-design'
                                                                     '-hdmi-d-sub-black/6507352.p?skuId=6507352']
root = 'https://tinylink/'
root_end = '.com'
capture_https = ['https://', 'https://www.']

REDIRECT_STORAGE = {}


def open_JSON(fp):
    if not os.path.exists(fp):
        data = {}
        json.dumps({})
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            return data
    else:
        with open(fp, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data


def write_toJSON(new_url, old_url, fp):
    if os.path.exists(fp):
        data = open_JSON(fp)
        data[new_url] = old_url
    else:
        data = {}
        json.dumps({})
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def grab_url_comp(url: str):
    unique_token = ""
    stop = True
    current_data_keys = open_JSON(fp).keys()
    arr_keys = []
    for key in current_data_keys:
        arr_keys.append(key[len(root):len(root)-1])
    print(arr_keys)
    while stop:
        unique_token = str(input("What token do you want? "))
        if type(unique_token) is str and len(unique_token) > 1 and unique_token not in arr_keys:
            stop = False
            break
        else:
            print("Try again")
    new_link = root + unique_token + root_end
    #fp = './text.json'
    write_toJSON(new_url=new_link.lower(), old_url=url.lower(), fp=fp)
    return new_link.lower()


def link_clicked(key):
    data = open_JSON('./test.json')
    return data[key]


if __name__ == '__main__':
    arr = []
    for url in example_urls:
        arr.append(grab_url_comp(url))
    print(arr)
