#include <bits/stdc++.h>
using namespace std;

bool removeElement(vector<int>&arr,int total)
{
    if(arr.size()==1) return true;
    if(*max_element(arr.begin(),arr.end())+*min_element(arr.begin(),arr.end())<=total) return true;
    return false;
}

int main()
{
	int N=4,K=7;
    cin>>N>>K;
    vector<int> A = {1,4,3,5};
    if(removeElement(A,K)) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
}
