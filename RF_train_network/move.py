import os, random, shutil

# 随机选取一些比例的数据集并移动到指定文件夹
def moveFile(fileDir, tarDir):
    pathDir = os.listdir(fileDir)
    filenumber = len(pathDir)
    rate = 0.0172
    picknumber = int(filenumber * rate)
    sample = random.sample(pathDir, picknumber)
    print(sample)
    print(len(sample))
    for name in sample:
        shutil.move(fileDir + name, tarDir + name)


if __name__ == '__main__':
    fileDir = "E:\\virus\\normal\\"  # 源文件夹路径
    # tarDir = "E:\\virus\\virussample\\"  # 移动到新的文件夹路径
    tarDir = "E:\\virus\\pythonProject1\\pythonProject1\\AndroidMalware-ngram-RF\\bit\\testAndroid\\white\\"
    moveFile(fileDir, tarDir)
