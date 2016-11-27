'''
v 1.0.0
Upload basic file to google drive
CTRT Electronics Subdivision
'''


from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth() #google drive authentication for an account
drive = GoogleDrive(gauth) #create drive instance for authorised instance(in this case, gauth)

file1 = drive.CreateFile({'title' : 'Hello.txt'}) #create file with name hello.txt
file1.SetContentFile('log.txt') #set contents of file1 to be contents of the file 'log.txt'
file1.Upload() # upload the file file1
