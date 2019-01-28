#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<conio.h>
#include<string.h>

int main() {
	char wzor[20];
	char tekst[100];
    printf("Podaj slowo do znalezienia: \n");
    gets(wzor);
    printf("Podaj tekst w ktorym bedziemy wyszukiwac wzorca \n");
    gets(tekst);
    for(int i = 0; i < strlen(tekst); i++){
        int j = 0;
        for(int a = 0; a < strlen(wzor); a++){
            if(tekst[i+j] == wzor[j])
                j++;
            else
                break;
        }
        if(j == strlen(wzor)){
            j--;
            printf("Znalazlem wzor na indeksie %d \n", i);
        }
        i = i + j;
    }
    _getch();
    return 0;
}
