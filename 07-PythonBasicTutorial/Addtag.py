#coding=utf-8
import re
"""
    给一个文本添加标签.
"""



def lines(file):
    for line in file:
        yield line
        yield "\n"

def blocks(lines):
    blocks = []
    for line in lines:
        if line.strip():
            blocks.append(line)
        elif blocks:
            yield " ".join(blocks).strip()
            blocks = []
    return blocks

if __name__ == "__main__":

    title = True
    with open("./source/test_input.txt","r") as f:
        # blocks = blocks(f);
        for block in blocks(f):
            block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
            print(block,end="")
            if title:
                print('<h1>')
                print(block)
                print('</h1>')
                title = False
            else:
                print('<p>')
                print(block)
                print('</p>')










