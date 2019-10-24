#ifndef __PB0030_H__
#define __PB0030_H__

#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <map>

namespace PB0030
{

using namespace std;

typedef unsigned long long int ll;

int pdt[10];

void cal()
{
    for(unsigned int i = 0; i <= 9; ++i)
        pdt[i] = i;
    
    for(unsigned int i = 2; i <= 9; ++i)
    {
        pdt[i] *= i; pdt[i] *= pdt[i]; pdt[i] *= i;
    }
        
    unsigned int sum = 0;
    
    for(unsigned int i = 2; i < 420000; ++i)
    {
        unsigned int j = i;
        unsigned int s = 0;
        while(j > 0)
        {
            s += pdt[j%10];
            j /= 10;
        }
        if(s==i)
        {
            cout << i << '\n';
            sum += i;
        }
    }
    
    cout << '\n' << sum << '\n';
}

}


#endif