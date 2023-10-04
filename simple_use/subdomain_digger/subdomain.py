# -*- coding: UTF-8 -*-
import argparse
import requests
import tld

bannerText = """


  /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$$  /$$  /$$$$$$  /$$   /$$
 /$$_____/ /$$_____/ /$$__  $$| $$__  $$|__/ /$$__  $$| $$  | $$
|  $$$$$$ | $$      | $$$$$$$$| $$  \ $$ /$$| $$  \ $$| $$  | $$
 \____  $$| $$      | $$_____/| $$  | $$| $$| $$  | $$| $$  | $$
 /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$| $$|  $$$$$$/|  $$$$$$$
|_______/  \_______/ \_______/|__/  |__/| $$ \______/  \____  $$
                                   /$$  | $$           /$$  | $$
                                  |  $$$$$$/          |  $$$$$$/
                                   \______/            \______/ 

"""
def url_parser(url):
    return tld.get_fld(url)

def domain_digger(domain):
    with open("list", "r", encoding="utf-8") as f:
        for sub in f:
            sub = sub.strip()
            subdomain = sub + "." +domain
            # print(subdomain)

def domain_burst(subdomain):
    try:
        response = requests.get(subdomain)
        code = response.status_code
        if code == 200 or code == 301:
            print(f"dig success , the domain is {subdomain}")
        else:
            pass
    except Exception as e:
        print(e)
        raise


if __name__ == '__main__':
    # url = "https://ftp.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx"
    # domain = url_parser(url)
    # domain_digger(domain)
    # print(domain)

    print(bannerText)

    parser = argparse.ArgumentParser("")
    parser.add_argument("-u", "--url", help="please put your url here", required=True)
    args = parser.parse_args()
    print(args)
    url = args.url

    domain = url_parser(url)
    domain_digger(domain)


