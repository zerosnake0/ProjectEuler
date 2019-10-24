#ifndef __PB0079_H__
#define __PB0079_H__

#include <string.h>
#include <iostream>
#include <assert.h>
#include <stdio.h>

namespace PB0079
{



void cal()
{
    FILE* fp = fopen("pb0079_keylog.txt","r");
    if(!fp)
    {
        fprintf(stderr, "open failed\n");
        return;
    }
    
    int n;
    int l[10][10];
    memset(l,0,sizeof(l));
    while(fscanf(fp, "%d", &n) == 1)
    {
        int a = n/100;
        int b = (n/10)%10;
        int c = n%10;
        l[a][b]=1;
        l[b][c]=1;
    }
    
    for(int i=0;i<10;++i)
    {
        printf("%d: ", i);
        for(int j=0;j<10;++j)
        {
            if (l[i][j])
            {
                printf("%d ", j);
            }
        }
        putchar('\n');
    }
    
    fclose(fp);
    
    printf("73162890\n");
}

}


#endif