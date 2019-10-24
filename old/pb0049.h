#ifndef __PB0049_H__
#define __PB0049_H__

#include <stdio.h>
#include <assert.h>
#include <iostream>
#include <string>

namespace PB0049
{

int bp[10000];

bool bper(unsigned int i, unsigned int j)
{
    int count[10];
    memset(count,0,sizeof(count));
    unsigned int k = i;
    while(k>0)
    {
        ++count[k%10];
        k /= 10;
    }
    k = j;
    while(k>0)
    {
        --count[k%10];
        k /= 10;
    }
    for(k=0;k<10;++k)
        if(count[k]!=0)
            return false;
    
    return true;
}

void cal()
{
    memset(bp,0,sizeof(bp));
    bp[2] = 1;
    for(unsigned int i = 3; i < 10000; i += 2)
        bp[i] = 1;
    
    for(unsigned int i = 3; i < 10000; i += 2)
        if(bp[i])
            for(unsigned int j = i; i * j < 10000; j += 2)
                bp[i * j] = 0;

    unsigned int p[10000];
    unsigned int pc = 0;

    for(unsigned int i = 1000; i < 10000; ++i)
    {
        if(!bp[i])
            continue;
        
        p[pc++] = i;
    }
    
    for(unsigned int i = 0; i < pc - 2; ++i)
    {
        for(unsigned int j = i + 1; j < pc - 1; ++j)
        {
            if (!bper(p[i],p[j]))
                continue;
            
            unsigned int k = 2*p[j]-p[i];
            
            if(k>=10000)
                continue;
            
            if(!bp[k])
                continue;
            
            if(!bper(p[i],k))
                continue;
                
            printf("%u %u %u\n",p[i],p[j],k);
        }
    }
}

}

#endif