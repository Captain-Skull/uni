#include <fstream>
#include <string>
#include <iostream>

using namespace std;

void task1() {
	ifstream input("input.txt");
	ofstream output("output.txt");

	string phrase = "useragreement";
	string text;

	getline(input, text);

	for (char c : text) {
		char low_c = tolower(c);

		if (phrase.find(c) == string::npos) {
			output << c;
		}
	}

	input.close();
	output.close();
}

void task2() {
	ifstream input1("input1.txt");
	ifstream input2("input2.txt");

	string x;
	string y;
	getline(input1, x);
	getline(input2, y);

	if (x.find(y) != string::npos) {
		cout << "yes";
	}
	else {
		cout << "no";
	}
}

string convertToBin(string numberStr) {
	int num = stoi(numberStr);
	string binaryNum = "";
	while (num > 0) {
		binaryNum += to_string(num % 2);
		num = num / 2;
	}

	reverse(binaryNum.begin(), binaryNum.end());
	cout << binaryNum << endl;

	return binaryNum;
}

void task3() {
	ifstream inputNum("inputNum.txt");
	ofstream outputNum("outputNum.txt");

	string nums = "0123456789";
	string text;
	getline(inputNum, text);

	bool flag = false;
	string num = "";

	for (char c : text) {
		if (nums.find(c) != string::npos) {
			num += c;
			flag = true;
		}
		else if (flag) {
			string binaryNum = convertToBin(num);
			outputNum << binaryNum;
			outputNum << c;
			flag = false;
			num = "";
		}
		else {
			outputNum << c;
		}
	}

	if (num != "") {
		string binaryNum = convertToBin(num);
		outputNum << binaryNum;
	}
}

int main() {
	task3();
}