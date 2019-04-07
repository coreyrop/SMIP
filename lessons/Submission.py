from pyspim.pyspim import Spim

sp = Spim(debug = False)


def run_MIPS(filename):
    sp.load(filename)
    sp.run()
    return {i: sp.reg(i) for i in range(32)}
