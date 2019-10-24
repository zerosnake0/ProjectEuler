#ifndef __PB0144_H__
#define __PB0144_H__

#include <stdio.h>
#include <math.h>

namespace PB0144
{

struct point
{
    long double x;
    long double y;
};

bool check(point* pt)
{
    if(pt->x < -0.01)
        return true;
    if(pt->x > 0.01)
        return true;
    if(pt->y < 0)
        return true;
    return false;
}

void cal()
{
    point p1 = {0.0, 10.1};
    point p2 = {1.4, -9.6};
    point p3;
    
    long double t1, t2, t3;
    
    unsigned int r = 0;
    
    do 
    {
        ++r;
        
        t1 = -4. * p2.x / p2.y;
        t1 = 2. * t1 / (1. - t1 * t1);
        
        t3 = (p2.y - p1.y) / (p2.x - p1.x);
        
        t2 = (t1 - t3) / (1. + t1*t3);
        
        long double a, b, c;
        a = 4 + t2 * t2;
        b = 2 * t2 * (p2.y - t2 * p2.x);
        c = p2.y - t2 * p2.x;
        c = c * c - 100;
        
        p3.x = - b/a - p2.x;
        p3.y = p2.y + t2 * (p3.x - p2.x);
        
        p1 = p2;
        p2 = p3;
    
    } while (check(&p2));
    
    printf("%u\n", r);
}

}


#endif