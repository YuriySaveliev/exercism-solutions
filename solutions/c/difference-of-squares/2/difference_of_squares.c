#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int n) {
    unsigned int sum_squares = 0;
    
    for (unsigned int i = 1; i <= n; i++ ) {
        sum_squares += i * i;
    }

    return sum_squares;
}

unsigned int square_of_sum(unsigned int n) {
    unsigned int sum = 0;

    for (unsigned int i = 1; i <= n; i++ ) {
        sum += i;
    }
   
    return sum * sum;
}

unsigned int difference_of_squares(unsigned int n) {
    return square_of_sum(n) - sum_of_squares(n);
}
