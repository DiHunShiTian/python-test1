def print_info(): #学籍管理系统
    print('-' * 20)
    print('欢迎登录学员管理系统')
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')
    print('-' * 20)

def add_info():  #接收用户输入学员信息
    """ 添加学员 """
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')
    # 声明info是全局变量
    global info
    # 检测用户输入的姓名是否存在，存在则报错提示
    for i in info:
        if new_name == i['name']:
            print('该用户已经存在！')
            return
    # 如果用户输入的姓名不存在，则添加该学员信息
    info_dict = {}  # 将用户输入的数据追加到字典
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    # 将这个学员的字典数据追加到列表
    info.append(info_dict)

def del_info():# 删除学员
    # 1. 用户输入要删除的学员的姓名
    del_name = input('请输入要删除的学员的姓名：')
    global info
    # 2. 判断学员是否存在:如果输入的姓名存在则删除，否则报错提示
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在')
        return
    print('删除成功')

def modify_info(): # 修改函数
    # 1. 用户输入要修改的学员的姓名
    modify_name = input('请输入要修改的学员的姓名：')
    global info
    # 2. 判断学员是否存在：如果输入的姓名存在则修改手机号，否则报错提示
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入新的手机号：')
            break
    else:
        print('该学员不存在')

def search_info():# 查询学员
    # 1. 输入要查找的学员姓名：
    search_name = input('请输入要查找的学员姓名：')

    global info
    # 2. 判断学员是否存在：如果输入的姓名存在则显示这位学员信息，否则报错提示
    for i in info:
        if search_name == i['name']:
            print('查找到的学员信息如下：\n----------')
            print(f"该学员的学号是{i['id']}, 姓名是{i['name']}, 手机号是{i['tel']}")
            break
    else:
        print('该学员不存在')

def print_all(): # 显示所有学员信息
    print('学号\t姓名\t手机号')
    for i in info:
        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')

info = []