#ifndef __PB0089_H__
#define __PB0089_H__

#include <string.h>
#include <iostream>
#include <assert.h>
#include <stdio.h>

namespace PB0089
{

void cal()
{
    FILE* fp = fopen("pb0089_roman.txt", "r");
    if(!fp)
    {
        fprintf(stderr, "open failed\n");
        return;
    }
    
    const char* pattern[] = {"DCCCC","LXXXX","VIIII",
                             "CCCC","XXXX","IIII"};
    
    char line[200];
    int c = 0;
    while(fgets(line, 200, fp))
    {
        int len = strlen(line)-1;
        if(line[len]=='\n')
             line[len] = '\0';
        
        int i = 0;
        
        int ll = len;
        while(i<len)
        {
            for(unsigned int j = 0; j < 6; ++j)
            {
                int len2 = strlen(pattern[j]);
                if(0 == strncmp(line+i, pattern[j], len2))
                {
                    i += len2 - 1;
                    ll -= len2 - 2;
                    break;
                }
            }
            ++i;
        }
        c += len - ll;
    }
    
    fclose(fp);
    
    printf("%d\n", c);
}

}


#endif