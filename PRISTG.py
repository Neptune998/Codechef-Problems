# include<bits/stdc++.h>
using
namespace
std;
int
isSubstring(string
s1, string
s2)
{
    int
M = s1.length();
int
N = s2.length();

/ *A
loop
to
slide
pat[]
one
by
one * /
for (int i = 0; i <= N - M; i++) {
    int j;

/ * For current index i, check for pattern match * /
for (j = 0; j < M; j++)
if (s2[i + j] != s1[j])
break;

if (j == M)
    return i;
}

return -1;
}
int
main()
{
string
a, b;
int
sum = 0;
cin >> a >> b;
int
n = a.length();
for (int i = 0; i < n; i++)
    for (int len = 1; len <= n - i; len++)
        {string
        s = a.substr(i, len);
        int
        x = isSubstring(s, b);
        if (x != -1)
        sum++;
        }
cout << sum << endl;

}