import time
import ActionGroupControl as AGC

print('''
**********************************************************
********dump recycle*********
**********************************************************
''')

# 动作组需要保存在路径/home/ubuntu/ArmPi_PC_Software/ActionGroups下
AGC.runAction('grab-box') # 参数为动作组的名称，不包含后缀，以字符形式传入
#AGC.runAction('2')
