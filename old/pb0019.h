#ifndef __PB0019_H__
#define __PB0019_H__

namespace PB0019
{

bool bLeep(int year)
{
    if(year % 4 != 0)
        return false;
    if(year % 100 == 0 && year % 400 != 0)
        return false;
    return true;
}

int nd(int m, int y)
{
    switch(m)
    {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            return 31;
        case 4:
        case 6:
        case 9:
        case 11:
            return 30;
        case 2:
            if(bLeep(y))
                return 29;
            else
                return 28;
    }
    return -1;
}

int cal()
{
    int d = (1 + 365) % 7;
    int count = 0;
    
    for(int y = 1901; y <= 2000; ++y)
        for(int m = 1; m <=12 ; ++m)
        {
            if(d==0)
                ++count;
            d = (d + nd(m,y)) % 7;
        }

    return count;
}

}


#endif