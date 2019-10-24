#include <stdio.h>
#include <string.h>

#define MAX 32

typedef struct _binary
{
    unsigned int bit[MAX];
}binary;

int bZero(const binary* b)
{
    int i;
    for(i = 0; i < MAX; ++i)
        if(b->bit[i])
            return 0;
    return 1;
}

void decr(binary* b)
{
    int i;
    for(i = 0; i < MAX; ++i)
    {
        --(b->bit[i]);
        if(b->bit[i] != (unsigned int)(-1))
            return;
    }
}

void print(const binary* b)
{
    int i, bp = 0;
    for(i = MAX - 1; i >= 0; --i)
    {
        if(b->bit[i] && !bp)
            bp = 1;
        if(bp)
            printf("%x ", b->bit[i]);
    }
    putchar('\n');
}

unsigned int n1(unsigned int a)
{
    int count = 0;
    while(a)
    {
        if(a & 0x1)
            ++count;
        a >>= 1;
    }
    return count;
}

unsigned int num1(const binary* b)
{
    int i, count = 0;
    for(i = 0; i < MAX; ++i)
        count += n1(b->bit[i]);
    
    return count;
}

binary m(int n)
{
    int i;
    binary b;
    
    memset(&b, 0, sizeof(b));
    
    for(i = 0; i < (n+1)/32; ++i)
        b.bit[i] = (unsigned int)(-1);
    
    b.bit[i] = (1<<((n+1)%32)) - 1;
    --b.bit[0];
    
    for(;;)
    {
        binary b2 = b;
        
        int count = 0, count2 = num1(&b);
        
        while(count2 <= n)
        {
            decr(&b);
            if(bZero(&b))
                return b2;
                
            count = count2;
            count2 += num1(&b);
        }
        decr(&b);
        if(bZero(&b))
            return b;
    }
    
    return b;
}

int s(binary b)
{
    int count = 0;
    while(!bZero(&b))
    {
        count += num1(&b);
        decr(&b);
    }
    return count;
}

int main(void)
{
    binary b;
    
    int res,i,count = 0;
    
    for(i=32; i<=1000; ++i)
    {
        b = m(i);
        printf("%d:",i);
        res = s(b);
        printf("%d\n", res);
        count += res * res * res;
    }
    printf("total:%d\n",count);
    return 0;
}