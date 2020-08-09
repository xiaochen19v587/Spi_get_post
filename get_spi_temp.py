# 导入需要用到的模块
import requests
from fake_useragent import UserAgent
import random
from lxml import etree

# 创建类
class Get_Spi_text():
    # 定义类属性
    def __init__(self,obj_url):
        # 定义爬取目标的url
        self.url = obj_url
        # 定义用户代理
        self.headers = {
            'User-Agent':UserAgent().random
        }

    # 将不同的功能封装成函数
    # 创建获取url的函数
    def get_url(self):
        # 使用format方法确定每一次要爬取的url
        url = self.url.format()
        # 确定好url之后，直接调用self.get_html()方法,并将url作为参数传入self.get_html()方法
        html = self.get_html(url)
        return html
        
    # 创建获取目标地址源代码的函数,参数url为目标地址
    def get_html(self,url):
        # 调用requests模块中的get()方法获取网页源代码
        html = requests.get(url=url,headers=self.headers).text
        return html
    
    # 创建解析源代码的函数，参数html为网页源代码
    # def parse_html(self,html):
    #     # 使用etree.HTML()方法获取到节点对象
    #     node_obj = etree.HTML(html)
    #     # 对node_obj进行xpath解析(如果需要两个及以上内容的时候可以先对一个大的节点对象进行解析)
    #     node_list = node_obj.xpath("//a[@class='j_th_tit']/text()")
    #     # print(node_list)
    #     # print(node_obj)
    #     # 然后再分别对每一个进行解析
    #     for node in node_list:
    #         title = node.xpath(".//a[@class='j_th_tit ']//text()")
    #         print(title)
    #         # 然后将得到列表进行处理打印出来即可
    
    # 创建主函数
    def main(self):
        html = self.get_url()
        return html

if __name__ == "__main__":
    ...

