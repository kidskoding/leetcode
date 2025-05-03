#include "main.hpp"
#include <iostream>

int main(int argc, char** argv) {
    std::string s = "abcdefg";
    std::string result = reverseStr(s, 2);
    std::cout << result << "\n";
}
