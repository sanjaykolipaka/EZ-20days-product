//Implement a 2d array and rotate the matrix 90 degrees
#include<stdio.h>
main()
{
	int a[10][10],n,i,j;
	printf("Enter n:");
	scanf("%d",&n);
	for(i=0;i<n;i++)     
	{
		for(j=0;j<n;j++) 
			scanf("%d",&a[i][j]);
	}
	printf("matrix after 90* rotaion\n");
	for (j = 0;j<n;j++)
	{
		for(i=n-1;i>=0;i--)
		{
			printf("%d\t",a[i][j]);
		}
		printf("\n");
	}
}
