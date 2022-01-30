#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>
#define sizeData 10 // WIELKOSC PLIKU
#define userCount 6 // ILOSC UZYTKOWNIKOW

using namespace std;

HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);

struct libraryUsers {
  int userID;
  string firstName;
  string lastName;
  int owns; // ilosc wypozyczonych

} users[userCount];

struct libraryBooks {
  int bookID;
  string bookName;
  string authorFirstName;
  string authorLastName;
  int avail;
  float userID; // dostepnosc ksiazki
} books[sizeData];

void dataLoading() // LADOWANIE PLIKOW
{
  ifstream in("DataBooks.txt");

  if (!in) {
    cout << "Nie udalo sie wczytac pliku DataBooks.txt, prosze skontaktowac "
            "sie z obsluga "
         << endl;
    return;
  }

  for (int i = 0; i < sizeData; i++) {
    in >> books[i].bookID >> books[i].bookName >> books[i].authorFirstName >>
        books[i].authorLastName >> books[i].avail >> books[i].userID;
  }

  cout << "Baza ksiazek zaladowana! \n";

  ifstream in2("DataUsers.txt");

  if (!in2) {
    cout << "Nie udalo sie wczytac pliku DataUsers.txt " << endl;
    return;
  }

  for (int i = 0; i < userCount; i++) {
    in2 >> users[i].userID >> users[i].firstName >> users[i].lastName >>
        users[i].owns;
  }
  in2.close();
  cout << "Baza uzytkownikow zaladowana! \n\n\n";
}

void dataOutput() // ZAPIS PLIKOW
{
  ofstream out("DataBooks.txt");
  if (out.is_open()) {
    for (int i = 0; i < sizeData; i++)
      out << books[i].bookID << " " << books[i].bookName << " " << books[i].authorFirstName << " "
          << books[i].authorLastName << " " << books[i].avail << " " << books[i].userID << "\n";
  } else {
    cout
        << "Nie udalo sie wczytac pliku DataBooks.txt, prosze skontaktowac sie "
           "z obsluga ";
    return;
    cout << "Baza ksiazek zaktualizowana!";
    out.close();
  }
}

