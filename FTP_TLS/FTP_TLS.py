from ftplib import FTP_TLS
import os


ftps = FTP_TLS(timeout=100) 
ftps.set_debuglevel(1)          
ftps.connect("192.168.1.35", 21)
ftps.auth()
ftps.prot_p()
ftps.login('pan', '1')
print(ftps.getwelcome())
print(ftps.pwd())
ftps.dir()
# 下载文件
os.chdir(r'D:\Desktop\FTP_TLS\FTP\00临时存储')
ftps.cwd('/')
ftps.nlst()  # 获取目录下的文件
filename = 'vsftpd.key'
file_handle = open(filename, "wb").write
ftps.retrbinary('RETR %s' % os.path.basename(filename), file_handle,blocksize=1024)  # 下载ftp文件

# 上传到服务器
bufsize = 1024
localpath = 'D:\\Desktop\\FTP_TLS\FTP\\00临时存储\\test.txt'
remotepath = '/test.txt'
fp = open(localpath, 'rb')
ftps.storbinary('STOR ' + remotepath, fp, bufsize)
# 打印证书
print(ftps.context)
print(ftps.certfile)
print(ftps.ssl_version)
# ftps.retrlines('LIST')
ftps.set_debuglevel(0)  
ftps.quit()