#ifndef __PB0100_H__
#define __PB0100_H__

#include <stdio.h>
#include <assert.h>
#include <iostream>
#include <string>

namespace PB0100
{

/*
    2b(b-1) = n(n-1)
    
    Diophantine Quadratic Equation
    
    b' = 3b + 2n - 2
    n' = 4b + 3n - 3

*/
typedef unsigned long long int ll;

const ll limit = 1000000000000;

void cal()
{
    ll b = 85;
    ll n = 85 + 35;
    
    while(n < limit)
    {
        ll tmp = b;
        b = b*3 + 2*n - 2;
        n = 4*tmp + 3*n - 3;
    }
    
    std::cout << b << std::endl;
}

}

#endif