import zipfile
import os
import numpy as np
import random


# get the number of occurrences of val in myList
def counter(myList, val):
    num = 0
    for item in myList:
        if val == item:
            num += 1
    return num


def selectOtherOne(exception, population):
    randomItem = random.sample(population, 1)[0]
    while randomItem == exception:
        randomItem = random.sample(population, 1)[0]
    return randomItem


# generate a list [start, start+step, ..., end]
def floatRange(start, step, end):
    temp = np.arange(start, end+step, step).tolist()
    result = [round(item, 3) for item in temp]
    return result


# zipcompress all files under a directory excluding directory
def zipCompress(dirName, zipFileName):
    delFile(zipFileName)
    with zipfile.ZipFile(zipFileName, 'w', zipfile.ZIP_DEFLATED) as f:
        for dirpath, dirNames, fileNames in os.walk(dirName):
            for fileName in fileNames:
                f.write(os.path.join(dirpath, fileName), fileName)


# delete a file
def delFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)


# delete all files (excluding directories) under a directory
def delDir(dirName):
    files = os.listdir(dirName)
    for file in files:
        path = os.path.join(dirName, file)
        os.remove(path)
    delFile(dirName)


# test floatRange()
def testFloatRange():
    print(floatRange(3, 0.2, 6))


# test zipCompress()
def testZipCompress():
    zipCompress('./data', './data.zip')

