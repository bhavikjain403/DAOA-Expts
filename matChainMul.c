#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main()
{
    int n, *arr, i, j, k, table[100][100],x,c;
    printf("Enter number of elements : ");
    scanf("%d",&n);
    arr = (int *)malloc(n*sizeof(int));
    printf("Enter the elements :\n");
    for (i = 0; i < n; i++)
    {
        printf("Enter element %d : ", i + 1);
        scanf("%d", &arr[i]);
    }
    for(i=0;i<n-1;i++)
    table[i][i]=0;
    for(x=1;x<n-1;x++)
    {
        for(j=x;j<n-1;j++)
        {
            i=j-x;
            table[i][j]=INT_MAX;
            for(k=i;k<j;k++)
            {
                c = table[i][k]+table[k+1][j]+arr[i]*arr[k+1]*arr[j+1];
                if(table[i][j]>c)
                table[i][j]=c;
            }
        }
    }
    printf("The Cost/Comparison table is as follows :\n");
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-1;j++)
        {
            if(j>=i)
            {
                printf("%d\t",table[i][j]);
            }
            else
            printf("\t");
        }
        printf("\n");
    }
    printf("Minimum mul required is %d",table[0][n-2]);
    return 0;
}