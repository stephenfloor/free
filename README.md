# free
A simple analog of the *NIX free utility for OSX.  Monitor memory usage. 

Essentially this utility reports all memory that is marked as purgeable as free as opposed to most OSX utilities.  Usage should mirror that after invoking the "purge" command, but without the loss of cached information associated with running purge.   

Also note that by default OSX swap is allocated in blocks so "free" swap only reports the currently allocated blocks.  OSX will allocate more swap blocks if necessary, up to remaining disk space. 

## usage

free

## sample output

Used Memory:            9.24 GB
Free Memory:            54.73 GB
Swap:                    used = 7.85M  free = 248.15M