int main() {


  SetConsoleTitle("Biblioteka");
  int choice1, choice2, choice3, choice4;
  int colorSuccess = 10, colorImportantFailed = 12, colorBiblioteka = 11, colorStandard = 15;
  bool correctSelection = false;
  SetConsoleTextAttribute(console, colorStandard);
  dataLoading();
  SetConsoleTextAttribute(console, colorBiblioteka);
  cout << "=====Biblioteka===== \n";
    SetConsoleTextAttribute(console, colorStandard);

  ///////LOGIN/////////////////////////////////////
  cout << "Zaloguj sie \n";
  do {
    cout << "ID: ";
    cin >> choice1;
    for (int i = 0; i < userCount; i++) // petla na ilosc uzytkownikow
    {
      if (choice1 == users[i].userID) // jesli wybor = uzytkownik then true
      {
        cout << "Witaj >";
        SetConsoleTextAttribute(console, colorImportantFailed);
        cout << users[choice1].firstName;
        SetConsoleTextAttribute(console, colorStandard);
        cout << "<! \n\n";
        correctSelection = true;
      }
    }
    if (correctSelection == false) {
      cout << "Niepoprawny login\n";
    }

  } while (correctSelection == false);

///////LOGIN////////////////////////////////////



    /// MENU ///

  for (;;) {
    SetConsoleTextAttribute(console, colorBiblioteka);
    cout << "\nWybierz opcje: \n";
    SetConsoleTextAttribute(console, colorStandard);
    cout << "1. Wypozycz ksiazke\n";
    cout << "2. Zwrot ksiazki\n";
    cout << "3. Aktualnie wypozyczone ksiazki\n";
    cout << "4. Stan biblioteki\n\n";
    cout << "> ";
    SetConsoleTextAttribute(console, colorImportantFailed);
    cin >> choice2;
    SetConsoleTextAttribute(console, colorStandard);

    /// MENU ///


    ///DEBUG SHOW ALL BOOKS///
     if (choice2 == 99) {
      cout << "\n Database Books \n";
      for (int i = 0; i < sizeData; i++) {
          cout << "BOOK ID: ";
          cout << books[i].bookID << " | BOOK NAME: ";
          cout << books[i].bookName << " | AUTHOR: ";
          cout << books[i].authorFirstName << " | LAST NAME: ";
          cout << books[i].authorLastName << " | AVAIL: ";
          cout << books[i].avail << " | USERID: ";
          cout << books[i].userID << "\n";
      }
  }



    /// WYPOZYCZANIE KSIAZKI ///
    if (choice2 == 1) {
      SetConsoleTextAttribute(console, colorBiblioteka);
      cout << "\nDostepne ksiazki: \n";
        SetConsoleTextAttribute(console, colorStandard);
      for (int i = 0; i < sizeData; i++) {
        if (books[i].avail == 1) {
          cout << "ID: ";
          cout << books[i].bookID << " | ";
          cout << books[i].bookName << " | Autor: ";
          cout << books[i].authorFirstName << " ";
          cout << books[i].authorLastName << "\n";
        }
      }

      SetConsoleTextAttribute(console, colorBiblioteka);
      cout << "Wpisz ID ksiazki, ktora chcesz wypozyczyc \n";
      cout << ">";
      SetConsoleTextAttribute(console, colorImportantFailed);
      cin >> choice3;
      SetConsoleTextAttribute(console, colorStandard);
      if (books[choice3].avail == 0) {
            SetConsoleTextAttribute(console, colorImportantFailed);
        cout << "Ksiazka nie jest dostepna \n";
      } else if (books[choice3].avail == 1) {
          SetConsoleTextAttribute(console, colorBiblioteka);
        cout << "Czy jestes pewien, ze chcesz wypozyczyc ksiazke "
             << books[choice3].bookName << "? (Wpisz 1 - Tak lub 2 - Nie) \n";
        cout << ">";
        SetConsoleTextAttribute(console, colorImportantFailed);
        cin >> choice4;
        SetConsoleTextAttribute(console, colorSuccess);
        if (choice4 == 1) {
          books[choice3].avail = 0;
          books[choice3].userID = choice1;
          cout << "Wypozyczono ksiazke " << books[choice3].bookName << " | "
               << books[choice3].authorFirstName << " "
               << books[choice3].authorLastName << "\n";
          dataOutput();
        }
      }
    }


   /// ZWROT KSIAZKI ///
    if (choice2 == 2) {
    SetConsoleTextAttribute(console, colorBiblioteka);
      cout << "\n Wypozyczone ksiazki: \n";
    SetConsoleTextAttribute(console, colorStandard);
      for (int i = 0; i < sizeData; i++) {
        if (choice1 == books[i].userID ) {
          cout << "ID: ";
          cout << books[i].bookID << " | ";
          cout << books[i].bookName << " | Autor: ";
          cout << books[i].authorFirstName << " ";
          cout << books[i].authorLastName << "\n";

        }
      }
SetConsoleTextAttribute(console, colorBiblioteka);
      cout << "Wpisz ID ksiazki, ktora chcesz zwrocic";
      cout << ">";
    SetConsoleTextAttribute(console, colorImportantFailed);
      cin >> choice3;
      if(choice1 == books[choice3].userID)
      {
          SetConsoleTextAttribute(console, colorSuccess);
          cout << "Zwrocono " << books[choice3].bookName << "! \n";
          books[choice3].avail = 1;
          books[choice3].userID = -1;
          dataOutput();
      }
      else{
        SetConsoleTextAttribute(console, colorImportantFailed);
        cout << "Niestety nie widzimy bys posiadal ta ksiazke! Jesli to blad, skontaktuj sie z obsluga\n";
      }
    }


    /// WYPOZYCZONYE KSIAZKI PRZEZ UZYTKOWNIKA ///
    if (choice2 == 3) {
            SetConsoleTextAttribute(console, colorBiblioteka);
        cout << "Twoje wypozyczone ksiazki: \n";
    SetConsoleTextAttribute(console, colorStandard);
      for (int i = 0; i < sizeData; i++) {
        if (books[i].userID == choice1) {
          cout << "ID: ";
          cout << books[i].bookID << " | ";
          cout << books[i].bookName << " | Autor: ";
          cout << books[i].authorFirstName << " ";
          cout << books[i].authorLastName << "\n";
        }
      }
    }
    /// SPRAWDZENIE STANU WSZYSTKICH KSIAZEK ///
       if (choice2 == 4) {
            SetConsoleTextAttribute(console, colorBiblioteka);
        cout << "Stan biblioteki: \n";
       SetConsoleTextAttribute(console, colorStandard);
      for (int i = 0; i < sizeData; i++) {

          cout << "ID: ";
          cout << books[i].bookID << " | ";
          cout << books[i].bookName << " | Autor: ";
          cout << books[i].authorFirstName << " | ";
          cout << books[i].authorLastName << " |  ";
          if(books[i].avail == 1)
          {
            SetConsoleTextAttribute(console, colorSuccess);
            cout << ">Dostepna< \n";
                      SetConsoleTextAttribute(console, colorStandard);
          }
            else{
                    SetConsoleTextAttribute(console, colorImportantFailed);
                    cout << ">Niedostepna< \n";
                              SetConsoleTextAttribute(console, colorStandard);
            }

      }
    }
  }
}

