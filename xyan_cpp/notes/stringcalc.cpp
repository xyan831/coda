// string calculator

/* === compile command === */
// g++ stringcalc.cpp -o run
/* === debug compile command === */
// g++ -std=c++17 -Wall -Wextra -pedantic -Weffc++ stringcalc.cpp -o run
/* === execute command === */
// .\run

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::stringstream;
using std::string;
using std::vector;
using std::reverse;

string get_str() {
    string str;
    cout << "check text" << endl;
    getline (cin, str);
    return str;
}

vector<string> split_str(const string& str) {
    vector<string> words;
    stringstream ss(str); // Create a stringstream from the input string
    string word;
    // Use the >> operator to extract words separated by whitespace
    while (ss >> word) {
        words.push_back(word);
    }
    return words;
}

void process(const vector<string>& words, string& num1, string& num2, char& symb) {
    num1 = words[0];
    reverse(num1.begin(), num1.end());
    num2 = words[2];
    reverse(num2.begin(), num2.end());
    symb = words[1][0];
}

// functions for solve
char int2char(const int& num) {
    return num+'0';
}

int char2int(const char& ch) {
    if (ch==0) return 0;
    return ch-'0';
}

int func_add(const int& num1, const int& num2, int& temp) {
    int sol = num1+num2+temp;
    temp = sol/10;
    sol = sol%10;
    return sol;
}

int func_subtract(const int& num1, const int& num2, int& temp) {
    int sol = num1-num2-temp;
    if (sol<0) {
        sol = 10+num1-num2-temp;
        temp = 1;
    } else {
        temp = 0;
    }
    return sol;
}

string solve(string num1, string num2, const char& symb) {
    string solution, for_switch;
    int len, digit1, digit2, temp, sol_num;
    char sol_ch;
    bool is_switched;
    
    if ((num1.size()>num2.size()) || (num1.size()==num2.size() && num1>num2)) {
        len = num1.size();
        is_switched = false;
    } else {
        len = num2.size();
        for_switch = num1;
        num1 = num2;
        num2 = for_switch;
        is_switched = true;
    }
    temp = 0;
    for (int i=0; i<len; i++) {
        digit1 = char2int(num1[i]);
        digit2 = char2int(num2[i]);
        switch(symb) {
            case '+':
                sol_num = func_add(digit1, digit2, temp);
                break;
            case '-':
                sol_num = func_subtract(digit1, digit2, temp);
                break;
        }
        sol_ch = int2char(sol_num);
        solution += sol_ch;
        cout << digit1 << " " << symb << " " << digit2 << " = " << sol_num << " r " << temp << endl;
    }
    if (symb=='+' && temp!=0) solution += temp+'0';
    if (symb=='-' && is_switched) solution += '-';
    reverse(solution.begin(), solution.end());
    
    return solution;
}

int main() {
    char symb;
    string expression, num1, num2, solution;
    vector<string> parts;
    
    //expression = get_str();
    expression = "1235 - 9236";
    parts = split_str(expression);
    
    process(parts, num1, num2, symb);
    solution = solve(num1, num2, symb);
    
    cout << expression << " = " << solution << endl;
    return 0;
}

