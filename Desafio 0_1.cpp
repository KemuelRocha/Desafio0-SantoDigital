#include<bits/stdc++.h> 

using namespace std;

int main(){
	int N;
	cin >> N;
	vector <int> A;
	
	for(int i=0; i<N; i++){
		int aux;
		cin >> aux;
		A.push_back(aux);
	}
	
	for(int i=0; i<N; i+=2){
		if(i == 0){
			cout << A[i];
		}else{
			cout << " " << A[i];
		}
	}
	return 0;
}
