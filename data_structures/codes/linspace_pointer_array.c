#include <stdio.h>
#include <stdlib.h>

//Main function
int main(void)
{
//Variable declarations
double a = -1.0, l = 1.0, d, *ap;
int n = 100, i;

//Creating memory for ap
ap = (double *)malloc(n * sizeof(double));

//Common difference
d = (l-a)/(n-1);

//Generating the AP array
for(i = 0; i < 100; i++)
{
ap[i] = a+i*d;
}

//Printing values
for(i = 0; i < n; i++)
	printf("%lf\n",ap[i]);

free(ap);
return 0;
}

