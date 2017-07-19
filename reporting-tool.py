#!/usr/bin/env python2.7

import psycopg2

f = open('output.txt', 'w')

DBNAME = 'news'
db = psycopg2.connect(database=DBNAME)

print "printing results into output.txt file ..."
cursor = db.cursor()
createViewQuery = "create view TopArticles as select substring" + \
                  "(path from 10) as slug,count(*) as num from log group " + \
                  "by path order by num desc limit 8 offset 1;"
cursor.execute(createViewQuery)
selectQuery = "select title,num from articles,TopArticles where " + \
              "articles.slug=TopArticles.slug order by num desc limit 3;"
cursor.execute(selectQuery)
results = cursor.fetchall()

f.write("Question 1. What are the most popular three articles of all time?\n")
f.write("Answer -\n")
for result in results:
    f.write("\"" + result[0] + "\" - " + str(result[1]) + " views\n")

selectQuery2 = "select name,sum from (select sum(num),author from " + \
               "articles,TopArticles where articles.slug=TopArticles.slug " + \
               "group by author order by sum desc)s,authors " + \
               "where authors.id=s.author;"
cursor.execute(selectQuery2)
results = cursor.fetchall()
f.write("\n")
f.write("Question 2. Who are the most popular article authors of all time?\n")
f.write("Answer -\n")
for result in results:
    f.write(result[0] + " - " + str(result[1]) + " views\n")

createViewQuery2 = "create view newlog as select trim(regexp_replace" + \
                  "(to_char(time,'Month dd,YYYY')," + \
                   "'\s+', ' ', 'g')) as time,status from log;"
cursor.execute(createViewQuery2)
selectQuery3 = "select time,round(percentage::numeric,1) from " + \
          "(select (scount::float/count(*)::float)*100 as " + \
          "percentage,newlog.time from newlog,(select time,count(*) " + \
          "as scount from newlog where " + \
          "status='404 NOT FOUND' group by time) as mlog " + \
          "where mlog.time=newlog.time group by " + \
          "newlog.time,scount) as t where percentage>1;"
cursor.execute(selectQuery3)
results = cursor.fetchall()
f.write("\n")
f.write("Question 3. On which days did more than 1% of" +
        "requests lead to errors?\n")
f.write("Answer -\n")
for result in results:
    f.write(result[0] + " - " + str(result[1]) + "%" + " errors\n")
f.close()
