#docker rm -vf $(docker ps -a -q)

#docker stop remaincont
#docker rm  remaincount

docker run -p 8000:8000 -v /opt/remainder-app/:/code -d --name remaincont expery_remainder 