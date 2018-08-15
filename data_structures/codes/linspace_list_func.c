#include <stdio.h>
#include <stdlib.h>

typedef struct list
{
double data;
struct list *next;
}node;

node *linspace_pointer(double, double, int );

int main(void)
{
node *ap;
double a = -1.0, l = 1.0;
int n = 100;

//Getting the head of the AP list
ap = linspace_pointer(a,l,n);

//Printing the AP
while(ap->next != NULL)
{
	printf("%lf\n", ap->data);
	ap = ap->next; 
}

return 0;
}

node *linspace_pointer(double a, double l, int n)
{
//Variable declarations
node *ap, *head;
double d;
int i;

//Common difference
d = (l-a)/(n-1);

ap = (node *)malloc(sizeof(node));
head = ap;
//Generating the AP
for(i = 0; i < 100; i++)
{

ap->data = a+i*d;
//Creating memory for next node
ap->next = (node *)malloc(sizeof(node));
//Initializing next node	
ap->next->next = NULL;
//node increment
ap = ap->next;
}
//Returning the address of the first memory block
return head;

}
