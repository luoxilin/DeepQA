#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models import word2vec

# 主程序
sentences = word2vec.Text8Corpus("content.txt")  # 加载语料
model = word2vec.Word2Vec(sentences, size=200)  # 训练skip-gram模型; 默认window=5

# 计算两个词的相似度/相关程度
y1 = model.similarity(u"不错", u"好")
print u"【不错】和【好】的相似度为：", y1
print "--------\n"

# 计算某个词的相关词列表
y2 = model.most_similar(u"日本", topn=20)  # 20个最相关的
print u"和【日本】最相关的词有：\n"
for item in y2:
    print item[0], item[1]
print "--------\n"

# 寻找对应关系
print u"日本-樱花，美食-"
y3 = model.most_similar([u'樱花', u'美食'], [u'日本'], topn=3)
for item in y3:
    print item[0], item[1]
print "--------\n"

# 寻找不合群的词
y4 = model.doesnt_match(u"歌 日本 烟火 寿司".split())
print u"不合群的词：", y4
print "--------\n"

# 保存模型，以便重用
model.save(u"10222.model")
# 对应的加载方式
# model_2 = text.Word2Vec.load("text8.model")

# 以一种C语言可以解析的形式存储词向量
model.save_word2vec_format(u"10222.model.bin", binary=True)
# 对应的加载方式
# model_3 = text.Word2Vec.load_word2vec_format("text8.model.bin", binary=True)

if __name__ == "__main__":
    pass