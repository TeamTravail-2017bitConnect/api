#! /bin/sh

zip -r app.zip app
scp -i ~/Downloads/travail.pem app.zip ec2-user@52.192.108.213:~/travail/
ssh -i ~/Downloads/travail.pem ec2-user@52.192.108.213 "kill `cat PID`"
ssh -i ~/Downloads/travail.pem ec2-user@52.192.108.213 "unzip -o app.zip -d travail"
ssh -i ~/Downloads/travail.pem ec2-user@52.192.108.213 "gunicorn -p PID travail.main:app&"


