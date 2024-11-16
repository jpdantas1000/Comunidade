#include <stdio.h>
#include <math.h>

void main(){
    char nome[15]; 
    int idade;
    printf("Digite seu nome:\n");
    scanf("%s", &nome);
    printf("Digite sua idade:\n");
    scanf("%d", &idade);

    printf("Olá %s sua idade é %d",nome,idade);
}