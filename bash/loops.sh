#!/bin/bash

#valor=0
#
#while [ $valor -le 10 ]
#do
#	echo $valor
#	valor=$((valor+1))
#done

for i in {0..100..10} # El segundo .. es el numero de incremento. de diez en diez
do
	echo $i
done
