// fibonacci sequence

/* === compile command === */
// g++ fibonacci.cpp -o run
/* === debug compile command === */
// g++ -std=c++17 -Wall -Wextra -pedantic -Weffc++ fibonacci.cpp -o run
/* === execute command === */
// .\run

#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

// f(n) = f(n-1) + f(n-2)

void get_fib(vector<int>& fib, const int& num) {
    for (int i=2; i<num; i++) {
        int next = fib[i-1] + fib[i-2];
        fib.push_back(next);
    }
}

int main() {
	int fiblen = 10;
    vector<int> fib = {1, 1};
    get_fib(fib, fiblen);
    for (int i=0; i<fiblen; i++) {
        cout << fib[i] << ' ';
    }
    cout << endl;
}
