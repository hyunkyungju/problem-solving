#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int p;
		scanf("%d", &p);
		int max_price = -1;
		string max_name = "";
		for (int j = 0; j < p; j++) {
			int price;
			string name;
			cin >> price >> name;
			if (max_price < price) {
				max_price = price;
				max_name = name;
			}
		}
		cout << max_name << endl;
	}
	return 0;
}