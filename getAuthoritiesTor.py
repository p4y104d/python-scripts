#!/usr/bin/env python
from stem.descriptor.remote import get_authorities
dirs = get_authorities()
for dir in dirs.keys():
    print ''
    print 'Nombre del nodo: %s \n, Direccion IP: %s \n, OR_PORT: %s \n, DIR_PORT: %s \n, Fingerprint: %s \n, V3Ident (Votar en el consenso) %s ' %(dirs[dir].nickname, dirs[dir].address, dirs[dir].or_port, dirs[dir].dir_port, dirs[dir].fingerprint, dirs[dir].v3ident) 

