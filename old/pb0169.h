#ifndef __PB0169_H__
#define __PB0169_H__

#include <stdio.h>
#include <math.h>
#include <string>
#include <map>

namespace PB0169
{


/*
    if n is odd
    f(n) = f(n/2)
    else n is even
    f(n) = f(n/2) + f(n/2-1)
    
    
    178653872807
 */
using namespace std;

typedef unsigned long long int ll;

class l4
{
public:
    l4():hi(0),lo(0){}
    
    ll hi;
    ll lo;
    
    const char* c_str()
    {
        if(hi>0)
            sprintf(s, "%llx%llx", hi, lo);
        else
            sprintf(s, "%llx", lo);
        return s;
    }
    
    char s[20];
};

map<string, ll> res;

ll flag = 1;

ll f(l4& v)
{
    if(v.hi == 0 && v.lo == 0)
        return 1;
    
    string s = v.c_str();
    map<string, ll>::iterator it = res.find(s);
    if(it != res.end())
    {
        return it->second;
    }
        
    l4 v1 = v;
    v1.hi >>= 1;
    v1.lo >>= 1;
    if(v.hi&0x1)
        v1.lo |= flag;

    l4 v2 = v1;
    v2.lo -= 0x1;
    
    ll r = f(v1);
    if(!(v.lo & 0x1))
        r += f(v2);
        
    res.insert(map<string,ll>::value_type(s,r));
    return r;
}

void cal()
{
    ll p525 = 1;
    for(unsigned int i = 0; i < 25; ++i)
        p525 *= 5;
        
    flag <<= 63;
        
    l4 v;
    v.lo = p525 << 25;
    v.hi = p525 >> (64-25);
    
    printf("%llu\n", f(v));
}

}


#endif