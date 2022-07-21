Compiler from C to asm.
Supports basic math operations, ternary operator, do-while loop

Input data: InputProgram.txt
Output data: OutputProgram.asm

Input example:
1.
int main(){
    int i = 0;
    do {
        i = i ++;
        continue;
        i = i - ~3;
     }while (i<1000);
    return i;
}

2. 
int sum(int a, int b, int d, int e, int f) {
    return a + b + d + e + f;
}

int main(){
    return sum(1, 2, 3, 4, 5);
}
    

3.
int calculator(int a, int operation, int b){
    int result = -1;
    result = operation == 1 ? a & b : result;
    result = operation == 2 ? 10 : result;
    result = operation == 3 ? a ^ b : result;
    result = operation == 4 ? a / b : result;
    result = operation == 5 ? a % b : result;
    result = operation == 6 ? a * b : result;
    result = operation == 7 ? a + b : result;
    result = operation == 8 ? a - b : result;
    result = operation == 9 ? a == b : result;
    result = operation == 10 ? a != b : result;
    result = operation == 11 ? a < b : result;
    result = operation == 12 ? a <= b : result;
    result = operation == 13 ? a > b : result;
    result = operation == 14 ? a >= b : result;
    return result;
}

int main(){
    int a = 5;
    int operation = 0;
    int b = 5;
    return calculator (a, operation, b);
}

