import function1

while True:
    # 1. 显示功能界面
    function1.print_info()
    # 2. 用户选择功能
    user_num = input('请选择您需要的功能序号：')
    # 3. 根据用户选择，执行不同的功能
    if user_num == '1':
        print('添加学员')
        function1.add_info()
    elif user_num == '2':
        print('删除学员')
        function1.del_info()
    elif user_num == '3':
        print('修改学员信息')
        function1.modify_info()
    elif user_num == '4':
        print('查询学员信息')
        function1.search_info()
    elif user_num == '5':
        print('显示所有学员信息')
        function1.print_all()
    elif user_num == '6':
        print('退出系统')
        exit_flag = input('确定要退出吗？yes or no\n')
        if exit_flag == 'yes':
            break
    else:
        print('输入错误，请重新输入!!!\n')
