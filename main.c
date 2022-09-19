#include <stdio.h>

int main(int argc, const char *argv[])
{
	Counter=InterruptPeriod;
	PC=InitialPC;
	tick = 0

	for(;;){
		switch(state) {
		case RAISE:
			break;
		case HIGH:
			break;
		case FALL:
			break;
		case LOW:
			tick += 1
			break;
		}
	}

	OpCode=Memory[PC++];
	Counter-=Cycles[OpCode];

  	switch(OpCode)
  	{
    case OpCode1:
    case OpCode2:
    	...
  	}

  	if(Counter<=0)
  	{
    /* Check for interrupts and do other */
    /* cyclic tasks here                 */
    ...
    	Counter+=InterruptPeriod;
    	if(ExitRequired) break;
  	}

	return 0;
}
