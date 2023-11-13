#include <stdlib.h>
struct studentData {
  char name[50];
  int age;
  } student;
int main() {
  int n, i, num;
  FILE *filepointer;
  filepointer =   fopen("C:\\student.txt", "wb");
  if(filepointer == NULL) {
    printf("Error opening file\n");
    exit(1);
  }
  printf("Enter the number of records you want to enter: ");
  scanf("%d", &n);
  for(i = 0; i < n; i++) {
    printf("\nEnter details of employee %d \n", i + 1);
    fflush(stdin);
    printf("Name: ");
    gets(student.name);
    printf("Age: ");
    scanf("%d", &student.age);
    num = fwrite(&student, sizeof(student), 1, filepointer);
    printf("Number of items written to the file: %d\n", num);
  }
  fclose(filepointer);
  return 0;
}