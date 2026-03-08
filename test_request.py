import http.client

conn = http.client.HTTPSConnection("push2.eastmoney.com")

payload = ""

headers = {
    'Accept': "*/*",
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'Accept-Language': "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    'Cookie': "qgqp_b_id=429884edc5b85ea8401f21160c907e9a; st_nvi=2Zht816xLmdZl-rS5goqaf5fc; nid18=0735a491c64cc7a7c8e84431e957007a; nid18_create_time=1771986153207; gviem=VCP6VEi30_fwGKoUZ2tUOe60f; gviem_create_time=1771986153207; fullscreengg=1; fullscreengg2=1; wsc_checkuser_ok=1",
    'Referer': "https://quote.eastmoney.com/center/gridlist.html",
    'sec-ch-ua': 'Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "macOS",
    'Sec-Fetch-Dest': "script",
    'Sec-Fetch-Mode': "no-cors",
    'Sec-Fetch-Site': "same-site",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    }

conn.request("GET", "/api/qt/clist/get?np=1&fltt=1&invt=2&fs=m%3A90%2Bs%3A4%2Bf%3A!50&fields=f12%2Cf13%2Cf14%2Cf1%2Cf2%2Cf4%2Cf3%2Cf152%2Cf20%2Cf8%2Cf104%2Cf105%2Cf128%2Cf140%2Cf141%2Cf207%2Cf208%2Cf209%2Cf136%2Cf222&fid=f3&pn=1&pz=100&po=1&dect=1&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb&_=1772112334325", payload, headers)

res = conn.getresponse()
data = res.read()

print(data)