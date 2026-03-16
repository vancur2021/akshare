# !/usr/bin/env python
"""
Date: 2025/3/10 18:00
Desc: 通用帮助函数
"""

import json
import math
import random
import time
from typing import List, Dict

import pandas as pd
# import requests
from curl_cffi import requests
from akshare.utils.cons import eastmoney_headers
from akshare.utils.tqdm import get_tqdm


def _parse_jsonp(text: str) -> dict:
    """解析 JSONP 格式的响应文本"""
    start = text.find('(')
    end = text.rfind(')')
    if start != -1 and end != -1:
        json_str = text[start + 1:end]
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            pass
    # 如果没有找到括号或者解析失败，尝试直接作为 JSON 解析
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}


def fetch_paginated_data(url: str, base_params: Dict, timeout: int = 15, header:dict=eastmoney_headers):
    """
    东方财富-分页获取数据并合并结果
    https://quote.eastmoney.com/f1.html?newcode=0.000001
    :param url: 股票代码
    :type url: str
    :param base_params: 基础请求参数
    :type base_params: dict
    :param timeout: 请求超时时间
    :type timeout: str
    :return: 合并后的数据
    :rtype: pandas.DataFrame
    """
    # 复制参数以避免修改原始参数
    params = base_params.copy()
    # 获取第一页数据，用于确定分页信息
    r = requests.get(url, params=params, headers=header, impersonate="chrome120", timeout=timeout)
    data_json = _parse_jsonp(r.text)
    
    if not data_json or "data" not in data_json or data_json["data"] is None or "diff" not in data_json["data"]:
        return pd.DataFrame()
        
    diff_data = data_json["data"]["diff"]
    if not diff_data:
        return pd.DataFrame()
        
    # 计算分页信息
    per_page_num = len(diff_data)
    total_page = math.ceil(data_json["data"]["total"] / per_page_num)
    
    # 存储所有页面数据
    temp_list = [pd.DataFrame(diff_data)]
    
    # 获取进度条
    tqdm = get_tqdm()
    # 获取剩余页面数据
    for page in tqdm(range(2, total_page + 1), leave=False):
        time.sleep(random.uniform(0.3, 1.5))
        params.update({"pn": page})
        r = requests.get(url, params=params, headers=header, impersonate="chrome120", timeout=timeout)
        data_json = _parse_jsonp(r.text)
        if data_json and "data" in data_json and data_json["data"] is not None and "diff" in data_json["data"]:
            inner_temp_df = pd.DataFrame(data_json["data"]["diff"])
            if not inner_temp_df.empty:
                temp_list.append(inner_temp_df)
                
    # 合并所有数据
    if not temp_list:
        return pd.DataFrame()
        
    temp_df = pd.concat(temp_list, ignore_index=True)
    
    if "f3" in temp_df.columns:
        temp_df["f3"] = pd.to_numeric(temp_df["f3"], errors="coerce")
        temp_df.sort_values(by=["f3"], ascending=False, inplace=True, ignore_index=True)
        
    temp_df.reset_index(inplace=True)
    temp_df["index"] = temp_df["index"].astype(int) + 1
    return temp_df


def set_df_columns(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    """
    设置 pandas.DataFrame 为空的情况
    :param df: 需要设置命名的数据框
    :type df: pandas.DataFrame
    :param cols: 字段的列表
    :type cols: list
    :return: 重新设置后的数据
    :rtype: pandas.DataFrame
    """
    if df.shape == (0, 0):
        return pd.DataFrame(data=[], columns=cols)
    else:
        df.columns = cols
        return df
