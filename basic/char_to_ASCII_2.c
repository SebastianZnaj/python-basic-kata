// To run C program in bash
// 1. name C script with ending .c
// 2. run command: gcc -o char_to_ASCII_2 char_to_ASCII_2.c
// 3. run script: ./char_to_ASCII_2

// C program to print
// ASCII Value of Character
#include <stdio.h>
int main()
{
    char c = 'k';
    
    // %d displays the interger value of a character
    // %d displays the actual character
    printf("The ASCII value of %c is %d", c, c);
    return 0;
}
