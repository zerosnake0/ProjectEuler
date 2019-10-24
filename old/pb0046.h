#ifndef __PB0046_H__
#define __PB0046_H__

#include <string.h>
#include <iostream>
#include <assert.h>
#include <stdio.h>
#include <map>

namespace PB0046
{

bool bPrime(unsigned int n)
{
    if(n<2)
        return false;

    if(n==2)
        return true;

    if((n&0x1) == 0)
        return false;

    for(unsigned int i = 3; i*i <= n; i+=2)
        if(n%i==0)
            return false;

    return true;
}
void cal()
{
    for(unsigned int i = 35;;i+=2)
    {
        if(bPrime(i))
            continue;
            
        bool b = false;
        for(unsigned int j = 1; 2 * j * j < i; ++j)
        {
            if(bPrime(i-2*j*j))
            {
                b = true;
                break;
            }
        }
        
        if(!b)
        {
            printf("%u\n", i);
            break;
        }
    }
}

}

#endif