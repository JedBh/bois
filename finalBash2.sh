#!/bin/bash

echo -e "Please enter number of rows: "
read rows

echo -e "Please enter number of columns: "
read columns

for (( i=1; i<=$rows; i++))
do
    for (( c=1; c<=$columns; c++))
    do
        echo -n "net4u "
    done
    echo -e ""
done