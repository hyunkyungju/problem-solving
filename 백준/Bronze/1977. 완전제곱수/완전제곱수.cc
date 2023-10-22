#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <cmath>

using namespace std;

int main() {
	int m, n, ret = 0;
	scanf("%d %d", &m, &n);
	int m_s = ceil(sqrt(m));
	int n_s = sqrt(n);
	
	for (int i = m_s; i <= n_s; i++) {
		ret += pow(i, 2);
	}
	if (ret == 0) {
		printf("-1");
		return 0;
	}
	printf("%d\n%d", ret, int(pow(m_s, 2)));

	return 0;
}