#!/bin/bash
#This script will email us our user, IP and hostname
emailaddr="al12gamer@gmail.com"
today=$(date +"%m-%d-%Y")
ip=$(ifconfig | grep 'inet 10' | awk '{print $2}')

printf -v content "User:\t%s\nHostname:\t%s\nIP:\t%s\n" $USER $HOSTNAME $ip

mail -s "IT3038C Linux IP" $emailaddr <<<$content