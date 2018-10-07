import Util
import GenerateInstance
import os


ratioToP1P2 = {0.35: (0.9625, 0.0250),
               0.40: (0.8500, 0.1000),
               0.45: (0.7375, 0.1750),
               0.50: (0.6250, 0.2500),
               0.65: (0.2875, 0.4750),
               0.80: (0.1500, 0.3000),
               0.95: (0.0375, 0.0750)}
# number of instances for a group of parameter settings
numInstancePerParameter = 50


# generate instances under a group of parameter settings
def generateInstances(n=500, r=4.5, p=0.3, alpha=1, c=20, ratio=0.50):
    instanceName = 'n=' + '%04d' % n + '_' + \
                   'r=' + '%.2f' % r + '_' + \
                   'p=' + '%.2f' % p + '_' + \
                   'alpha=' + '%.2f' % alpha + '_' + \
                   'c=' + '%02d' % c + '_' + \
                   'ratio=' + '%.2f' % ratio + '_' + \
                   'numInstancePerParameter=' + '%02d' % numInstancePerParameter
    p1, p2 = ratioToP1P2[ratio]

    for rank in range(numInstancePerParameter):
        generateInstance = GenerateInstance.GenerateInstance(n=n, r=r, p=p, alpha=alpha, c=c, p1=p1, p2=p2)

        generateInstance.instanceToFile('data/' + instanceName + '_' +
                                        'rank=' + '%02d' % rank + '.cnf')

# generate instances used in our experiments
def generateAllInstances():
    if os.path.exists('./data'):
        Util.delDir('./data')
    os.mkdir('./data')
    ratioList = list(ratioToP1P2.keys())
    pList = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    alphaList = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    for ratio in ratioList:
        for p in pList:
            for alpha in alphaList:
                print(ratio, p, alpha)
                generateInstances(p=p, alpha=alpha, ratio=ratio, n=700)
    Util.zipCompress('./data', './allInstances.zip')


if __name__ == '__main__':
    generateAllInstances()
