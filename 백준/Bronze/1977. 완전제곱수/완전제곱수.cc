#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int m, n;
	cin >> m >> n;
	int m_s = ceil(sqrt(m));
	int n_s = sqrt(n);
	int ret = 0;
	for (int i = m_s; i <= n_s; i++) {
		ret += pow(i, 2);
	}
	if (ret == 0) {
		cout << -1 << endl;
		return 0;
	}
	cout << ret << endl;
	cout << pow(m_s, 2) << endl;
	return 0;
}