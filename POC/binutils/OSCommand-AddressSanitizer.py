import os
import time

command = '../build/bin/c++filt -t'
path0 = '/media/whj/01D3344861A8D2E01/wcventure/Project/binutils-2.31/Fuzzing/c++filt_out/m1/crashes/'
path1 = '/media/whj/01D3344861A8D2E01/wcventure/Project/binutils-2.31/Fuzzing/c++filt_out/s1/crashes/'
path2 = '/media/whj/01D3344861A8D2E01/wcventure/Project/binutils-2.31/Fuzzing/c++filt_out/s2/crashes/'
path3 = '/media/whj/01D3344861A8D2E01/wcventure/Project/binutils-2.31/Fuzzing/c++filt_out/s3/crashes/'

def file_name(path, filelist): 
    for i in os.walk(path):
        for each in i[2]:
            if "README" not in each:
                filelist.append(path + each)



# main
filelist=[]
file_name(path0, filelist)
file_name(path1, filelist)
file_name(path2, filelist)
file_name(path3, filelist)
filelist.sort()


os.popen("echo '\n@@@@@@@@@@@@@@@@@@@@@@@@@@     Start    @@@@@@@@@@@@@@@@@@@@@@@@@@\n'" + " > log.txt", 'r')

i=1

for eachfile in filelist:

    os.popen("echo '----------------- go on -------------------'" + " >> log.txt", 'r')
    os.popen("echo 'Commond Line: " + command + eachfile + "\n'" + " >> log.txt", 'r')
    os.system(command + ' < ' + eachfile + ' 2>> log.txt')
    print("Finished: " + eachfile)
    i = i + 1


os.popen("echo '\n@@@@@@@@@@@@@@@@@@@@@@@@@@ Finished All @@@@@@@@@@@@@@@@@@@@@@@@@@\n'" + " >> log.txt", 'r')
time.sleep(0.01)


print("\nFinished: ALL")
