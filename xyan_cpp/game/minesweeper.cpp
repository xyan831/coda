// minesweeper

/* === compile command === */
// g++ minesweeper.cpp -o run
/* === debug compile command === */
// g++ -std=c++17 -Wall -Wextra -pedantic -Weffc++ minesweeper.cpp -o run
/* === execute command === */
// .\run

#include <iostream>
#include <limits>
//#include <string>
#include <vector>
#include <algorithm>
#include <random>

using std::cout;
using std::cin;
using std::endl;
//using std::getline;
//using std::string;
using std::vector;
using std::count;

// structure for matrix row col
struct matrix_dim {
    int numrows, numcols;
};

// function random integer between 2 int not include max
int rand_int(const int& min, const int& max) {
    int gen = rand() % (max-min) + min;
    return gen;
}

// function check valid
bool check_valid(const matrix_dim& md, const int& row, const int& col) {
    return (row>=0 && row<md.numrows && col>=0 && col<md.numcols);
}

// function print matrix
void print_mat(const matrix_dim& md, const vector<vector<char>>& mat) {
    for (int i=0; i<md.numrows; i++) {
        for (int j=0; j<md.numcols; j++) {
            cout << mat[i][j] << ' ';
        }
        cout << endl;
    }
}

// check matrix neighbor values
char check_neighbor(const matrix_dim& md, const vector<vector<char>>& mat, const int& row, const int& col) {
    // Offsets for all eight neighbors: (up, down, left, right, top-left, top-right, bottom-left, bottom-right)
    int dr[] = {-1, 1, 0, 0, -1, -1, 1, 1};
    int dc[] = {0, 0, -1, 1, -1, 1, -1, 1};
    // check neighbors
    vector<char> neighbor_vals;
    for (int i = 0; i < 8; i++) {
        int newrow = row + dr[i];
        int newcol = col + dc[i];
        // Ensure the neighbor is within bounds and not the original cell itself (implicitly handled by offsets here)
        bool is_valid = check_valid(md, newrow, newcol);
        if (is_valid) {
            neighbor_vals.push_back(mat[newrow][newcol]);
        }
    }
    int neighbor_bomb = count(neighbor_vals.begin(), neighbor_vals.end(), '*');
    return neighbor_bomb+'0';
}

// function initialize solution matrix
void init_sol_mat(const int& bomb_num, const matrix_dim& md, vector<vector<char>>& mat) {
    for (int i=0; i<bomb_num; i++) {
        int row = rand_int(0, md.numrows);
        int col = rand_int(0, md.numcols);
        if (mat[row][col]=='*') i--;
        mat[row][col] = '*';
    }
    for (int i=0; i<md.numrows; i++) {
        for (int j=0; j<md.numcols; j++) {
            if (mat[i][j]=='*') continue;
            else {
                mat[i][j] = check_neighbor(md, mat, i, j);
            }
        }
    }
}

void add_checkpos(const matrix_dim& md, vector<int>& checkx, vector<int>& checky, const int& row, const int& col) {
    int dr[] = {-1, 1, 0, 0, -1, -1, 1, 1};
    int dc[] = {0, 0, -1, 1, -1, 1, -1, 1};
    for (int i = 0; i < 8; i++) {
        int newx = row + dr[i];
        int newy = col + dc[i];
        // Ensure the neighbor is within bounds and not the original cell itself (implicitly handled by offsets here)
        bool is_valid = check_valid(md, newx, newy);
        if (is_valid) {
            checkx.push_back(newx);
            checky.push_back(newy);
        }
    }
}

// function open neighbor value until edge all not 0
void open_neighbor(const matrix_dim& md, const vector<vector<char>>& sol_mat, vector<vector<char>>& play_mat, const int& row0, const int& col0) {
    vector<int> checkx, checky;
    add_checkpos(md, checkx, checky, row0, col0);
    do {
        int row = checkx.back();
        int col = checky.back();
        checkx.pop_back();
        checky.pop_back();
        if (play_mat[row][col]=='_' || play_mat[row][col]=='F') {
            play_mat[row][col] = sol_mat[row][col];
            if (sol_mat[row][col]=='0') add_checkpos(md, checkx, checky, row, col);
        }
    } while (!checkx.empty());
}

bool check_win(const matrix_dim& md, const vector<vector<char>>& sol_mat, const vector<vector<char>>& play_mat) {
    for (int i=0; i<md.numrows; i++) {
        for (int j=0; j<md.numcols; j++) {
            if (sol_mat[i][j]!='*') {
                if (sol_mat[i][j]!=play_mat[i][j]) return false;
            }
        }
    }
    cout << "you win yay" << endl;
    return true;
}

// function play minesweeper ui
void play_game(const matrix_dim& md, const vector<vector<char>>& sol_mat, vector<vector<char>>& play_mat) {
    bool game_end = false;
    int row, col;
    char action;
    print_mat(md, play_mat);
    do {
        cout << "input: row(1-8) col(1-8) action(m=mine/f=flag)" << endl;
        cin >> row >> col >> action;
        // ignore extra inputs until newline
        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        row--;
        col--;
        bool is_valid = check_valid(md, row, col);
        if (is_valid) {
            if (action=='f') {
                if (play_mat[row][col]=='_') play_mat[row][col] = 'F';
                else if (play_mat[row][col]=='F') play_mat[row][col] = '_';
                else {
                    cout << "pos cant be flagged, try again" << endl;
                    continue;
                }
            } else if (action=='m') {
                if (play_mat[row][col]=='_' || play_mat[row][col]=='F') {
                    play_mat[row][col] = sol_mat[row][col];
                    if (sol_mat[row][col]=='*') {
                        cout << "touch bomb oh no" << endl;
                        game_end = true;
                        continue;
                    } else if (sol_mat[row][col]=='0') {
                        open_neighbor(md, sol_mat, play_mat, row, col);
                    }
                } else {
                    cout << "pos cant be mined, try again" << endl;
                    continue;
                }
            } else {
                cout << "invalid action, try again" << endl;
                continue;
            }
        } else {
            cout << "invalid row/col, try again";
            continue;
        }
        print_mat(md, play_mat);
        game_end = check_win(md, sol_mat, play_mat);
    } while (!game_end);
    cout << "end game" << endl;
}

int main() {
    matrix_dim md;
    char play;
    
    md.numrows = 8;
    md.numcols = 8;
    int bomb_num = 10;
    cout << "play game? [y/n]" << endl;
    cin >> play;
    // ignore extra inputs until newline
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    while (play=='y') {
        vector<vector<char>> sol_mat(md.numrows, vector<char>(md.numcols, '_'));
        vector<vector<char>> play_mat(md.numrows, vector<char>(md.numcols, '_'));
        init_sol_mat(bomb_num, md, sol_mat);
        //print_mat(md, sol_mat);
        //print_mat(md, play_mat);
        play_game(md, sol_mat, play_mat);
        cout << "play again? [y/n]" << endl;
        cin >> play;
    }
    cout << "ok bye bye" << endl;
    return 0;
}

