#include <stdio.h>
#include <string.h>

#define MAX_STR_LEN 1024
#define MAX_ELEMENTS 100
#define MAX_SUBSTR_LEN 100

int main() {
    char input[MAX_STR_LEN];
    char elements[MAX_ELEMENTS][MAX_SUBSTR_LEN];
    int element_count = 0;

    // 1. Ask user to input a string
    printf("Enter a string with '$' as a splitter: ");
    if (fgets(input, sizeof(input), stdin) == NULL) {
        printf("Error reading input.\n");
        return 1;
    }

    // Remove trailing newline character from fgets if it exists
    input[strcspn(input, "\n")] = '\0';

    // 2 & 3. Split the string using strtok (handles any placement of '$')
    char *token = strtok(input, "$");
    
    while (token != NULL && element_count < MAX_ELEMENTS) {
        // Copy the substring into our array
        strncpy(elements[element_count], token, MAX_SUBSTR_LEN - 1);
        elements[element_count][MAX_SUBSTR_LEN - 1] = '\0'; // Ensure null-termination
        element_count++;
        
        // Get the next token
        token = strtok(NULL, "$");
    }

    // Print the resulting array elements
    printf("\nExtracted elements stored in the array:\n");
    for (int i = 0; i < element_count; i++) {
        printf("Array[%d]: %s\n", i, elements[i]);
    }
  //return back
    return 0;
}
