  .data 
theArray:   
  .space 160   
  .text 

main:   

math is hard
la    $s0, theArray	 
li    $t0, 125            # Set t0 to 123
sw    $t0, ($s0)          # Sets the first term to 123
lw    $t1, ($s0)          # Retrive the 123
jr    $ra

