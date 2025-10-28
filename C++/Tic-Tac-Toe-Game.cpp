#include <bits/stdc++.h>

using namespace std;

const char space = ' ', P1 = 'X', P2 = 'O';
char board[3][3] = {{space, space, space}, {space, space, space}, {space, space, space}}, h = P1;

void printBoard()
{
    cout << "Game Board:\n";
    cout << "  1 2 3\n";
    for (int i = 0; i < 3; i++)
    {
        cout << i + 1 << " ";
        for (int j = 0; j < 3; j++)
        {
            cout << "|" << board[i][j];
        }
        cout << "|\n";
    }
}

void newBoard()
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            board[i][j] = space;
        }
    }
}

bool isWinner()
{
    for (int i = 0; i < 3; i++)
    {
        if (board[i][0] == h && board[i][1] == h && board[i][2] == h)
        {
            return true;
        }
        if (board[0][i] == h && board[1][i] == h && board[2][i] == h)
        {
            return true;
        }
    }
    if ((board[0][0] == h && board[1][1] == h && board[2][2] == h) ||
        (board[0][2] == h && board[1][1] == h && board[2][0] == h))
    {
        return true;
    }
    return false;
}

bool fullBoard()
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] == space)
            {
                return false;
            }
        }
    }
    return true;
}

int main()
{
    cout << "Welcome to 'X' & 'O' Game\n";
    while (true)
    {
        printBoard();
        cout << "Player '" << h << "' Turn (Enter Row Then column Like 1 1): ";
        int row, col;
        cin >> row >> col;
        if (0 <= (row - 1) && (row - 1) < 3 && 0 <= (col - 1) && (col - 1) < 3 && board[row - 1][col - 1] == space)
        {
            board[row - 1][col - 1] = h;
            if (isWinner())
            {
                printBoard();
                cout << "Congratulations, Player '" << h << "' wins" << endl;
                string again;
                cout << "Do you want to play again? (y/n): ";
                cin >> again;
                if (again == "Y" || again == "y" || again == "yes" || again == "YES" || again == "Yes")
                {
                    newBoard();
                    h = P1;
                    continue;
                }
                else
                {
                    cout << "Thanks for playing, Goodbye\n";
                    break;
                }
            }
            else if (fullBoard())
            {
                printBoard();
                cout << "It's a Tie!" << endl;
                string again;
                cout << "Do you want to play again? (y/n): ";
                cin >> again;
                if (again == "Y" || again == "y" || again == "yes" || again == "YES" || again == "Yes")
                {
                    newBoard();
                    h = P1;
                    continue;
                }
                else
                {
                    cout << "Thanks for playing, Goodbye\n";
                    break;
                }
            }
            if (h == P1)
            {
                h = P2;
            }
            else
            {
                h = P1;
            }
        }
        else
        {
            cout << "Invalid move. Please choose an empty space\n";
        }
    }
}