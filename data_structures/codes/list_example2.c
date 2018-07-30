#include <stdio.h>
#include <stdlib.h>

typedef struct abc
{
    int data;
    struct abc *next;        
}node;


//insert data to list
node *insert(int num, node *list)
{
	list->next = ( node *)malloc(sizeof( node));//creating new node
	list->next->next = NULL;
	list->next->data = num;
	return list->next;
	
	
}
//display the list
void display(node *list)
{
//node *temp;
//temp = head;
while (list != NULL)
{
//	printf("Enter display");
	printf("%d ",list->data);
//	printf("Entered display function\n");
	list = list->next;
	
}
}

int main()
{
	int i, num,count=0;
	node *list=NULL,*head=NULL;

while(1)
{
	
	printf("\n List Operations:\n");
    printf("===============\n");
    printf("1.Insert\n");
    printf("2.Display\n");
    printf("3.Size\n");
    printf("4.Delete\n");
    printf("5.Exit\n");
    printf("Enter your choice : ");
    
    scanf("%d", &i);
    
    switch(i)
    {
		case 1: if (count == 0)
				{
					head= ( node *)malloc(sizeof( node));
					scanf("%d",&num);
					head->data = num;
					list = head;
				}
				else
				{				
					scanf("%d",&num);
					list = insert(num, list);
				}
	//			printf("The list entry is %d",list->data);
				count++;
				break;
		case 2: 
				display(head);
				break;
		case 5: return 0;
		default:    printf("Invalid option\n");
	}
    
    

}
return 0;
}
