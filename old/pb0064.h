#ifndef __PB0064_H__
#define __PB0064_H__

#include <stdio.h>
#include <assert.h>
#include <iostream>
#include <string>

namespace PB0064
{

struct frac
{
    int n;
    int l;
    
    int a;
    int b;
    int c;
    
    void go()
    {
        int tmp = n - b*b;
        if(tmp%c!=0)
        {
            printf("!!!");
            print();
            getchar();
        }
        c = tmp/c;
        a = (l-b) / c;
        b = - b - a * c;
    }
    
    void print()
    {
        printf("%d+(%d %d)/%d\n",a,n,b,c);
    }
    
    const frac& operator=(const frac& f)
    {
        n = f.n;
        l = f.l;
        a = f.a;
        b = f.b;
        c = f.c;
        return *this;
    }

    bool operator==(const frac& f)
    {
        return (n==f.n && a==f.a && b==f.b && c==f.c);
    }
    
    bool operator!=(const frac& f)
    {
        return (n!=f.n || a!=f.a || b!=f.b || c!=f.c);
    }
};

unsigned int p(unsigned int n)
{
    unsigned int l;
    for(l=1; l*l<n; ++l);

    if(l*l==n)
        return -1;
    
    --l;
    
    frac f0;
    
    f0.n = n;
    f0.l = l;
    f0.c = n - l*l;
    f0.a = l * 2 / f0.c;
    f0.b = l - f0.a * f0.c;
    
    frac ff = f0;
    
    unsigned r = 0;
    
    do
    {
        ff.go();
        ++r;
    } while (ff != f0);
    
    return r;
}

void cal()
{
    int r = 0;
    
    for(unsigned int i = 2; i <= 10000; ++i)
    {
        int j = p(i);
        if(j==-1)
        {
            continue;
        }
        
        if(j&0x1)
            ++r;
    }
    
    printf("%d\n",r);
}

}

#endif