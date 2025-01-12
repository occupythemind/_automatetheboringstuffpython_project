#!/usr/bin/bash

#To avoid repeatitive typing of updating commit, this simple script was made.

echo "All changes will be added except for the files added in .gitignore"
git add .

echo "Enter commit message"
read msg

git commit -m $msg