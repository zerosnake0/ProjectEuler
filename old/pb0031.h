#ifndef __PB0031_H__
#define __PB0031_H__

#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <map>

namespace PB0031
{

using namespace std;

const int p[] = {1,2,5,10,20,50,100,200};
const int pc = 8;

unsigned int f(unsigned int sum, unsigned int begin = 0)
{
    if(sum==0)
        return 1;
    
    if(begin >= pc)
        return 0;
    
    unsigned int c = 0;
    unsigned int cm = sum/p[begin];
    for(unsigned int i = 0; i <= cm; ++i)
        c += f(sum - i * p[begin], begin + 1);

    return c;
}

void cal()
{
    cout << f(200) << endl;
}

}


#endif