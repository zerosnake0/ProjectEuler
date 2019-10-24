#ifndef __PB0032_H__
#define __PB0032_H__

#include <string.h>
#include <iostream>
#include <assert.h>
#include <stdio.h>
#include <map>

namespace PB0032
{

int b[10000];
int bb[10000];

void printb(int n)
{
    for(int i=0;i<9;++i)
    {
        putchar('0'+(n&0x1));
        n >>= 1;
    }
    putchar('\n');
}

void cal()
{
    memset(b,0,sizeof(b));
    

    for(int i = 2; i <= 9999; ++i)
    {
        int j = i;
        int c = 0;
        while(j > 0)
        {
            int k = j % 10;
            if(k==0)
            {
                c = -1;
                break;
            }
            
            int f = 1 << (k-1);
            if(c & f)
            {
                c = -1;
                break;
            }
            c |= f;
            j /= 10;
        }
        b[i] = c;
    }
    /*
    for(int i = 10; i <= 100; ++i)
    {
        printf("%d ",i);
        int j = b[i];
        if(j != -1)
        {
            while(j)
            {
                putchar('0'+(j&0x1));
                j >>= 1;
            }
        }
        putchar('\n');
    }*/
    memset(bb,0,sizeof(bb));
    for(int i = 2; i <= 9; ++i)
    {
        for(int j = 1234; j * i <= 9999; ++j)
        {
            if(b[j] == -1)
                continue;
            
            if(b[j] & b[i])
                continue;
            
            int pdt = i*j;
            if(b[pdt] == -1)
                continue;
            
            if(b[pdt] & (b[j] | b[i]))
                continue;
                
            printf("%d %d %d\n", i, j, pdt);
           
            bb[pdt] = 1;
        }
    }

    for(int i = 12; i <= 98; ++i)
    {
        if(b[i] == -1)
            continue;
        
        for(int j = 123; j * i <= 9999; ++j)
        {
            if(b[j] == -1)
                continue;
            
            if(b[j] & b[i])
                continue;
            
            int pdt = i*j;
            if(b[pdt] == -1)
                continue;
                
            if(b[pdt] & (b[j] | b[i]))
                continue;
            
            printf("%d %d %d\n", i, j, pdt);
            
            bb[pdt] = 1;
        }
    }
    
    int c = 0;
    for(int i = 1000; i<10000; ++i)
        if(bb[i])
            c += i;
            
    printf("%d\n",c);
    
}

}


#endif