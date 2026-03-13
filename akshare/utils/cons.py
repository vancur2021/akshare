# !/usr/bin/env python
"""
Date: 2024/4/7 15:30
Desc: 通用变量
"""
import time
import random
import urllib.parse
from datetime import datetime

def generate_eastmoney_headers(current_timestamp):
    """
    动态生成东方财富网的请求头
    """
    # 将时间戳相关的 Cookie 进行动态替换，保持设备指纹等静态值不变
    now = datetime.now()
    st_sp_value = urllib.parse.quote(now.strftime("%Y-%m-%d %H:%M:%S"))
    st_psi_prefix = now.strftime('%Y%m%d%H%M%S')
    
    cookies = {
        "fullscreengg": "1",
        "fullscreengg2": "1",
        "qgqp_b_id": "429884edc5b85ea8401f21160c907e9a",
        "st_nvi": "r16kR3c-OfIWTYY6BhtrR5f7b",
        "st_si": str(random.randint(10000000000000, 99999999999999)),
        "nid18": "0f512d6ee90e691d53d979bde12a1561",
        "nid18_create_time": str(current_timestamp),
        "gviem": "MjhKPK929HLSd-Lqf1H3j05ce",
        "gviem_create_time": str(current_timestamp),
        "st_asi": "delete",
        "st_pvi": str(random.randint(10000000000000, 99999999999999)),
        "st_sp": st_sp_value,
        "st_inirUrl": "",
        "st_sn": "2", # 如果在同一会话内连续请求，应递增此值
        "st_psi": f"{st_psi_prefix}36-{random.randint(100000000000, 999999999999)}-{random.randint(1000000000, 9999999999)}"
    }
    
    # 拼接 Cookie 字符串
    cookie_string = "; ".join([f"{k}={v}" for k, v in cookies.items()])

    # 4. 构造 Headers
    headers = {
        "sec-ch-ua-platform": '"macOS"',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
        "sec-ch-ua-mobile": "?0",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "script",
        "Referer": "https://quote.eastmoney.com/center/gridlist.html",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cookie": cookie_string
    }
    return headers


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

eastmoney_headers = generate_eastmoney_headers(int(time.time() * 1000))