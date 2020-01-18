#!/bin/sh
echo "BEGIN $(date)"

err="ERROR:"
fix="SUGGESTED FIX:"

if grep -e "\\.*\\s$" ../README.md ;
then
  echo "${err} End-of-line whitespace detected."
  echo "${fix} Remove spaces at end of lines. Link lines should end in period (.) followed by newline only."
  exit 1
fi

grep -E -orh --line-buffered "(http(s)?://){1}[^'\\)]+" README.md >urls.tmp
while read -r LINE; do
    curl -o /dev/null --silent --progress-bar --head --write-out '%{http_code} %{time_starttransfer} %{url_effective}\n' "$LINE" >> urls_result.tmp
    sleep 2
done < urls.tmp

if grep '000 ' urls_result.tmp ;
then
  echo "${err} URL check failed."
  echo "${fix} Check URL spelling and that resource is online."
  exit 1
fi

echo "DONE $(date)"