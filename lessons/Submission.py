from pyspim.pyspim import Spim


def run_MIPS(filename):
    sp = Spim(debug=False)
    sp.load(filename)
    sp.run()
    return {i: sp.reg(i) for i in range(32)}
