import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)))
import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python extract_tags.py [file name] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

# file_name = args[0]
file_name = '/home/tutumeimei1023/DeepQA2/data/text/content.txt'

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

content = open(file_name, 'rb').read()

tags = jieba_test.analyse.extract_tags(content, topK=topK)

f1 = open('/home/tutumeimei1023/DeepQA2/data/text/content_new.txt', 'w')
for tag in tags:
    f1.write(tag)


print(",".join(tags))