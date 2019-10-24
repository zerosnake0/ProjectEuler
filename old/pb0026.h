#ifndef __PB0026_H__
#define __PB0026_H__

#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <map>

namespace PB0026
{

typedef unsigned long long int ll;

void cal()
{
    unsigned int max = 0, maxk = 0;
    for(unsigned int d = 2; d < 1000; ++d)
    {
        if(d%2 == 0)
            continue;
        
        if(d%5 == 0)
            continue;
        
        //std::cout << d << ' ';
        
        unsigned int k = 0;
        unsigned int i = 10;
        do 
        {
            i = (i%d)*10;
            ++k;
        } while (i!=10);
        
        
        //std::cout << k << std::endl;
        
        if(k > maxk)
        {
            maxk = k;
            max  = d;
        }
    }
    
    std::cout << max << std::endl;
}

}


#endif