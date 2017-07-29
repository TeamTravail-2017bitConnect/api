#! /bin/sh
HOME=/home/ec2-user
GUNICORN=$HOME/.pyenv/shims/gunicorn
PID=$HOME/PID

zip -r app.zip app
scp -i travail.pem app.zip ec2-user@52.192.108.213:$HOME/travail/
ssh -i travail.pem ec2-user@52.192.108.213 "kill `cat PID`"
ssh -i travail.pem ec2-user@52.192.108.213 "unzip -o app.zip -d travail"
ssh -i travail.pem ec2-user@52.192.108.213 exec $GUNICORN -p $PID travail.main:app&


