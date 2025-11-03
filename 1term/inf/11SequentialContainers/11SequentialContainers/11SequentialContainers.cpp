#include <iostream>
#include <random>
#include <array>
#include <list>
#include<string>
#include <windows.h>
#include <forward_list>

using namespace std;

int random_int(int min, int max) {
    static random_device rd;
    static mt19937 gen(rd());
    uniform_int_distribution<int> dist(min, max);
    return dist(gen);
}

void arrayPrinter(array<int, 10> arr) {
    cout << "Array: ";
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }

    cout << endl;
}

void listPrinter(list<string> arr) {
    cout << "Array: ";
    for (string s : arr) {
        cout << s << " ";
    }
    cout << endl;
}

void listPrinter(forward_list<int> arr) {
    cout << "Array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

void listPrinter(list<int> arr) {
    cout << "Array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

void task1() {
    array<int, 10> numsArr;
    int sum = 0;
    for (int i = 0; i < 10; i++) {
        numsArr[i] = random_int(1, 10);
        sum += numsArr[i];
    }

    arrayPrinter(numsArr);
    double middle = sum / static_cast<double>(10);
    cout << middle;
}

void task3() {
    list<string> students = { "Иванов", "Петров", "Сидоров", "Алексеев", "Борисов" };
    students.remove_if([](string& student) {return student[0] == 'А';  });
    students.sort([](const string& s1, const string& s2) { return s1 < s2; });

    listPrinter(students);
}

void task4() {
    forward_list<int> fwlist;
    auto it = fwlist.before_begin();
    it = fwlist.insert_after(it, 5);
    it = fwlist.insert_after(it, 4);
    it = fwlist.insert_after(it, 3);
    it = fwlist.insert_after(it, 2);
    it = fwlist.insert_after(it, 1);

    fwlist.reverse();

    listPrinter(fwlist);
}

void task5() {
    list<int> a = { 1, 3, 5, 7 };
    list<int> b = { 2, 3, 6, 7, 8 };
    a.merge(b);
    a.unique();
    a.remove_if([](int& x) { return x > 6;  });
    listPrinter(a);
}

int main() {
    setlocale(LC_ALL, "RU");
	task4();
}