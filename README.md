
Based on:
    python 3.5
    django 1.10.5
    pgsql 9.4+
    bootstrap3
    jq (latest)
    Highcharts.js
    

Instruction for *nix and OS X:

1) clone project to your local machine:
git clone git@github.com:neonua/ceaser.git && cd ceasar/

In cloned catalog you will find two directories:
 - cesar_env
 - prj_cesar
 
 cesar_env is virtualenv environment to work with a project
 prj_cesar is project
 
 2) change settings:
 You need chanпe settings.py in projec for configured to work with a database.
 You can use any relational database, but in the example will use PostgresSQL.
 Open "prj_cesar/prj_cesar/settings.py" and find DATABASES. Change NAME db, USER db,
 and PASSWORD db. Also you can uncomment PORT and HOST and insert your data.
 The database needs to store the words that will be useful for guessing.
 
 3) activate environment:
 source cesar_env/bin/activate
 
 4) migrate:
 cd prj_cesar
 python3.5 manage.py migrate
 
 5) filling data into the database:
 python3.5 manage.py generator
 
 6) start project on 8000 port:
 python3.5 manage.py rinserver 8000
 
 if 8000 port is used - change your unused port
 
 7) open link in web-browser:
 http://127.0.0.1:8000
 
