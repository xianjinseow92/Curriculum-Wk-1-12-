#!/bin/bash

for i in `seq 0 10`;
do 
  curl https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data > data$i.txt
done
