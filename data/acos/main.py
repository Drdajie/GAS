"""
将四元组数据分为 aspect 显示和隐式两种
思路：读文件中每一个 instance，依次存 sentence 和 各个标注，判断每个标注并归入显示文件和隐式文件
步骤：
    1_读每个 instance 并存 sentence 和 各个标注
    2_判断每个标注是否是 aspect 隐式 -> 形成新的显示、隐式 instance
"""

import os

def process_one_domain(dir):
    in_pathes = os.listdir(dir)
    for in_path in in_pathes:
        with open(dir + in_path, 'r', encoding='utf-8') as in_f,\
            open('./acos_hide_classification/apparent/'+dir+in_path, 'w', encoding='utf-8') as out_apr_f,\
            open('./acos_hide_classification/hide/'+dir+in_path, 'w', encoding='utf-8') as out_hide_f:
            # 1_读每个 instance 并存 sentence 和 各个标注
            for line in in_f:
                line = line.strip()
                sent, labels = line.split('####')
                # 2_判断每个标注是否是 aspect 隐式 -> 并处理
                tuples = eval(labels)
                list_apr, list_hide = [], []
                for tuple in tuples:
                    if tuple[0][0] == -1 and tuple[0][1] == -1:
                        list_hide.append(tuple)
                    else:
                        list_apr.append(tuple)
                if list_apr != []:
                    apr_line = sent + "####" + str(list_apr)
                    out_apr_f.write(apr_line + '\n')
                if list_hide != []:
                    hide_line = sent + "####" + str(list_hide)
                    out_hide_f.write(hide_line + '\n')

if __name__ == '__main__':
    in_dir = ['restaurant/', 'laptop/']
    for dir in in_dir:
        process_one_domain(dir)