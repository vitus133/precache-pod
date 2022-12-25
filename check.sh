#!/bin/bash

cat images | while read line || [[ -n $line ]];
do
   img="${line%\"}"
   img="${img#\"}"
   podman image exists $img
   rc=$?
   if [ ! $rc == 0 ]; then
     echo "image $img not found"
     exit 1
   fi
done
exit 0
