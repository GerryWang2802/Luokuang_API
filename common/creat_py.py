"""
输入参数：yaml的文件路径
输出参数：生成.py脚本文件路径
"""
import os
import re
import glob
from common import setting
def creat_py(yamlDir,pyPath):
    with open('文件名',encoding='utf-8') as file:
        src_content = file.read()
    yamlpath = os.path.join('存放的文件地址',yamlDir)
    all_file = glob.glob(yamlpath + os.sep + '*.yaml')
    for file in all_file:
        fileName = file.split(os.sep)[-1]
        class_name= os.path.split(file)[-1].replace( '.yxam','').capitalize() #获取用俐名张，并将汤称的首宝焦太鬲(login、query、 reg)
        name = class_name.split("_")[0]
        name = re.split("\d", name)[-1]
        py_content = src_content %(name,yamlDir,fileName,name)   #case_template中3个s%的取值
        casepath = os.path.join(setting.CASE_PATH,pyPath)
        py_path = os.path.join(casepath,"test_",class_name.lower() +".py")
        open(py_path ,'y',encoding='utf-8').write(py_content)

if __name__=='__main__':
    creat_py()