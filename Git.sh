#!/usr/bin/bash

#To avoid repeatitive typing of updating commit, this simple script was made.
# Unstable Version
echo "All changes will be added except for the files added in .gitignore"
git add .

echo "Enter commit message"
read "msg" #This place can't handle a sentence, just a word.

git commit -m $msg