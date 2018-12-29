import angr
from angrutils import *
binary = "./test"
b=angr.Project(binary, load_options={'auto_load_libs':False})
cfg=b.analyses.CFG()
plot_cfg(cfg, "cfgfast", asminst=True, remove_imports=True, remove_path_terminator=True)

# main = b.loader.main_bin.get_symbol('main')
# s=b.factory.blank_state(addr=main.addr)
# cfg = b.analyses.CFGAccurate(fail_fast=True, starts=[main.addr], initial_state=s)
# plot_cfg(cfg, "cfgaccurate", asminst=True, remove_imports=True, remove_path_terminator=True)  