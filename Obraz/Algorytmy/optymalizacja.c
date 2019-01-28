#include <conio.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

struct kukulka{
    float x, y;
};

float funkcja(struct kukulka k){
    return (k.x*k.x)*k.x+(k.y)*(k.y)*k.y;
}

float float_rand(float min, float max){
    float sc = rand() / (float) RAND_MAX;
    return min + sc * (max-min);
}



int main(){
    float px = 5;
    float py = 5;
    struct kukulka kukulka[100];
    for(int i = 0; i < 100; i++){
        struct kukulka knowa;
        knowa.x = float_rand(-px, px);
        knowa.y = float_rand(-py, py);
    }

    int generacje = 10;
    for(int i = 0; i < generacje; i++){
            for(int k = 0; k < 100; k++){
                float decyzja = float_rand(0, 1);
                if(decyzja < 0.5){
                    //ruch kukulki
                    float parametr = 0.3;
                    kukulka[k].x += (1/sqrt(4*3.14*parametr)*(pow(2.72, (-kukulka[k].x*kukulka[k].x)/(4*parametr))));
                    kukulka[k].y += (1/sqrt(4*3.14*parametr)*(pow(2.72, (-kukulka[k].y*kukulka[k].y)/(4*parametr))));
                }else{
                    struct kukulka nowa;
                    nowa.x = float_rand(-px, px);
                    nowa.y = float_rand(-py, py);
                    if(funkcja(nowa) < funkcja(kukulka[k])){
                        kukulka[k] = nowa;
                    }
                }
            }
    }

    struct kukulka rozwiazanie = kukulka[0];
    for(int i = 1; i < 100; i++){
        if(funkcja(rozwiazanie) > funkcja(kukulka[i])){
            rozwiazanie = kukulka[i];
        }
    }

    printf("Znaleziono najmniejsza wartosc w punkcie (%f, %f) o wartosci %f", rozwiazanie.x, rozwiazanie.y, funkcja(rozwiazanie));


}
