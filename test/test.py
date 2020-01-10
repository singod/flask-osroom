#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time : 2019/11/18 15:07
# @Author : Allen Woo

import os
import sys

sys.exit()
auther_info = """# @Time : 2017/11/1 ~ 2019/9/1\n# @Author : Allen Woo\n"""
n = 0
for root, dirs, files in os.walk("/home/work/project/osroom"):
    # if n == 3:
    #     break
    for name in files:
        # if n == 3:
        #     break
        if name.endswith(".py") and name != "__init__.py":
            path = os.path.join(root, name)
            print(path)
            n += 1
            is_w = False
            with open(path, 'r') as f:
                lines = f.readlines()

                for i, line in enumerate(lines):
                    if line.strip() in ["# -*-coding:utf-8-*-"]:
                        if lines[i+1].startswith("# @Time :"):
                            break

                        lines.insert(i+1, auther_info)
                        if i == 0:
                            lines.insert(0, "#!/usr/bin/env python\n")
                        is_w = True
                        break
                    if i >= 3:
                        lines.insert(0, "#!/usr/bin/env python\n# -*-coding:utf-8-*-\n{}".format(auther_info))
                        is_w = True
                        break

                for i, line in enumerate(lines):
                    if line.strip() == '__author__ = "Allen Woo"':
                        if lines[i-1].strip() == "":
                            del lines[i-1]
                            del lines[i-1]
                        else:
                            del lines[i]
                        is_w = True
                        break

            if is_w:
                with open(path, 'w') as f:
                    f.writelines(lines)
