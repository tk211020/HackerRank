#!/bin/bash




mv code $2

if [ "$3" = "py" ]
then
        lan="Python"
elif [ "$3" = "js" ]
then
        lan="JavaScript"
else
        lan=$3
fi

git pull
git add $dirName
git commit -m "Problem: $1, Language: $3."
git push
