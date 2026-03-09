#!/bin/bash

echo "Elija un numero entre el 1 y el 3"
read valor

case $valor in
	1)
		echo "Usted eligio el 1"
	;;
	2)
		echo "Usted eligio el 2"
	;;
	3)
		echo "Usted eligio el 3"
	;;
	*)
		echo "Debe ser entre el 1 y el 3"
	;;
esac
