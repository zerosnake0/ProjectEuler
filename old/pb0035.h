#ifndef __PB0035_H__
#define __PB0035_H__

#include <string.h>
#include <iostream>
#include <assert.h>

namespace PB0035
{

const unsigned int max = 1000000;

char bp[max];

unsigned int next(unsigned int n)
{
    unsigned int i = n;
    unsigned int j = 0;
    while(i > 0)
    {
        ++j;
        i /= 10;
    }

    i = n % 10;
    for(;j>1; --j)
        i *= 10;
    
    return i + n / 10;
}

int check(unsigned int n)
{
    while(n>0)
    {
        if(n % 10 == 0)
            return 0;
        n /= 10;
    }
    return 1;
}

void cal()
{
    memset(bp, 0, sizeof(bp));
    bp[2] = 1;
    for(unsigned int i = 3; i < max; i += 2)
        bp[i] = 1;
        
    for(unsigned int i = 3; i < max; i += 2)
        if(bp[i])
            for(unsigned int j = i; j * i < max; j += 2)
                bp[j*i] = 0;

    unsigned int c = 1;
    
    for(unsigned int i = 3; i < max; i += 2)
        if(bp[i] && check(i))
        {
            int b = 1;
            unsigned int j = next(i);
            while(j != i)
            {
                if(!bp[j])
                {
                    b = 0;
                    break;
                }
                j = next(j);
            }
            if(b)
                ++c;
        }
        
    std::cout << c << std::endl;
}

}


#endif