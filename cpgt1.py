import subprocess
import os
from os import listdir
from os.path import isfile, join
mypath = "E:\\lesson"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
loop = 0
name = "lesson"
url = []


for w in onlyfiles:
    if f"{name}{loop}" in w:
        loop += 1

    isExist = os.path.exists(f"{mypath}/{name}{loop}.png") 
    if(isExist):    
        loop += 1

def opfile():
    global url 
    file = open('imodnl.txt', 'r', encoding='utf-8')
    line = file.readline()
    url += [line]
    while line:
        line = file.readline()
        if line == "\n":
            continue
        url += [line]   
    file.close()

def opLnk():
    '''
    global loop
    for x in url:   
        copy_to_e_drive(x, loop)
        loop += 1
    ''' 
    copy_to_e_drive("https://example/master.m3u8", 3)   
        #print (x)


def copy_to_e_drive(input_file, num):
    output_file = f"E://lesson{num}.mp4"  # Change the output file name and path as needed

    # FFmpeg command with protocol whitelist and copy operation
    ffmpeg_cmd = [
        "ffmpeg",
        "-protocol_whitelist", "file,http,https,tcp,tls,crypto",
        "-i", input_file,
        "-c", "copy",
        output_file
    ]

    try:
        process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()  # Wait for the process to complete
        print(f"File successfully copied to {output_file}")
        print("Done")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    opfile()
    opLnk()