from datetime import date
from icrawler.builtin import FlickrImageCrawler

# Cai dau là public key cua tai khoan minh, cai sau tao 1 thu muc theo ten ngay tai folder code, vi du o day la 1
flickr_crawler = FlickrImageCrawler('38128d586f56e5a049ce03420dba0af5',
                                    storage={'root_dir': '1'})

# max_num la so luong anh minh crawl, text la text minh dung de search
flickr_crawler.crawl(max_num=50, text='stop signs',
                     sort='relevance', safe_search=3)
