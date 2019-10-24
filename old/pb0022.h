#ifndef __PB0022_H__
#define __PB0022_H__

#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

namespace PB0022
{

typedef unsigned long long int ll;

using namespace std;

vector<string> g_vec;

bool init()
{
    FILE* fp = fopen("pb0022_names.txt", "r");
    if(!fp)
        return false;
    
    do
    {
        fgetc(fp);
        string s;
        char c;
        while((c=fgetc(fp))!='"')
            s += c;
        g_vec.push_back(s);
    } while(fgetc(fp)==',');
    
    
    sort(g_vec.begin(), g_vec.end());
    
    fclose(fp);
    return true;
}

ll score(const string& str)
{
    ll c = 0;
    const char* p = str.c_str();
    for(; *p != '\0'; ++p)
        c += *p - 'A' + 1;
    
    return c;
}

ll cal()
{
    if(!init())
        return -1;

    size_t tt = g_vec.size();
    ll c = 0;
    
    for(unsigned int i = 0; i < tt; ++i)
    {
        c += score(g_vec[i]) * (i + 1);
    }
    
    return c;
}

}


#endif