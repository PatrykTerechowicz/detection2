#include <conio.h>
#include <stdio.h>

struct stack{
    int l[100];
    int top;
};
struct stack st;
void push(int num){
    if(st.top >= 100){
        printf("Stos jest pelny");
        return;
    }
    st.l[st.top] = num;
    st.top++;
}

int pop(){
    if(st.top <= 0){
        printf("Stos jest pusty");
        return;
    }
    st.top--;
    return st.l[st.top];
}

void display(){
    while(st.top > 0){
        int num = pop(st);
        printf("st[%d] = %d \n", st.top, num);

    }
}

int main(){
    st.top = 0;
    for(int i = 0; i < 100; i++){
        push(100-i);
    }

    display();
    return 0;
}
