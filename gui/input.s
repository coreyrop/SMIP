# "Hello World" in MIPS assembly
# From: http://labs.cs.upt.ro/labs/so2/html/resources/nachos-doc/mipsf.html
	
	# All program code is placed after the
	# .text assembler directive
	.text

	# Declare main as a global function
	.globl	main
	
# The label 'main' represents the starting point
main:

	# your code here
	addi $t0, $0, 3
	addi $t1, $0, 5
	add $t4, $t0, $t1


	# All memory structures are placed after the
	# .data assembler directive
	.data
