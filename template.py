#!/usr/bin/env python3

from pwn import *

context.update(arch='amd64')
exe = './pwn'
argv = ''
LOCAL = True # True / False


host = '' # Hostname or IP address
port = 4444 # Port
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

def exploit(io,elf):

    # data = io.recvline()
    # data = io.recvuntil(b"end")
    # io.sendline(b"data")
    io.interactive()


#===========================================================
#                INITIALIZATION GOES HERE
#===========================================================

if LOCAL:
    with gdb.debug(exe + '' + argv, gdbscript=gdbscript) as io:
        exploit(io, ELF(exe))
else:
    with remote(host, port) as io:
        exploit(io, ELF(exe))