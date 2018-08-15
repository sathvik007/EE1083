#include <stdio.h>
#include <stdlib.h>

double *linspace_pointer(double, double, int );
int main(void)
{
double a = -1.0, l = 1.0, *ap;
int n = 100, i;

//Assigning pointer to a
ap = linspace_pointer(a,l,n);

for(i = 0; i < n; i++)
	printf("%lf\n",ap[i]);

//Common difference

return 0;
}

double *linspace_pointer(double a, double l, int n)
{
//Variable declarations
double d, *ap;
int i;

//Creating memory for ap
ap = (double *)malloc(n * sizeof(double));

//Common difference
d = (l-a)/(n-1);

//Generating the AP
for(i = 0; i < 100; i++)
{
ap[i] = a+i*d;
}
//Returning the address of the first memory block
return ap;

}
