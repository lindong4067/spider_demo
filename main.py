from scrapy import cmdline

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# cmdline.execute("scrapy crawl tonghuashun".split())
cmdline.execute("scrapy crawl stock".split())
