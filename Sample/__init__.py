from pyspim.pyspim import Spim

spim = Spim(debug=False)
spim.load('sample.s')
spim.run()
for i in range(32):
    print('reg('+str(i)+'): ', spim.reg(i))
spim.quit()