#!/bin/bash

edad=18
sexo="masculino"

if [ $edad -ge 18 ]
then
	if [ $sexo = "masculino" ]
	then
		echo "Hombre mayor de edad"
	else
		echo "Mujer mayor de edad"
	fi
else
	if [ $sexo = "masculino" ]
	then
		echo "Hombre menor de edad"
	else
		echo "Mujer menor de edad"
	fi
fi
