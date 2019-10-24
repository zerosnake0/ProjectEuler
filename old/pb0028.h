#ifndef __PB0028_H__
#define __PB0028_H__

#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <map>

namespace PB0028
{

typedef unsigned long long int ll;

void cal()
{
    unsigned int sum = 1;
    unsigned int a = 1;
    for(unsigned int i = 2; i < 1001; i+=2)
    {
        a += i; sum += a;
        a += i; sum += a;
        a += i; sum += a;
        a += i; sum += a;
    }
    std::cout << sum << std::endl;
}

}


#endif