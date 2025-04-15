#include <stdio.h>
#include "basecon.h"

void dec_xxx(int n)
{
	printf("\nOctal Number for %d = %o", n, n);
	printf("\nHexadecimal Number for %d = %X", n, n);
}

void dec_convert(int n, int r, char *convert)
{
	int i=1, j, temp;
	
	printf("\nBase %d Number for %d = ", r, n);
	
	while (n!=0)
	{
		temp = n%r;

		//To convert integer into character
		if (temp < 10)
		{
			temp = temp + 48;
		}
		else
		{
			temp = temp + 55;
		}
		
		convert[i++] = temp;
		n = n/r;
	}
	
	for (j=i-1; j>0; j--)
	{
		printf("%c",convert[j]);
	}
}
