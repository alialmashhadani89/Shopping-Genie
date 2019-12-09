# We gonna put all the code for hiding activities here.
#from torrequest import TorRequest

#tr = TorRequest(password="hashpass")
agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 1.0.3705)",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; rv:11.0) like Gecko",
    "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",
    "Opera/9.80 (Linux armv7l) Presto/2.12.407 Version/12.51 , D50u-D1-UHD/V1.5.16-UHD (Vizio, D50u-D1, Wireless)",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3198.0 Safari/537.36 OPR/49.0.2711.0",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36 OPR/36.0.2130.80",
    "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0"
    ]

user_agents = []

#class Proxy:
#    def __init__(self, ip, port):
#        self.proxy = "http://" + ip + ":" + port
#
#    def getProxy(self):
#        return self.proxy

proxies = []#[
    #{ "http": "http://209.90.63.108:80",
    #  "https": "http://209.90.63.108:80"},
    #{ "http": "http://35.163.85.149:80",
    #  "https": "http://35.163.85.149:80"},
    #{ "http": "http://23.237.173.109:3128",
    #  "https": "http://23.237.173.109:3128"},
    #{ "http": "http://159.203.81.37:8080",
    #  "https": "http://159.203.81.37:8080"},
    #{ "http": "http://208.88.253.8:8080",
    #  "https": "http://208.88.253.8:8080"}
    #]

def getFirst():

    #plist = ["http://76.76.76.74:53281",
    #         "http://49.51.193.134:1080",
    #         "http://166.249.185.136:57680",
    #         "http://207.191.15.166:38528",
    #         "http://49.51.195.24:1080",
    #         "http://74.87.75.58:8080"]

    #for p in plist:
    #    proxies.append({"http": p,
    #                    "https": p})

    for h in agents:
        user_agents.append({
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    #"Host": "httpbin.org",
    "Referer": "https://google.com",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": h
  })
    firstPackage = {
        #"tr": tr,
        "user_agent": user_agents[0],
        "ua_id": 0,
        "count": 0
    }

    #print(firstPackage)

    return firstPackage

def getNewPackage( ua_id):
    #print("TIME FOR PACKAGE CHANGE")
    #new_proxy_id = proxy_id + 1
    #if new_proxy_id >= len(proxies):
    #    new_proxy_id = 0

    new_ua_id = ua_id + 1
    if new_ua_id >= len(user_agents):
        new_ua_id = 0
    #tr.reset_identity()
    newPackage = {
        #"tr": tr,
        "user_agent": user_agents[new_ua_id],
        "ua_id": new_ua_id,
        "count": 0
    }
    #print(newPackage)
    # a
    return newPackage

# An attempt to do proxy and user agent rotation
# @param  package  A combination of user agent and proxy, in dictionary form
# @param  count  How often the given package has been used
def getPackage(package):

    #print("Pre Package")
    #print(package)
    if package == None:
        return getFirst()

    if package["count"] >= 3:
        return getNewPackage(package["ua_id"])

    else:
        package["count"] += 1
        return package
