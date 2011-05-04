/*************************************************************************
 Author: Junjie Bian
 Created Time: 2010年11月20日 星期六 21时43分04秒
 File Name: pro31.cpp
 Description: 
 ************************************************************************/
#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int S[201][8]={0};
int money[8]={1,2,5,10,20,50,100,200};

void init()
{
   int i,j;
   for (i=1;i<=200;i++)
       S[i][0]=1;

}

int cal(int m,int n)
{
    if (S[m][n]!=0)
	return S[m][n];

    int k=m/money[n];
    int i;
    for (i=0;i<=k;i++)
    {
	int remain=m-i*money[n];
	if (remain==0)
	    S[m][n]+=1;
	else
	    S[m][n]+=cal(remain,n-1);
    }
    return S[m][n];
}
int main()
{

//    memset(S,-1,sizeof(S));
    init();
    cal(200,7);
    cout<<S[200][7]<<endl;
}
