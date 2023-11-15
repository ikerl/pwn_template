#===========================================================
#                    FORMAT STRINGS
#===========================================================

fmtstr_payload(1, {0x0: 0x1337babe}, write_size='short', numbwritten=0)

int.from_bytes(bytes_data,"little")

#===========================================================
#                    SIGRETURN
#===========================================================

context.arch = "amd64"
frame = SigreturnFrame()
frame.rax = constants.SYS_write
frame.rdi = constants.STDOUT_FILENO
frame.rsi = binary.symbols['message']
frame.rdx = len(message)
frame.rsp = 0xdeadbeef
frame.rip = binary.symbols['syscall']

#===========================================================
#                    MISC
#===========================================================

binsh = next(libc.search(b'/bin/sh'))

# Hex string to bytes
bytes.fromhex(hex_string.replace(b"0x",b""))

# Offset calculation
cyclic(20)
cyclic_find(b'baaa')