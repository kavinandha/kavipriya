#include<iostream>
#include<string>
using namespace std;
void appendDemo(string str 1,string str2)
{
str1.append(str2);
cout<<"using append():";
cout<<str1<<end1;
}
int main()
{
  string str1("hello world!");
  string str2("geeksforgeeks");
  cout<<"original string:"<<str1<<end1;
  appendDemo(str1,str2);
  return 0;
  }
