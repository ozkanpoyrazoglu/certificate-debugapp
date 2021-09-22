#!/bin/sh

certificates=$(ls -l /certificates | grep .crt | awk -F ' ' '{ print $9 }' ORS=' ')

for i in $certificates;
do
	echo $i
	openssl x509 -in /certificates/$i -noout -text |grep ' Not '
done