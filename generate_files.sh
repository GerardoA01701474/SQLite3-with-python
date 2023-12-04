#!/bin/bash
count=0
while [ "$count" -lt 10 ]; do
    rm file$count.txt
    count=$((count + 1))
done