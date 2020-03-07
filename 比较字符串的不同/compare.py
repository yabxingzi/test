#!/usr/bin/env python

import difflib

text1 = "https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html"

text1_lines = text1.splitlines()                # 以行进行分割，以便进行对比
text2 = "https://y.qq.com/n/yqq/song/001xd0HI0X9GNq.html"

text2_lines = text2.splitlines()
d = difflib.Differ()            # 创建Differ()对象
diff = d.compare(text1_lines, text2_lines)           # 采用compare方法对字符串进行比较
print('\n'.join(list(diff)))