#!/bin/bash

for filename in $( ls data{0..10}.txt );
do
  echo "Cleaning $filename"
  sed -i "" s/'?  '/nan/g $filename
done
