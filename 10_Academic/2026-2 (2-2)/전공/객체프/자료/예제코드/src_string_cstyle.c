#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    // 1. Creating strings
    char s1[100] = "Hello";
    char s2[100] = "World";
    char s3[200] = "";             // empty string

    // 2. Concatenation
    strcpy(s3, s1);
    strcat(s3, " ");
    strcat(s3, s2);
    printf("%s\n", s3);            // Hello World

    // 3. Length
    printf("Length: %zu\n", strlen(s3));

    // 4. Accessing individual characters
    printf("%c\n", s3[0]);         // H
    printf("%c\n", s3[1]);         // e

    // 5. Modifying a character
    s3[0] = 'h';
    printf("%s\n", s3);            // hello World

    // 6. Adding text
    strcat(s3, "!");
    strcat(s3, " C");
    printf("%s\n", s3);            // hello World! C

    // 7. Finding a substring
    char *pos = strstr(s3, "World");

    if (pos != NULL)
        printf("Found at index: %td\n", pos - s3);

    // 8. Extracting a substring
    char sub[6];
    strncpy(sub, s3 + 6, 5);
    sub[5] = '\0';
    printf("%s\n", sub);           // World

    // 9. Replacing part of a string
    // replacement is not supported in C 

    // 10. Inserting text
    // insertion is not supported in C

    // 11. Erasing part of a string
    // erase 6 characters starting at index 5
    // erase is not supported

    // 12. String comparison
    char a[] = "apple";
    char b[] = "banana";

    if (strcmp(a, b) < 0)
        printf("apple comes before banana\n");

    if (strcmp(a, "apple") == 0)
        printf("a is apple\n");

    // 13. Checking whether a string is empty
    if (strlen(s3) == 0)
        printf("String is empty\n");

    // 14. Iterating through characters
    for (size_t i = 0; i < strlen(s3); i++)
        printf("%c ", s3[i]);

    printf("\n");

    // 15. C-style string
    const char *p = s3;
    printf("%s\n", p);

    // 16. Numeric conversions
    char doubleStr[] = "123.45";
    char intStr[] = "67";

    double dval = atof(doubleStr);   // String to double
    int ival = (int)atoi(intStr); // String to int

    char formatted1[50];
    char formatted2[50];

    sprintf(formatted1, "%f", dval * 2);
    sprintf(formatted2, "%d", ival * 2);

    printf("conversion result: %s , %s\n",
           formatted1, formatted2);

    return 0;
}
