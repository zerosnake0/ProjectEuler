#ifndef __PB0162_H__
#define __PB0162_H__

#include <stdio.h>

namespace PB0162
{

typedef long long int ll;

const int MAX = 16;

ll p2[MAX+1];
ll p3[MAX+1];
ll p13[MAX+1];
ll c[MAX+1][MAX+1];

void init()
{
    p2[0] = p3[0] = p13[0] = 1;
    for(int i = 1; i <= MAX; ++i)
    {
        p2[i] = p2[i-1] * 2;
        p3[i] = p3[i-1] * 3;
        p13[i] = p13[i-1] * 13;
    }
    
    c[0][0] = 1;
    for(int i = 1; i <= MAX; ++i)
    {
        c[i][0] = c[i][i] = 1;
        for(int j = 1; j < i; ++j)
            c[i][j] = c[i-1][j-1] + c[i-1][j];
    }
}

ll cal()
{
    init();
    
    ll count = 0;

    for(int i = 3; i <= MAX; ++i)
        count += p13[MAX-i]*c[MAX][i]*(p3[i]-(p2[i]-2)*3-3);
    
    
    for(int i = MAX-1; i >= 2; --i)
    {
        ll c2 = 0;

        for(int j = i; j >= 2; --j)
            c2 += p13[i-j] * c[i][j] * (p2[j]-2);

        count -= c2;
    }
    
    printf("%llx\n", count);
    return count;
}

}


#endif