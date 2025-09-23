#!/bin/bash

while true; do
    uso_cpu=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1 "%"}')
    echo "$(date) - Uso de la CPU: $uso_cpu" >> monitoreo_cpu_archivo.log
    sleep 1
done
