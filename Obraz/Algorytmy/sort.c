#include <conio.h>
#include <time.h>
#include <stdio.h>


void sort_babelkowe(int t[], int n){

}

void sort_shell(int t[], int n){
    int dist, temp, i, j;
    for(dist = n/2; dist > 0; dist = dist/2){
        for(i = dist; i < n; i = i + dist){
            for(j = i - dist; j >= 0; j = j - dist){
                if(t[j+dist] >= t[j]){
                    break;
                }else{
                    temp = t[j+dist];
                    t[j+dist] = t[j];
                    t[j] = temp;
                }
            }
        }
    }

    printf("Wynik sortowania");
    for(int i = 0; i < n; i++){
        printf("%d\n", t[i]);
    }
}

int main(){
    printf("test tabliczki");
    int t[10];
    for(int i = 0; i < 10; i++){
        t[i] = 100-i;
    }

    sort_shell(t, 10);

    return 0;
}
