#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_STATES 100
#define MAX_SYMBOLS 100

int main() {
    char data[1000];
    char white_space = ' ';
    char *ptr;
    int num_states, i, j;
    char delta[MAX_STATES][MAX_SYMBOLS], symbol[MAX_SYMBOLS], word[MAX_SYMBOLS], current_state[10], final_state[MAX_STATES][10];

    fgets(data, 1000, stdin); // 標準入力から読み込む
    sscanf(data, "%d %*s", &num_states);

    for (i = 0; i < num_states; i++) {
        fgets(data, 1000, stdin);
        ptr = strtok(data, &white_space);
        for (j = 0; j < strlen(data); j++) {
            if (*ptr == ' ') {
                ptr++;
            }
            delta[i][j] = *ptr;
            ptr++;
        }
    }

    fgets(symbol, MAX_SYMBOLS, stdin);
    fgets(word, MAX_SYMBOLS, stdin);
    fgets(data, MAX_STATES, stdin);
    sscanf(data, "%s", current_state);
    fgets(data, MAX_STATES, stdin);
    ptr = strtok(data, &white_space);
    i = 0;
    while (ptr != NULL) {
        strcpy(final_state[i], ptr);
        ptr = strtok(NULL, &white_space);
        i++;
    }

    for (i = 0; i < strlen(word) - 1; i++) {
        int index = strchr(symbol, word[i]) - symbol;
        char next_state = delta[atoi(current_state) - 1][index];
        current_state[0] = next_state;
    }

    for (i = 0; i < sizeof(final_state) / sizeof(final_state[0]); i++) {
        if (strcmp(current_state, final_state[i]) == 0) {
            printf("Yes\n");
            return 0;
        }
    }

    printf("No\n");
    return 0;
}