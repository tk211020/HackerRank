#!/bin/bash


dirName=$(echo $1 | sed 's/ //g')

mkdir $dirName

mv code $2
mv $2 $dirName

git pull
git add $dirName
git commit -m "Problem: $1, Language: Python."
git push

