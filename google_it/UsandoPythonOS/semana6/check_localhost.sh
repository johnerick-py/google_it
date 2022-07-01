#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
    echo "tudo ok"
else
    echo "ERRO! 127.0.0.1 nao esta em /etc/hosts"
fi 