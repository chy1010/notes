// build a function
#include <stdio.h>

int step_function(int x){
    int result = 0; // should claim variable

    if (x < 0) {
        result = -1;
    } else if (x > 0) {
        result = 1;
    } else {
        // result = 0; // nothing to change
    }
    return result;
}

int main(void){
    int val1 = step_function(3345678);
    int val2 = step_function(0);
    int val3 = step_function(-9527);

    printf("f(3345678)=%d; f(0)=%d; f(-9527)=%d.\n", val1, val2, val3);
}