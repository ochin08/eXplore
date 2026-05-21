



#include <iostream>
#define MY_CONSTANT 42

void greet() {
    std::cout << "Hello from greet()!" << std::endl;
}

#ifndef DEBUG_MODE
void debug_print() {
    // This function should be removed if DEBUG_MODE is not defined
    std::cout << "Debug info: MY_CONSTANT is " << MY_CONSTANT << std::endl;
}
#endif

int main() {
    std::cout << "Starting program." << std::endl;
    greet();
    std::cout << "Value of constant: " << MY_CONSTANT << std::endl;
    
    #ifdef DEBUG_MODE
    debug_print();
    #endif
    
    return 0;
}