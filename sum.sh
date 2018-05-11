#!/bin/bash
i=0
while [ $i -le 20 ]
do
	let i++
	[ $[i%6] -ne 0 ] && continue
	echo $[i*i]
done

exit 2
