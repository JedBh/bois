#!/bin/bash#!/bin/bash

script="mkdir Net4U; cd Net4U; touch {1..4}.txt; tar -cvzf net4u.tgz 1.txt 2.txt 3.txt 4.txt"

ssh jed@192.168.1.1 "${script}"
