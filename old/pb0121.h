#ifndef __PB0121_H__
#define __PB0121_H__

#include <stdio.h>

namespace PB0121
{

typedef unsigned long long int ll;

const int max = 15;

void cal()
{
    ll fz = 0, fm = 1;
    for(unsigned int i = 0; i < max; ++i)
        fm *= (i+2);
    
    for(unsigned int i = 0; i < (1<<max); ++i)
    {
        unsigned int k, c = 0, pdt = 1;
        for(k = 0; k < max; ++k)
        {
            if(i & (1<<k))
            {
                ++c;
                pdt *= (k+1);
            }
        }
        if(c <= max/2)
            fz += pdt;
    }
    
    printf("%llu\n", fm/fz);
}

}


#endif