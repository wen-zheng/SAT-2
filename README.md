# SAT-2

# staticfg 是由python3源文件生成CFG的项目，项目说明: https://github.com/wen-zheng/SAT-2/tree/master/staticfg
# 关于angr示例的执行:
    需要用到的包:
    angr,angr-utils

    执行步骤：
    gcc example.c -o test
    python plotcfg.py
    gcc test.c -o test
    python solver.py
    python plotcfg.py
