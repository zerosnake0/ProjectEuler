#ifndef __PB0029_H__
#define __PB0029_H__

#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <map>

namespace PB0029
{

using namespace std;

typedef unsigned long long int ll;

int bc[101];

const int max = 100;

void cal()
{
    memset(bc,0,sizeof(bc));
    
    unsigned int count = 0;
    for(unsigned int a = 2; a <= max; ++a)
    {
        if(bc[a])
            continue;
        
        unsigned int b = a;
        unsigned int k = 1;
        
        map<int, int> cont;

        while(b <= max)
        {
            bc[b] = 1;
            for(unsigned int i = 2; i <= max; ++i)
                cont.insert(map<int,int>::value_type(i*k,1));
            b *= a;
            ++k;
        }
        
        count += cont.size();
    }
    
    cout << count << endl;
}

}


#endif