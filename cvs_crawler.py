import time

import requests
from pyquery import PyQuery as pq

def get_web_page(url): #原始地址
    time.sleep(0.5)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取
    response = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    #if resp.status_code != 200:
    #    print('Invalid url:', resp.url)
    #    return None
    #else:
    return pq(response.text)

if __name__ == '__main__':
    PTT_URL = 'https://www.ptt.cc/'
    CSV_URL = 'https://www.ptt.cc/bbs/CVS/index.html'
    current_page_pq = get_web_page(CSV_URL)
    for crawled_page_count in range(10):
        previous_page_url = current_page_pq('.btn-group-paging .wide')[1].items()[1][1]
        print(previous_page_url)
        for article in current_page_pq('.r-ent .title a').items():
            print(f"{PTT_URL}{article.attr('href')}")
            article_pq =  get_web_page(f"{PTT_URL}{article.attr('href')}")
            article_info_generator = article_pq('.article-metaline  .article-meta-value').items()
            article_info = [article_info.text() for article_info in article_info_generator]
            print(article_info)
            # for push in article_pq('.push').items():
            #     print(push('.push-content').text()[2:])

        current_page_pq = get_web_page(f"{PTT_URL}{previous_page_url}")