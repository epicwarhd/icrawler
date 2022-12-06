from icrawler.builtin import GreedyImageCrawler

greedy_crawler = GreedyImageCrawler(storage={'root_dir': '1'})
greedy_crawler.crawl(domains='https://www.google.com/search?q=narrow+bridge+sign&tbm=isch&ved=2ahUKEwj6mo3ay-T7AhUH_JQKHeLVBygQ2-cCegQIABAA&oq=narrow+bridge+sign&gs_lcp=CgNpbWcQDFAAWABgAGgAcAB4AIABAIgBAJIBAJgBAKoBC2d3cy13aXotaW1n&sclient=img&ei=k_-OY7qFCof40wTiq5_AAg&bih=722&biw=1536', 
                     max_num=50,
                     min_size=None, max_size=None)
