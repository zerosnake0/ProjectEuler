#ifndef __PB0081_H__
#define __PB0081_H__

#include <stdio.h>
#include <assert.h>
#include <iostream>
#include <string>

namespace PB0081
{

const int max = 80;

int mat[max][max];

void cal()
{
    FILE* fp = fopen("pb0081_matrix.txt","r");
    if(!fp)
    {
        printf("open failed\n");
        return;
    }
    
    for(int i = 0; i < max; ++i)
        for(int j = 0; j < max; ++j)
        {
            fscanf(fp, "%d", &mat[i][j]);
            fgetc(fp);
        }
    
    fclose(fp);
    
    for(int i = max - 2; i >= 0; --i)
    {
        mat[max-1][i] += mat[max-1][i+1];
        mat[i][max-1] += mat[i+1][max-1];
    }
    
    for(int i = max - 2; i >= 0; --i)
        for(int j = max - 2; j >= 0; --j)
            mat[i][j] += ((mat[i][j+1] < mat[i+1][j])? mat[i][j+1] : mat[i+1][j]);
    
    printf("%d\n",mat[0][0]);
}

}

#endif