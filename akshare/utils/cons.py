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
    # 简化 Headers，移除可能导致风控的复杂静态 Cookie
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Referer": "https://quote.eastmoney.com/center/gridlist.html",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    }
    return headers


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

eastmoney_headers = generate_eastmoney_headers(int(time.time() * 1000))

# 主流浏览器指纹池，用于 curl_cffi 的 impersonate 参数
# 仅保留 curl_cffi 稳定支持的指纹版本
BROWSER_FINGERPRINTS = [
    "chrome110",
    "chrome116",
    "chrome120",
    "edge101",
    "safari15_3",
    "safari15_5",
]

def get_random_impersonate():
    """
    获取随机的浏览器指纹
    """
    return random.choice(BROWSER_FINGERPRINTS)
