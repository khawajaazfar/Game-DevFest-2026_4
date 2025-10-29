#include <iostream>
using namespace std;

int main() {
    float a, b, c, d, e;
    cout << "Enter First Value: ";
    cin >> a;
    cout << "Enter Second Value: ";
    cin >> b;
    cout << "Enter Third Value: ";
    cin >> c;
    cout << "Enter Fourth Value: ";
    cin >> d;
    cout << "Enter Fifth Value: ";
    cin >> e;

    if (a >= b && a >= c && a >= d && a >= e)
        cout << "Largest number: " << a;
    else if (b >= a && b >= c && b >= d && b >= e)
        cout << "Largest number: " << b;
    else if (c >= a && c >= b && c >= d && c >= e)
        cout << "Largest number: " << c;
    else if (d >= a && d >= b && d >= c && d >= e)
        cout << "Largest number: " << d;
    else
        cout << "Largest number: " << e;

    return 0;
}
