#!/usr/local/bin/python3
#coding:utf-8

import sys
import re
import urllib
# import shutil
from urllib import request
from bs4 import BeautifulSoup

md_file = sys.argv[1]   # 运行参数：md地址
# new_md = sys.argv[1][0:-3] + '_copy.md'
# shutil.copyfile(sys.argv[1], new_md)
post = None
# 读文件 使用utf-8 编码打开
with open(md_file, 'r', encoding='utf-8') as f:
    post = f.read()
    # 列表
    matches = re.compile(r'(\t?<li>(.*?)</li>)').findall(post)
    for match in matches:
      md = '- {0}'.format(match[1])
      post = post.replace(match[0], md)
    post = post.replace('<ul>', '\n')
    post = post.replace('</ul>', '\n')
    # 引用
    matches = re.compile(r'(<blockquote>(.*?)</blockquote>)').findall(post)
    for match in matches:
      md = '> {0}'.format(match[1])
      post = post.replace(match[0], md)
    # 加粗标签
    matches = re.compile(r'(<strong>(.*?)</strong>)').findall(post)
    for match in matches:
      md = '**{0}**'.format(match[1])
      post = post.replace(match[0], md)
    # 替换a链接
    matches = re.compile(r'(<a href="(.*?)".*?>(.*?)</a>)').findall(post)
    for match in matches:
        md = '[{0}]({1})'.format(match[2], match[1])
        post = post.replace(match[0], md)
    # 替换img链接
    matches = re.compile(r'(<img src="(.*?)".*?/>)').findall(post)
    for match in matches:
        md = '\n![]({0})'.format(match[1])
        post = post.replace(match[0], md)
    matches = re.compile(r'(<span.*?>)').findall(post)
    for match in matches:
      post = post.replace(match, '')
    post = post.replace('</span>', '')
    # 链接转为脚注
    matches = re.compile('[^!]\\[.*?\\](\(.*?\\))').findall(post)
    matches_no_repeat = list(set(matches))
    matches_no_repeat.sort(key=matches.index)
    matches = matches_no_repeat
    index = 0
    post += '\n';
    for match in matches:
        index = index + 1
        url = match[1:-1]
        footnote_mark = '[{0}]'.format(index)
        post = post.replace(match, footnote_mark)
        footnote_line = '\n'+footnote_mark + ': ' + url
        post = post + footnote_line
# 写入
open(md_file, 'w', encoding='utf-8').write(post)
