# "Hello World" in MIPS assembly
# From: http://labs.cs.upt.ro/labs/so2/html/resources/nachos-doc/mipsf.html
	
	# All program code is placed after the
	# .text assembler directive
	.text

	# Declare main as a global function
	.globl	main
	
# The label 'main' represents the starting point
main:
	# Run the print_string syscall which has code 4
	addi $v0, $0, 100
	addi $s6, $0, 1000

	# All memory structures are placed after the
	# .data assembler directive
	.data

	# The .asciiz assembler directive creates
	# an ASCII string in memory terminated by
	# the null character. Note that strings are
	# surrounded by double-quotes
msg:	.asciiz	"Hello World!\n"
