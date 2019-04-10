# Welcome to Practice! Write some code!!
.globl main
.globl init_values
.globl end_program
.globl print_value

# $t0 = $s5
# $s5 += $t0
# $s5 += $t0
# $s5 += $t0
# $s5 += $t0
# $s5 += $t0
#
# $s4 = $s5 + $s3
# $s4 -= $s2

.text
init_values:
	addi $s4, $0, 4
	addi $s5, $0, 4
	addi $s3, $0, 4
	addi $s2, $0, 4
	jr $ra
	add $0, $0, $0

main:
	jal init_values
	add $0, $0, $0
	
	add $t0, $s5, $0
	add $s5, $s5, $t0
	add $s5, $s5, $t0
	add $s5, $s5, $t0	
	add $s5, $s5, $t0
	add $s5, $s5, $t0

	add $s4, $s5, $s3
	
	sub $s4, $s4, $s2

	jal print_value
	add $0, $0, $0
	j end_program
	add $0, $0, $0

print_value:
	addi $v0, $0, 1
	add $a0, $s4, $0
	syscall
	jr $ra
	add $0, $0, $0
	
end_program:
	addi $v0, $0, 10
	syscall



