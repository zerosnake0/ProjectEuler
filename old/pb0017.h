#ifndef __PB0017_H__
#define __PB0017_H__

namespace PB0017
{

unsigned int cal(void)
{
    unsigned int res = 0;
    
    // 1 ~ 9
    unsigned int one2nine = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4;
    res = one2nine;
         
    // 1 ~ 9 , 20 ~ 99
    res *= 9;
    res += 10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6);
    
    // 10 ~ 19
    res += 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8;
    
    // 1 ~ 999
    res *= 10;
    res += (one2nine + 9 * 7) * 100 + 3 * 9 * 99;
    
    // 1000
    res += 3 + 8;
    
    return res;
}
    

}


#endif