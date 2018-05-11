#!/bin/bash
i=1
while [ $i -le 254 ]
do
        ping -c1 -i0.2 -w1 176.202.140.$i &>/dev/null
        if [ $? -eq 0 ]
        then
        echo 176.202.140.$i is up
        else
        echo 176.202.140.$i is down
        fi
        let i++
done

