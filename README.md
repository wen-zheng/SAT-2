# SAT-2

# 课程报告：[课程报告](https://github.com/wen-zheng/SAT-2/blob/master/CFG%E4%B8%8E%E7%AC%A6%E5%8F%B7%E6%89%A7%E8%A1%8C.pdf)
# staticfg 是由python3源文件生成CFG的项目，项目说明: [staticfg](https://github.com/wen-zheng/SAT-2/tree/master/staticfg)
# 关于angr示例的执行:
### 需要用到的包:
    angr,angr-utils

### 执行步骤：
    ```
    gcc example.c -o test
    python plotcfg.py
    gcc test.c -o test
    python solver.py
    python plotcfg.py
    
    ```
