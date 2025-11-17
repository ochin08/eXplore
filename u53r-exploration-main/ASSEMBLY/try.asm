



; hello64.asm
section .data
    msg db "Hello, 64-bit World!", 0xA
    len equ $ - msg

section .text
    global _start

_start:
    mov rax, 1          ; sys_write
    mov rdi, 1          ; stdout
    mov rsi, msg        ; address of msg
    mov rdx, len        ; length
    syscall             ; make system call

    mov rax, 60         ; sys_exit
    xor rdi, rdi        ; return 0
    syscall
