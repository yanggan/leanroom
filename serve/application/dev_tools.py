# coding:utf-8
from config.config import *

import commands,re




# 测试用的功能
# 开发环境下显示git版本号 
def show_git_data(flag=config["default"].GIT_VERSION_DISPLAY):
    # git log --pretty=oneline -1  
    # return 451ecd160187ab7ea0c8bcef85a906967dd95d6a added: model add colmmn structure
    if flag == True:
        print "show_git_data  func is enable"
        (status, output) = commands.getstatusoutput('git log --pretty=fuller -1')
        # print status, output

        recomm = r'commit.(\w{20,})\nAuthor:\s*.*\n.*\n.*\nCommitDate:(.*)\n*(.*)'
        git_data = re.findall(recomm,output)
        git_data = git_data[0] #转换为元祖
        # print git_data
        # print type(git_data)

    return {'version':git_data[0],'commit':git_data[2],'time':git_data[1]}

# 开启或者关闭调试信息功能
# show_git_data()
if config["default"].GIT_VERSION_DISPLAY:
    
    git_data = show_git_data()
    dev_data = {
        'flag':config["default"].GIT_VERSION_DISPLAY,
        'git':{ 
            'version':git_data['version'],
            'commit':git_data['commit'],
            'time':git_data['time'],
        }
    }
else:

    dev_data = {
        'flag':config["default"].GIT_VERSION_DISPLAY,
    }


