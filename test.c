#include <stdio.h>

#define N 4

void decrypt(int code[], int k, int result[])
{
    for (int i = 0; i < N; i++)
    {
        int sum = 0;

        if (k == 0)
        {
            result[i] = 0;
        }
        else if (k > 0)
        {
            for (int j = 1; j <= k; j++)
            {
                sum += code[(i + j) % N]; // wrap forward
            }
            result[i] = sum;
        }
        else
        { // k < 0
            for (int j = 1; j <= -k; j++)
            {
                sum += code[(i - j + N) % N]; // wrap backward
            }
            result[i] = sum;
        }
    }
}

int main()
{
    int code[N] = {2, 4, 9, 3};
    int k = -2;
    int result[N];

    decrypt(code, k, result);

    printf("Decrypted code: ");
    for (int i = 0; i < N; i++)
    {
        printf("%d ", result[i]);
    }

    return 0;
}
