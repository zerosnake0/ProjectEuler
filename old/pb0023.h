#ifndef __PB0023_H__
#define __PB0023_H__

#include <stdio.h>
#include <map>
#include <assert.h>

namespace PB0023
{

typedef unsigned long long int ll;

const unsigned int max = 28123;

int bp[max+1];
int ba[max+1];
int bw[max+1];

void init()
{
    bp[0] = bp[1] = 0;
    
    for(unsigned int i = 2; i <= max; ++i)
        bp[i] = 1;
    
    for(unsigned int i = 2; i <= max; ++i)
        if(bp[i])
            for(unsigned int j = i; i * j <= max; ++j)
                bp[i*j] = 0;
    
    memset(ba, 0, sizeof(ba));
    
    int coef[max+1];
    
    for(unsigned int i = 2; i <= max; ++i)
        if(!bp[i])
        {
            memset(coef, 0, sizeof(coef));
            unsigned int j = i;
            for(unsigned int k = 2; k < i && j >= k; ++k)
                if(bp[k])
                    while(j%k==0)
                    {
                        j /= k;
                        ++coef[k];
                    }

            assert(j==1);

            unsigned int tmp = 1;
            j = 1;
            for(unsigned int k = 2; j < i; ++k)
                if(coef[k])
                {
                    unsigned int c = 1;
                    unsigned int kk = coef[k];
                    while(kk-->0)
                        c *= k;

                    j *= c;
                    tmp *= (c*k - 1) / (k - 1);
                }

            
            tmp -= i;
            if(tmp > i)
                ba[i] = 1;
        }
    
    memset(bw, 0, sizeof(bw));
    
    for(unsigned int k = 0; k <= max; ++k)
        if(ba[k])
            for(unsigned int m = k; m + k <= max; ++m)
                if(ba[m])
                    bw[m+k] = 1;
}

void cal()
{
    init();

    ll c = 0;
    for(unsigned int i = 0; i <= max; ++i)
        if(!bw[i])
            c += i;

    printf("%llu\n",c);
}

}


#endif