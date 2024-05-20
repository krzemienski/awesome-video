#!/bin/sh

if [ "$GITHUB_REF" != "refs/heads/master" ]
then
  exit
fi

git checkout master

remote=$(git config remote.origin.url)

git config user.name "READMEbot"
git config user.email "readmebot@users.noreply.github.com"
git config --global user.password $GH_TOKEN > /dev/null 2>&1

echo add readme
git add README.md database.json

echo commit
git commit -m "[auto] [ci skip] Generate README & Database.json"

echo push
git push --quiet --force origin master > /dev/null 2>&1
