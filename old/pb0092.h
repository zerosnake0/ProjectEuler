#ifndef __PB0092_H__
#define __PB0092_H__

#include <string.h>
#include <iostream>

namespace PB0092
{

const unsigned int max = 10000000;
int b[max];

void cal()
{
    memset(b, 0, sizeof(b));
    for(unsigned int i = 1; i < max; ++i)
    {
        unsigned int j = i, k = 0;
        while(j>0)
        {
            unsigned int m = j%10;
            k += m*m;
            j /= 10;
        }
        b[i] = k;
    }
    
    unsigned int c = 0;
    for(unsigned int i = 1; i < max; ++i)
    {
        while(b[i]!=1 && b[i]!=89)
            b[i] = b[b[i]];
        
        if(b[i]==89)
            ++c;
    }
    
    std::cout << c << std::endl;
}


}


#endif