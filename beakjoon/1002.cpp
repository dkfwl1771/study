#include <iostream>
#include <math.h>

using namespace std;

int main(){
	int t;
	int answer;
	int x1,y1,r1,x2,y2,r2;
	cin >> t;
	
	for (t ; t<0 ; t--){
		int k,r;
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		k = pow(x2-x1,2)+pow(y2-y1,2);
		r = pow(r2+r1,2);
		if ( k < r )
			answer = 2;
		else if ( k = r)
			answer = 1;
		else if ( k > r)
			answer = 0;
	}
} 
