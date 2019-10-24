#ifndef __PB0036_H__
#define __PB0036_H__

#include <stdio.h>
#include <assert.h>
#include <iostream>
#include <string>


namespace PB0036
{

bool bP(const char* str)
{
    for(unsigned int i = 0, j = strlen(str)-1; i < j;++i,--j)
        if(str[i] != str[j])
            return false;
    
    return true;
}

void cal()
{
    char str[30];
    
    unsigned int c = 0;
    
    for(unsigned int i = 1; i < 1000000; ++i)
    {
        sprintf(str, "%u", i);
        if(!bP(str))
            continue;
        
        unsigned int j = i;
        unsigned int k = 0;
        while(j > 0)
        {
            str[k++] = '0' + (j & 0x1);
            j >>= 1;
        }
        str[k] = '\0';
        if(bP(str))
            c += i;
    }
    
    printf("%u\n", c);
}

}


#endif