#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    int i, j;
    int sum=0;
    scanf("%d", &n);
    int a[n];
    for(i=0; i<n; i++){
        scanf("%d", &a[i]);
    }
    int swp;
    int key;
    for(i=1; i<n; i++){
        key=a[i];
        for(j=i-1; j>=0&&key<a[j]; j--){
            a[j+1]=a[j];
        }
        a[j+1]=key;
    }
    for(i=0; i<n; i++){
        for(j=0; j<=i; j++){
            sum=sum+a[j];
        }
    }
    printf("%d", sum);
    return 0;
}
