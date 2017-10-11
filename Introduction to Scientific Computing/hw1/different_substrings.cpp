#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;
 
typedef unsigned int ui;
 
ui z_function (string s) {
	ui n = (ui) s.length();
	vector<ui> z (n);
	for (ui i=1, l=0, r=0; i<n; ++i) {
		if (i <= r)
			z[i] = min (r-i+1, z[i-l]);
		while (i+z[i] < n && s[z[i]] == s[i+z[i]])
			++z[i];
		if (i+z[i]-1 > r)
			l = i,  r = i+z[i]-1;
	}
    return *std::max_element(z.begin(), z.end());
}
 
ui process_experiment(string s) {
    ui answer = 0;
    for(auto i = 0; i < s.length(); ++i) {
        auto substr = s.substr(0, i+1);
        reverse(substr.begin(), substr.end());
        auto maxz = z_function(substr);
        answer += (i + 1) - maxz; 
    }
    return answer;
}
 
int main(int argc, char** argv) {
    ui num_experiments;
    cin >> num_experiments;
 
    string s;
 
    for(ui i = 0; i < num_experiments; ++i) {
        cin >> s;
        cout << process_experiment(s) << std::endl;
    }
 
 
    return 0;
}
