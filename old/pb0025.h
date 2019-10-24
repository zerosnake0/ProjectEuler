#ifndef __PB0025_H__
#define __PB0025_H__

#include <string.h>
#include <iostream>
#include <assert.h>
#include <stdio.h>
#include <map>

namespace PB0025
{

class bignum
{
public:
    typedef unsigned int digit;
    static const unsigned int max = 1000;

    bignum()
    {
        memset(d,0,sizeof(d));
    }

    bignum(const unsigned int &i)
    {
        memset(d,0,sizeof(d));

        unsigned int j = i;
        unsigned int k = 0;

        while(j>0)
        {
            d[k] = j % 10;
            j /= 10;
            ++k;

            assert(k<max);
        }
    }

    bignum& operator=(const unsigned int &i)
    {
        memset(d,0,sizeof(d));

        unsigned int j = i;
        unsigned int k = 0;

        while(j>0)
        {
            d[k] = j % 10;
            j /= 10;
            ++k;

            assert(k<max);
        }

        return *this;
    }

    bignum& operator=(const bignum& i)
    {
        memcpy(d, i.d, sizeof(i.d));
        return *this;
    }

    bignum& operator+=(const unsigned int &i)
    {
        bignum n(i);
        *this += n;
        return *this;
    }

    bignum& operator+=(const bignum& i)
    {
        digit c = 0;

        for(unsigned int k = 0; k < max; ++k)
        {
            d[k] += c + i.d[k];
            c = d[k] / 10;
            d[k] -= c * 10;
        }
        assert(c == 0);

        return *this;
    }

    bignum& operator*=(const unsigned int& i)
    {
        digit c = 0;

        for(unsigned int k = 0; k < max; ++k)
        {
            d[k] = d[k]*i + c;
            c = d[k] / 10;
            d[k] -= c * 10;
        }

        assert(c == 0);

        return *this;
    }

    void swap(bignum& i)
    {
        digit t[max];
        memcpy(t, d, sizeof(d));
        memcpy(d, i.d, sizeof(i.d));
        memcpy(i.d, t, sizeof(t));
    }

    void print()
    {
        int b = 0;
        for(int k = max-1; k >= 0; --k)
        {
            if(d[k] != 0)
                b = 1;
            if(b)
                putchar('0' + d[k]);
        }
        putchar('\n');
    }

    digit d[max];
};

void cal()
{
    bignum a(1), b(1), c;
    unsigned int i = 2;
    for(;;)
    {
        c = a;
        a += b;
        b = c;
        ++i;
        
        if(a.d[999] != 0)
        {
            printf("%u ", i);
            a.print();
            break;
        }
    }
}

}

#endif