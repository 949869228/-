# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:29:51 2018

@author: john
"""
import requests
from bs4 import BeautifulSoup
import os

'''
类说明：下载人教网高中语文教师用书
目标网址：http://old.pep.com.cn/gzyw/jszx/tbjxzy/kbjc/jsys/
Parameter：无
Return：无
Modify：2018-1-24
'''


class downloder(object):
    def __init__(self):
        self.serve = 'http://old.pep.com.cn/gzyw/jszx/tbjxzy/kbjc/jsys'
        self.target = 'http://old.pep.com.cn/gzyw/jszx/tbjxzy/kbjc/jsys'
        self.books = []  # 存放书本名
        self.urls_book = []  # 存放书籍链接
        self.names = []  # 存放章节名
        self.urls = []  # 存放章节链接
        self.nums = 0  # 章节数

    '''
    函数说明：获取book下载链接
    Parameterw:无
    Return:无
    Modify:2018-1-24
    '''

    def get_download_book(self):
        req = requests.get(url=self.target)
        html = req.text
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_='seperator5')
        A_bf = BeautifulSoup(str(div))
        A = A_bf.find_all('a')
        for each in A:
            self.books.append(each.text)
            self.urls_book.append(self.serve + each.get('href')[1:])

    '''
    函数说明：获取文章下载链接
    Parameterw:target-书籍地址；books-书籍名称
    Return:无
    Modify:2018-1-24
    '''

    def get_download_url(self, target):
        self.names = []
        self.urls = []
        req = requests.get(url=target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_='ttlist_nodot')
        a_bf = BeautifulSoup(str(div))
        a = a_bf.find_all('a')
        for each in a:
            self.names.append(each.text.replace('\n', '').replace('\t', '').replace('\u3000', ''))
            self.urls.append(target + each.get('href')[2:])

    '''
    函数说明：获取文章内容
    parameter:
    Return:
    Modify:2018-1-24
    '''

    def get_contents(self, target):
        req = requests.get(url=target)
        html = req.content
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_='seperator10')
        return str(texts[0])

    '''
    函数说明：文件夹检查及创建
    参数：
    return：
    Modify：2018-1-24   
    '''

    def create_os(self, book):
        isExists = os.path.exists(book)
        if not isExists:
            os.makedirs(book)

    '''
    函数说明：写入本地
    Parameters:book-文件夹名称，
                name-章节名称；
                path-当前路径下，小说保存的名称；
                text-章节内容
    Returns:无
    Modify：2018-1-24
    '''

    def writer(self, book, name, path, text):
        with open(book + '/' + path, 'a', encoding='utf-8')as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


'''        
if __name__=='__main__':
    dl=downloder()
    dl.get_download_book()
    for i in range(len(dl.books)):
        dl.create_os(dl.books[i])
        target=dl.urls_book[i]
        dl.get_download_url(target)
        for j in range(dl.nums):
            dl.writer(dl.books[i],dl.names[j],dl.names[j],dl.get_contents(dl.urls[j]))
'''

dl = downloder()
dl.get_download_book()
for i in range(len(dl.books)):
    dl.create_os(dl.books[i])
    target = dl.urls_book[i]
    dl.get_download_url(target)
    for j in range(len(dl.names)):
        dl.writer(dl.books[i], dl.names[j], dl.names[j], dl.get_contents(dl.urls[j]))

'''
#测试代码
dl=downloder()
dl.get_download_book()
dl.create_os(dl.books[0])
target=dl.urls_book[0]
dl.get_download_url(target)
dl.writer(dl.books[0],dl.names[1],dl.names[1],dl.get_contents(dl.urls[1]))
'''