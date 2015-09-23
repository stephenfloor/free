#!/usr/bin/python

import subprocess
import re

# Get process info
ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0]
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0]
swap = subprocess.Popen(['sysctl', 'vm.swapusage'], stdout=subprocess.PIPE).communicate()[0]

# Iterate processes
processLines = ps.split('\n')
sep = re.compile('[\s]+')
rssTotal = 0 # kB
for row in range(1,len(processLines)):
    rowText = processLines[row].strip()
    rowElements = sep.split(rowText)
    try:
        rss = float(rowElements[0]) * 1024
    except:
        rss = 0 # ignore...
    rssTotal += rss

# Process vm_stat
vmLines = vm.split('\n')
sep = re.compile(':[\s]+')
vmStats = {}
for row in range(1,len(vmLines)-2):
    rowText = vmLines[row].strip()
    rowElements = sep.split(rowText)
    vmStats[(rowElements[0])] = int(rowElements[1].strip('\.')) * 4096 /1024.**3 # in GB 

# process swap output 
swapLines = swap.split('\n')

free = vmStats["Pages free"]
active = vmStats["Pages active"]
inactive = vmStats["Pages inactive"]
speculative = vmStats["Pages speculative"]  
wired = vmStats["Pages wired down"]
purgeable = vmStats["Pages purgeable"]
filecache = vmStats["File-backed pages"]
anonymous = vmStats["Anonymous pages"]

#print 'Wired Memory:\t\t%3.2f GB' % wired
#print 'Active Memory:\t\t%3.2f GB' % active
#print 'Inactive Memory:\t%3.2f GB' % inactive
#print 'Real Mem Total (ps):\t%3.2f GB' % ( rssTotal/1024/1024/1024. )
#print 'Anonymous pages:\t%3.2f GB' % anonymous
print 'Used Memory:\t\t%3.2f GB' % (anonymous + wired)
print 'Free Memory:\t\t%3.2f GB' % (free + filecache) #(64 - (rssTotal/1024.**3 + wired))#free + purgeable + speculative) 
#print 'File cache:\t\t%3.2f GB' % filecache
#print 'Total memory:\t\t%3.2f GB' % (wired+active+free+inactive+purgeable+speculative)
print 'Swap:\t\t\t%s' % swapLines[0][30:-13]
