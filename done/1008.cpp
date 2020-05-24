// 1008 - Salary
#include <iostream>

using namespace std;

int main() {
    int number, hours;
    float money, salary;
    cout.precision(2);
    cout.setf(ios::fixed);
    cin >> number >> hours >> money;
    salary = hours * money;
    cout << "NUMBER = " << number << "\n";
    cout << "SALARY = U$ " << salary << "\n";
    return 0;
}
