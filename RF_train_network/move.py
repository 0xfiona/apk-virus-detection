import os, random, shutil


def moveFile(fileDir, tarDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    rate = 0.0172  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    print(sample)
    print(len(sample))
    for name in sample:
        shutil.move(fileDir + name, tarDir + name)


if __name__ == '__main__':
    fileDir = "E:\\virus\\normal\\"  # 源图片文件夹路径
    # tarDir = "E:\\virus\\virussample\\"  # 移动到新的文件夹路径
    tarDir = "E:\\virus\\pythonProject1\\pythonProject1\\AndroidMalware-ngram-RF\\bit\\testAndroid\\white\\"
    moveFile(fileDir, tarDir)
