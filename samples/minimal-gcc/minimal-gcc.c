#include<stdio.h>
#include <time.h>
#include <stdlib.h>

int random_func(){
    srand(time(NULL));
    return rand() % 2;
}

void print_foo(int i){
    printf("foo %d\n", i);
}

void print_bar(int i){
    printf("bar %d\n", i);
}

int main(){
    int i = random_func();
    if (i){
        print_foo(i);
    }else{
        print_bar(i);
    }
    return 0;
}
