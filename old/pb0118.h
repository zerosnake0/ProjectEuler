#ifndef __PB0118_H__
#define __PB0118_H__

#include <stdio.h>

namespace PB0118
{

typedef long long int ll;

bool bPrime(ll n)
{
    if(n<2)
        return false;
    
    if(n==2)
        return true;
    
    if((n&0x1) == 0)
        return false;
        
    for(unsigned int i = 3; i*i <= n; i+=2)
        if(n%i==0)
            return false;

    return true;
}

ll count[1<<9];

void printb(unsigned int n)
{
    char tmp[10];
    for(unsigned int i = 0; i < 9; ++i)
    {
        tmp[8-i] = '0' + (n & 0x1);
        n >>= 1;
    }
    tmp[9] = '\0';
    printf(tmp);
}

ll cal2(unsigned int n)
{
    if(n==0)
        return 1;
    
    ll c = 0;
    
    unsigned int i = n;
    unsigned int j = 0;
    
    while(i>0)
    {
        ++j;
        i >>= 1;
    }
    
    j = 1 << (j-1);
    
    for(unsigned int i = n; i>=j; i = (i-1)&n)
    {
        if(count[i] > 0)
            c += count[i] * cal2(n-i);
    }
    
    return c;
}

ll cal()
{
    memset(count, 0, sizeof(count));
    
    for(unsigned int i = 2; i <= 987654321; ++i)
    {
        unsigned int c = 0;
        unsigned int j = i;
        while(j>0)
        {
            unsigned int rest = j%10;
            if(rest==0)
                break;
            
            unsigned int f = (1<<(rest-1));
            if(c & f)
                break;
                
            c |= f;
            j /= 10;
        }
        if(j>0)
            continue;
        
        if(bPrime(i))
        {
            ++count[c];
        }
    }
    
    
    for(unsigned int i = 0; i < (1<<9); ++i)
        if(count[i])
        {
            printb(i);
            printf(" %llu\n", count[i]);
        }
    
    printf("%llu\n", cal2((1<<9)-1));
    return 0;
}

}


#endif