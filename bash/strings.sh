#!/bin/bash

#echo "Enter passwd"
#read input1
#
#echo "Repeat passwd"
#read input2
#
#if [ $input1 == $input2 ]
#then
#	echo "Correct passwd"
#else
#	echo "Wrong passwd"
#fi

echo "Ingrese una palabra"
read palabra
echo ${palabra,} # Convertir a minusculas (solo con una lo hace con la primer letra)
echo ${palabra^} # Convertir a mayusculas
echo ${palabra^^[aeiou]} # Afecta a los caracteres en []
