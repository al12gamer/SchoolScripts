#!/bin/bash
#this is a script that will eventually show ip addresses
greeting="This is a script. Hello!"

echo $greeting
echo $greeting, "thanks for joining us!"
echo $greeting,"thanks for joining us! You owe me \$100"

echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session length: $SECONDS
echo Home Dir: $HOME

ip=