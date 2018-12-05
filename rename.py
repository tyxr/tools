
import os

def nist2wav(src_dir):
    count = 0
    for subdir, dirs, files in os.walk(src_dir):
        for f in files:
            fullFilename = os.path.join(subdir, f)
            if f.endswith('.php'):
                count += 1
                os.rename(fullFilename,fullFilename[:-4]+".txt")
                #print(fullFilename)

if __name__ == '__main__':
    nist2wav('D:\碳云源代码_78450\碳云源代码\PHP_碳云')
