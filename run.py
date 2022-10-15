from pickle import TRUE


def run():
    import os
    from datetime import datetime
    inputfolder=input('请输入输入文件夹，默认输出到output+当前日期T时间文件夹,默认为input')
    if (inputfolder==''):
        inputfolder='input'
    path_input='./'+inputfolder
    file_name_list=os.listdir(path_input)
    n=len(file_name_list)
    tmp_time=(str(datetime.now())[:-7])
    tmp_time=tmp_time.replace('-','.')
    tmp_time=tmp_time.replace(':','.')
    tmp_time=tmp_time.replace(' ','T')
    flag_upper=True
    for i in range(n):
        os.stat(path_input+'/'+file_name_list[i])
        #阻止处理大文件
        size=os.stat(path_input+'/'+file_name_list[i]).st_size>>20
        if size>1 and flag_upper: 
            flag=input('该文件较大，是否继续（N/Y）')
            if flag=='N' or flag=='n':
                flag_upper=False
                continue
        filetype='.'+file_name_list[i].split(sep='.')[-1]
        os.rename(path_input+'/'+file_name_list[i],path_input+'/'+str(i)+filetype)
        #输出及输入文件，输出文件均相异
        command_gpu='realesrgan-ncnn-vulkan.exe -i '+path_input+'/'+str(i)+filetype+' -o ./output'+tmp_time+'/'+str(i)+'new'+filetype+' -n realesrgan-x4plus-anime'
        os.system(command_gpu)
    print('mission complete')

run()

