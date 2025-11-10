#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <map>

using namespace std;

void mapPrinter(map<char, char> arr) {
    for (const auto& pair : arr) {
        cout << pair.first << " ";
    }
    cout << endl;
}

void task1() {
    vector<string> words = { "apple", "apache", "ear", "peach" };
    map<char, char> letters;

    for (char c : words[0]) {
        letters[c] = c;
    }

    for (int i = 1; i < words.size(); i++) {
        map<char, char> newLetters;
        for (const auto& pair : letters) {
            char c = pair.first;
            if (words[i].find(c) != string::npos) {
                newLetters[c] = c;
            }
        }
        letters = newLetters;
    }

    mapPrinter(letters);
}

void task2() {
	int n;
	cin >> n;
	unordered_map<string, vector<int>> book;

	for (int i = 0; i < n; i++) {
		string word;
		int page;
		cin >> word >> page;
		book[word].push_back(page);
	}

	map<int, map<string, string>> outputBook;

    for (const auto& pair : book) {
        string word = pair.first;
        vector<int> pages = pair.second;

        if (pages.size() != 1) {
            continue;
        }

        outputBook[pages[0]][word] = word;
    }

    for (const auto& pair : outputBook) {
        int page = pair.first;
        map<string, string> wordMap = pair.second;
        auto& firstWordPair = *wordMap.begin();
        string word = firstWordPair.first;

        cout << page << " " << word;
    }
}

int main() {
	task2();
}