#include <stdio.h>

void comparar(void) {
  int vet1[10], vet2[10], cont=0, pont=0;

  //Le o vetor 1
  printf("Sequencia 1:\n");
  for (int i=0; i<10; i++){
    printf("Digite o %iº termo: ", i+1);
    scanf("%i",&vet1[i]);
  }

  //Le o vetor 2
  printf("Sequencia 2:\n");
  for (int i=0; i<10; i++){
    printf("Digite o %iº termo: ", i+1);
    scanf("%i",&vet2[i]);
  }

    //compara os vetores
  for (int i=0; i<10; i++){
    cont += 1;
    if (vet1[i] != vet2[i]){
      pont+=1;
      break;
    }
  }

  //mede as comparações e da o resultado
  if (pont == 0){
    printf("As sequencias são iguais!\n");
  } else {
    printf("As sequencias não são iguais\n");
  }
  
  printf("Foram feitas %i comparações\n", cont);
}

void rec_PA (void) {
  int vetor[10], r[10], cont=0;

  //Le o vetor
  printf("Digite a sequencia:\n");
  for (int i=0; i<10; i++){
    printf("Digite o %iº termo: ", i+1);
    scanf("%i",&vetor[i]);
  }

  //tira a razão
  for (int i=0; i<10; i++){
    if (i >= 1) {
      r[i] = vetor[i] - vetor[i-1];
    }
  }

  //verifica se é uma PA
  for (int i=0; i<10; i++){
    if (i >= 2) {
      if (r[i] != r[i-1]){
        cont++;
      }
    }
  }

  //Mostra a classificação
  if (cont > 0){
    printf("\nNão é uma PA!\n");
  } else if (r[5] > 0) {
    printf ("\nÉ uma PA crescente\n");
  } else if (r[5] < 0) {
    printf ("\nÉ uma PA decrescente\n");
  } else if (r[5] == 0) {
    printf ("\nÉ uma PA constante\n");
  }
}


int main(void) {
  int op;
  
  printf("Escolha uma opção: \n");
  printf("[1] - Comparar 2 Vetroes\n");
  printf("[2] - Reconhecer PA\n");
  printf("-> ");
  scanf("%i", &op);

  switch (op) {
    case 1: comparar(); break;
    case 2: rec_PA(); break;
  }
  return 0;
}