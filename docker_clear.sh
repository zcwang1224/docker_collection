#!/bin/bash


echo " ================ Container  ================"
docker container ls -a
echo

echo " ================ Image ================"
docker image ls

echo 
read -p "確定清空?(Y/n)" is_confirm

if [[ ! ${is_confirm^} == 'Y'  ]]; then
	exit 0
fi



docker container rm -f `docker container ls -aq`
docker image rm -f `docker image ls -aq`

echo " ================ Container  ================"
docker container ls -a

echo " ================ Image ================"
docker image ls

exit 0
