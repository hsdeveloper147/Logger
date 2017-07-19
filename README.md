# Logger
FSND project
## Requirements
### 1. Python 2.7 
Install Python 2.7 from [this](https://www.python.org/download/releases/2.7/) link.
### 2. PostgreSQL
Install it via pip command  
``` pip install psycopg2```   
or follow [this](http://initd.org/psycopg/docs/install.html) link if having trouble.  
Further you need to configre the localhost to run the server.  
### OR 
follow [this](https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) link for easy setup  
This easy setup installs a VM ware and provides python and postgreSQl and required customisation by itself.  

## Running the Code
1.Run the terminal and type ``` psql -d news -f newsdata.sql ``` to import the data.  
2.Type ``` psql -d news``` to get to the news database.  
3.**Important** - Since in addition to imported tables I have created two Views you have to run following 
3a.```create view TopArticles as select substring(path from 10) as slug,count(*) as num from log group by path order by num desc limit 8 offset 1;```   
3b```create view newlog as select trim(regexp_replace(to_char(time,'Month dd,YYYY'),'\s+', ' ', 'g')) as time,status from log;```
4.The repo consists of a file reporting-tool.py. Run it in the terminal by ``` python reporting-tool.py```.  
The output file output.txt will be created a
and the log results will be written to this file.
