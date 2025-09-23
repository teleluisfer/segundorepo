#!/bin/bash
echo `date`
#cpu use thresholdcpu_threshold='80'
#mem idle thresholdmem_threshold='100'
#disk use thresholddisk_threshold='90'
#---cpucpu_usage () {cpu_idle=`top -b -n 1 | grep Cpu | awk '{print }'|cut -f 1 -d "."`cpu_use=`expr 100 - $cpu_idle` echo "cpu utilization: $cpu_use"if then echo "cpu warning!!!" else echo "cpu ok!!!"fi}#---memmem_usage () { #MB unitsmem_free=`free -m | grep "Mem" | awk '{print +}'` 
echo "memory space remaining : $mem_free MB"if then echo "mem warning!!!" else echo "mem ok!!!"fi}#---diskdisk_usage () {disk_use=`df -P | grep /dev | grep -v -E '(tmp|boot)' | awk '{print }' | cut -f 1 -d "%"` 
echo "disk usage : $disk_use" if then echo "disk warning!!!" else echo "disk ok!!!"fi }cpu_usagemem_usagedisk_usage
