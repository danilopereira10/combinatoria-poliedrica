//#include <stdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <stack>
#include <tuple>
#include <cstring>
#include <cstdlib>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
stack<tuple<int, int, int>> num;
stack<tuple<int, int, int>> num2;
vi dif;
typedef long long ll;
int main() {
    while (true) {
        string s;
        if (cin.eof()) {
            break;
        } else 
            cin >> s;
        long long int a, b;
        cin >> a;
        if (cin.eof())
        break;
        cin >> b;
        // YOUR SOLUTION HERE
    }
  return 0;
    string s;
    cin >> s;
    vi a;
    vi b;
    double n;
    for (int i = 0; i < s.size(); i++) {

    }
    while (s != "0") {
        cin >> s;
    }
    for (int i = 0; i < s; i++) {
        string b;
        cin >> b;
        int sum = 0;
        if (b[0] == '0') {
            sum+= 10;
        } else {
            sum += b[0] - '1' + 1;
        }
        for (int j = 1; j < 4; j++) {
            if (b[j] == b[j-1] && b[j] == '0') {
                sum += 1;
            } else if (b[j] == '0') {
                sum += '9'+1 - b[j-1] + 1;
            } else if (b[j-1] == '0') {
                sum += abs(b[j] - ('9' + 1)) + 1;

            } else {
                sum += abs(b[j] - b[j-1]) + 1;
            }
        }
        cout << sum << endl;
    }

}