#ifndef __PB0240_H__
#define __PB0240_H__

#include <stdio.h>
#include <assert.h>

namespace PB0240
{

typedef unsigned long long int ll;

//#define TEST1
#ifdef TEST1
const int top = 3;
const int total = 15;
const int max = 6;
const int rest = 2;
#else
const int top = 10;
const int total = 70;
const int max = 12;
const int rest = 10;
#endif

int tmp[top];
ll res = 0;
int numc[max+1];
int numc2[max+1];
int numc3[max+1];
int mm;


#define MAX 30
ll ccc[MAX+1][MAX+1];

void init()
{
    ccc[0][0] = 1;
    for(int i = 1; i <= MAX; ++i)
    {
        ccc[i][0] = ccc[i][i] = 1;
        for(int j = 1; j < i; ++j)
            ccc[i][j] = ccc[i-1][j-1] + ccc[i-1][j];
    }
}

bool incr()
{
    for(int i = mm; i >= 1; --i)
    {
        if(numc2[i]==rest)
            numc2[i] = 0;
        else
        {
            ++numc2[i];
            return true;
        }
    }
    return false;
}

bool ok()
{
    int co = 0;
    for(int i = mm; i >= 1; --i)
        co += numc2[i];
    
    return (co == rest);
}

void count2()
{
    memset(numc2, 0, sizeof(numc2));
    mm = 1;
    for(; mm<=max;++mm)
        if(numc[mm]!=0)
            break;
    numc2[mm] = rest;
    do 
    {
        if(ok())
        {
            for(int i = 1; i<=max;++i)
                numc3[i] = numc[i] + numc2[i];
            
            ll ttt = 1;
            ll tlt = top+rest;
            
            for(int i = 1; i<=max;++i)
                if(numc3[i]!=0)
                {
                    ttt *= ccc[tlt][numc3[i]];
                    tlt -= numc3[i];
                }
                
                
            assert(tlt == 0);
            res += ttt;
        }
    } while (incr());
}

ll count(int num, int sum, int least)
{
    ll c = num * least;
    
    if(sum < c)
        return 0;
    
    if(sum == c)
    {
        for(int i = top-num; i<top; ++i)
            tmp[i] = least;

        memset(numc, 0, sizeof(numc));
        
        for(int i = 0; i<top; ++i)
            ++numc[tmp[i]];
            
        count2();
        
        return 1;
    }
        
    if(num == 0)
        return 0;
    
    c = 0;
    for(int i = least; i <= max; ++i)
    {
        /////////////////
        tmp[top-num] = i;
        /////////////////
        
        c += count(num-1, sum-i, i);
    }
    
    return c;
}


ll cal()
{
    init();
    ll r = count(top, total, 1);
    printf("%llu\n", r);
    printf("%llu\n", res);
    return res;
}

}


#endif