#!/bin/bash

n=1
# verificando se a variavel n e menor ou igual a 5 usando -le
# o loop começa com "do"
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1)) #usamos aspas duplas para que permita fazer operacoes matematicas
done
#termina com "done"