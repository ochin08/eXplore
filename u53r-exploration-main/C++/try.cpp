
//Print "Hello, World!" to the console


/*
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" <<endl;
    cout << "This is a C++ program using the C++17 standard." << endl;
    return 0;
}
*/




/*
#include <iostream>

int main() {
    int number;
    std::cout << "Enter an integer: ";
    std::cin >> number;
    std::cout << "You entered: " << number << '\n';
    return 0;
}
*/



/*
#include <iostream>
using namespace std;

int main() {
    int n1 = 10;
    int n2 = 4;
    float add = n1 % n2;
    cout << "Total: " << add;
}*/


/*
#include <iostream>
using namespace std;

int main() {
    int day = 3;

    switch (day) {
        case 1:
            cout << "Lunes\n";
            break;
        case 2:
            cout << "Martes\n";
            break;
        case 3:
            cout << "Miyerkules\n";
            break;
        default:
            cout << "Hindi kilalang araw\n";
    }

    return 0;
}
*/




#include <iostream>

// A simple function to add two numbers
int add(int a, int b) {
    return a + b;
}

class Calculator {
public:
    // A member function to multiply two numbers
    int multiply(int a, int b) {
        return a * b;
    }
};

int main() {
    int x = 5;
    int y = 3;

    // Using the standalone function 'add'
    int sum = add(x, y);
    std::cout << "Sum: " << sum << '\n';

    // Using a class and member function
    Calculator calc;
    int product = calc.multiply(x, y);
    std::cout << "Product: " << product << '\n';

    return 0;
}
