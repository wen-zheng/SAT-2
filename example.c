#include <stdio.h>

void func(int n){
	printf("%d\n",n);
}

int main(){
	int a;
	scanf("%d", &a);
	if(a>10){
		func(a);
		return 0;
	}
	else{
		func(a);
		return 0;
	}
}

