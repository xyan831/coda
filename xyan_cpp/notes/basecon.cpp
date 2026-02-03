// base conversion

/* === compile command === */
// g++ basecon.cpp -o run
/* === debug compile command === */
// g++ -std=c++17 -Wall -Wextra -pedantic -Weffc++ basecon.cpp -o run
/* === execute command === */
// .\run

#include <iostream>
#include <vector>
#include <algorithm>

//using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::reverse;

void dec_convert(int n, const int& r, vector<char>& convert) {
	int temp, len;
	char digit;
	cout << "Decimal " << n << " convert to base " << r << endl;
	cout << "ans = ";
	while (n!=0) {
		temp = n%r;
		n = n/r;
		// convert integer into character
		if (temp<10) digit = temp + '0';
		else digit = temp-10 + 'A';
		convert.push_back(digit);
	}
	len = convert.size();
	reverse(convert.begin(), convert.end());
	for (int i=0; i<len; i++) {
		cout << convert[i];
	}
	cout << endl;
}

int main(void) {
	int n=648;
	vector<char> c1, c2, c3;
	
	dec_convert(n, 2, c1);
	dec_convert(n, 8, c2);
	dec_convert(n, 16, c3);

	return 0;
}

