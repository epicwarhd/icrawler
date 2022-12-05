from icrawler.builtin import GoogleImageCrawler

# storage la ten foler, vi du o day la 2
google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=1,
    downloader_threads=4,
    storage={'root_dir': '2'})

filters = dict(
    type='photo',
    size='large',)

# max_num la so anh minh crawl
google_crawler.crawl(keyword='stop signs', filters=filters, offset=0, max_num=50,
                     min_size=(200, 200), max_size=None, file_idx_offset=0)
