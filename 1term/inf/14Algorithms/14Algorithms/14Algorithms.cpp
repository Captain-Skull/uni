#include <iostream>
#include <vector>

using namespace std;

template <typename T>
void vectorPrinter(vector<T> arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
}

template <typename T>
vector<T> Duplicate(std::vector<T>& v) {
    vector<T> newV;

    for (auto it = v.begin(); it != v.end(); ++it) {
        newV.push_back(*it);
    }

    for (auto it = v.begin(); it != v.end(); ++it) {
        newV.push_back(*it);
    }

    return newV;
}

int main()
{
    vector<int> firstV = { 1, 2, 4 };
    firstV = Duplicate(firstV);

    vectorPrinter(firstV);
}