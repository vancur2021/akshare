# !/usr/bin/env python
"""
Date: 2024/4/7 15:30
Desc: 通用变量
"""

import time

def generate_eastmoney_headers():
    """
    动态生成东方财富网的请求头
    """
    # 1. 获取当前时间的13位毫秒级时间戳
    current_timestamp = str(int(time.time() * 1000))
    
    # 2. 将 Cookie 拆解为字典，便于动态赋值和后续更新
    # 注：实际工程中，qgqp_b_id、st_nvi 等值通常由上游接口返回或通过JS逆向生成，此处以保留原值为例
    cookies_dict = {
        "qgqp_b_id": "429884edc5b85ea8401f21160c907e9a",
        "st_nvi": "2Zht816xLmdZl-rS5goqaf5fc",
        "nid18": "0735a491c64cc7a7c8e84431e957007a",
        "nid18_create_time": current_timestamp,       # 动态注入时间戳
        "gviem": "VCP6VEi30_fwGKoUZ2tUOe60f",
        "gviem_create_time": current_timestamp,       # 动态注入时间戳
        "fullscreengg": "1",
        "fullscreengg2": "1",
        "wsc_checkuser_ok": "1"
    }
    
    # 3. 将 Cookie 字典格式化为标准的 HTTP Cookie 字符串格式 ("key=value; key=value")
    cookie_string = "; ".join([f"{k}={v}" for k, v in cookies_dict.items()])
    
    # 4. 定义静态常量提取（如需测试不同浏览器，可在此统一修改）
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    sec_ch_ua = "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\""
    
    # 5. 组装最终的 Headers 字典
    headers = {
        "Accept": "*/*",
        # 建议：如果 requests 库未安装 zstd/brotli 支持，建议移除 "br, zstd" 以防止返回乱码
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cookie": cookie_string,  # 注入拼接好的动态 Cookie
        "Referer": "https://quote.eastmoney.com/center/gridlist.html",
        "sec-ch-ua": sec_ch_ua,
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": user_agent,
        "Content-Length": "0"
    }
    
    return headers


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/114.0.0.0 Safari/537.36"
}

eastmoney_headers = generate_eastmoney_headers()