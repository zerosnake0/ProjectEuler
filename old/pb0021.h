#ifndef __PB0021_H__
#define __PB0021_H__

namespace PB0021
{

const int max = 10000;

int n[max+1];

int d(int b)
{
    int res = 0, i = 1;
    for(; i * i < b; ++i)
    {
        if(b%i == 0)
            res += i + b/i;
    }
    if(i*i==b)
        res += i;
    return res - b;
}

int cal()
{
    int count = 0;
    memset(n, 0, sizeof(n));
    
    for(int i = 1; i <= max; i++)
    {
        if(n[i] != 0)
            continue;
            
        n[i] = d(i);
        
        if(n[i]>i)
        {
            int tmp = d(n[i]);
            if(tmp == i)
            {
                n[n[i]] = tmp;
                count += i + n[i];
            }
        }
    }
    
    return count;
}

}


#endif