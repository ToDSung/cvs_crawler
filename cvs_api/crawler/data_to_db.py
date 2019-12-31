import json
import os
import sys
import django

sys.path.append('/var/www/cvs_api')
# sys.path.append('/c/Users/wluna/Desktop/my_git_hub/cvs_crawler/www/cvs_api/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cvs_api.settings')
django.setup()

from django.db import IntegrityError
from web.models import Cvs

def main():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    with open (f'{dirname}/cvs.json', 'r', encoding='utf-8') as f:
        data_list  = json.loads(f.read())
        
        
        news_result_list = []
        for each_data in data_list:
            news_result_list.append(
                Cvs(
                    title = each_data['文章標題'],
                    topic = each_data['議題'],
                    article_time = each_data['文章時間'],
                    article_link = each_data['文章網址'],
                    message = each_data['留言數'],
                    push_count = each_data['推文數'],
                    push_message = each_data['推文留言'],
                    bull_count =each_data['噓文數'],
                    bull_message = each_data['噓文留言'],
                    arrow_count = each_data['箭頭數'],
                    arrow_message = each_data['箭頭留言']
                )
            )
    Cvs.objects.bulk_create(news_result_list, ignore_conflicts = True)
if __name__ == '__main__':
    main()