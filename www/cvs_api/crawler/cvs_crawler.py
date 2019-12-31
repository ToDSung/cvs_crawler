import json
import time

import requests
from pyquery import PyQuery as pq

from my_date_tool import covert_string_to_datetime, covert_datetime_to_string

def get_web_page(url): #原始地址
    time.sleep(0.1)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取
    response = requests.get(
        url=url,
        cookies={'over18': '1'},
        verify=False
    )
    #if resp.status_code != 200:
    #    print('Invalid url:', resp.url)
    #    return None
    #else:
    return pq(response.text)

def judge_cvs_topic(article_info):
    topic = ''
    if  article_info[1][1:3] in ['資訊', '情報', '新聞']:
        topic = 1
    elif article_info[1][1:3] in ['商品']:
        topic = 2
    elif article_info[1][1:3] in ['問題', '贈送', '討論', '心得']:
        topic = 3
    return topic

if __name__ == '__main__':
    PTT_URL = 'https://www.ptt.cc/'
    CSV_URL = 'https://www.ptt.cc/bbs/CVS/index.html'
    current_page_pq = get_web_page(CSV_URL)
    
    output_list = []
    
    for crawled_page_count in range(1):
        previous_page_url = current_page_pq('.btn-group-paging .wide')[1].items()[1][1]
        for article in current_page_pq('.r-ent .title a').items():
            article_pq =  get_web_page(f"{PTT_URL}{article.attr('href')}")
            article_info_generator = article_pq('.article-metaline  .article-meta-value').items()
            article_info = [article_info.text() for article_info in article_info_generator]
            
            if len(article_info) == 0:
                continue
            
            topic = judge_cvs_topic(article_info)
            
            push_count = 0
            bull_count = 0
            arrow_count = 0
            push_comment_list = []
            bull_comment_list = []
            arrow_comment_list = []
            for push_content in article_pq('.push').items():
                comment = push_content('.push-content').text()[2:]
                push_label = push_content('.push-tag').text()
                if push_label == '推':
                    push_count += 1
                    push_comment_list.append(comment)
                elif push_label == '噓':
                    bull_count += 1
                    bull_comment_list.append(comment)
                elif push_label == '→':
                    arrow_count += 1
                    arrow_comment_list.append(comment)
                    
            print(f"{PTT_URL}{article.attr('href')}")
            output_list.append({                
                "文章標題": article_info[1],
                "議題": topic,
                "文章時間": covert_datetime_to_string(covert_string_to_datetime(article_info[2], '%a %b %d %H:%M:%S %Y'), '%m月%d日'),
                "文章網址": f"{PTT_URL}{article.attr('href')}",
                "留言數": push_count + bull_count + arrow_count,
                "推文數": push_count,
                "推文留言": push_comment_list,
                "噓文數": bull_count,
                "噓文留言": bull_comment_list,
                "箭頭數": arrow_count,
                "箭頭留言": arrow_comment_list,
            })
        current_page_pq = get_web_page(f"{PTT_URL}{previous_page_url}")
        
    with open ('./cvs.json', 'w', encoding='utf-8') as f:
        output_list = sorted(output_list, key=lambda x: x['文章時間'], reverse=True)
        json.dump(output_list, f, ensure_ascii=False, indent=4)