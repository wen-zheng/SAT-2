#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import angr


def basic_symbolic_execution():
    p = angr.Project('test')  
    # 新建一个angr的工程，括号中是目标二进制程序的路径
    state = p.factory.entry_state()  
    # 接着新建一个SimState的对象
    path = p.factory.path(state)  
    # 使用factory.path这个容器获取state的起点path对象
    # 根据前面获取的函数入口点的path对象，利用path_group容器获取沿着path开端下面将会执行的path列表
    pathgroup = p.factory.path_group(path)
    # 接下来就让pathgroup对象一直执行下去，直到执行到可选择的路径个数大于一个，即产生选择分支的时候，再停止。
    pathgroup.step(until=lambda lpg: len(lpg.active) > 1)
    # 对应在上述的简单程序中authenticate函数的 if (strcmp(password, sneaky) == 0)这个条件判断语句


    input_0 = pathgroup.active[0].state.posix.dumps(0)  
    # dump出所有分支的内容，看看哪个答案应该是最可能的
    input_1 = pathgroup.active[1].state.posix.dumps(0)

    if 'SOSNEAKY' in input_0:
        return input_0
    else:
        return input_1


def test():
    pass
if __name__ == '__main__':
    print basic_symbolic_execution()
