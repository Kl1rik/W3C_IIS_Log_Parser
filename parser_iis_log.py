import sqlite3
import re
db_path = "iis_parser.db"
path = "u_ex230404.log"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
zero = 0
f = open(path,"r")
raw_logs = f.readlines()
# cursor.execute('''CREATE TABLE IIS ("date" text, "time" text,"s-ip" text,"cs-method" text,"cs-uri-stem" text,"cs-uri-query" text,"s-port" text,"cs-username" text,"c-ip" text, "cs-version" text,"cs(User-Agent)" text, "cs(Referer)" text, "cs-host" text, "sc-status" text, "sc-substatus" text, "sc-win32-status" text, "sc-bytes" text,"cs-bytes" text, "time-taken" text)''')
#if re.match("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ?\d+\.?\d+\.?\d+\.?\d+ \w{3} \/.+ \- \d{3} \- ?\d+\.?\d+\.?\d+\.?\d+ \w{4}\/.+ .+ .+ .+ \d+ \d+ \d+ \d+ \d+ \d+",log):
with open(path,'r') as fh:
     for curline in fh:
         # check if the current line
         # starts with "#"
         if curline.startswith("#"):
            print(".")
         else:
            curline = curline.split()
            print(curline)
            cursor.execute('INSERT INTO  IIS (date,time,sip	,csmethod	,csuristem	,csuriquery	,sport	,csusername	,cip	,csversion	,csUserAgent	,csReferer	,cshost	,scstatus	,scsubstatus	,scwin32status	,scbytes	,csbytes	,timetaken	) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(curline[0],curline[1],curline[2],curline[3],curline[4],curline[5],curline[6],curline[7],curline[8],curline[9],curline[10],curline[11],curline[12],curline[13],curline[14],curline[15],curline[16],curline[17],curline[18],))
            connection.commit()
rows = cursor.fetchall()

for row in rows :
    print(row)





























