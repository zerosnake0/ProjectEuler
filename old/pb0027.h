#ifndef __PB0027_H__
#define __PB0027_H__

#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <map>

namespace PB0027
{

typedef unsigned long long int ll;

const int max = 2000000;

int bp[max];

void cal()
{
    memset(bp,0,sizeof(bp));
    bp[2] = 1;
    for(unsigned int i = 3; i < max; i += 2)
        bp[i] = 1;
    
    for(unsigned int i = 3; i < max; i += 2)
        if(bp[i])
            for(unsigned int j = i; j * i < max; j += 2)
                bp[j * i] = 0;
    
    int maxn = 0;
    int pdt = 0;
    for(int a = -999; a <= 999; ++a)
    {
        for(int b = -999; b <= 999; ++b)
        {
            int n = 0;
            int sum = n*(n+a)+b;
            while(sum >= 0 && bp[sum])
            {
                ++n;
                sum = n*(n+a)+b;
            }
            if(n > maxn)
            {
                maxn = n;
                pdt = a*b;
            }
        }
    }
    
    std::cout << pdt << std::endl;
}

}


#endif