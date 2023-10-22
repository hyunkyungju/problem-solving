#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int p;
		scanf("%d", &p);
		int max_price = -1;
		char max_name[21];
		for (int j = 0; j < p; j++) {
			int price;
			char name[21];
			scanf("%d %s", &price, &name);
			if (max_price < price) {
				max_price = price;
				strcpy(max_name, name);
			}
		}
		printf("%s\n", max_name);
	}
}