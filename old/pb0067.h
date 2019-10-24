#ifndef __PB0067_H__
#define __PB0067_H__

#include <stdio.h>

namespace PB0067
{

const int depth = 100;

int triangle[depth][depth];

bool init()
{
    FILE* fp = fopen("pb0067_triangle.txt","r");
    if(!fp)
        return false;
        
    for(int i = 0; i < depth; ++i)
        for(int j = 0; j <= i; ++j)
            fscanf(fp, "%d", &triangle[i][j]);
            
    fclose(fp);
    return true;
}

    int cal()
    {
        if(!init())
            return -1;
        for(int i = depth - 2; i >= 0; --i)
        {
            for(int j = 0; j <= i; ++j)
            {
                triangle[i][j] += triangle[i+1][j] > triangle[i+1][j+1] ?
                    triangle[i+1][j] : triangle[i+1][j+1];
            }
        }
        return triangle[0][0];
    }

}


#endif