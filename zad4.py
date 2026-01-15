import pandas as pd

dane = {
    'ID': [1, 2, 3, 4, 5],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Imie': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager']
}
df = pd.DataFrame(dane)

print("Zarabiają powyżej 5000:")
print(df[df['Pensja'] > 5000])

print("\nPosortowani po wieku:")
print(df.sort_values(by='Wiek'))

print("\nŚrednia pensja na stanowisko:")
print(df.groupby('Stanowisko')['Pensja'].mean())

nowe_dane = pd.DataFrame({'ID': [2, 4], 'Nowe_Stanowisko': ['Senior', 'Team Lead']})
polaczone = pd.merge(df, nowe_dane, on='ID', how='left')
print("\nPo połączeniu:")
print(polaczone)

polaczone.to_csv('pracownicy.csv', index=False)
print("\nWczytano z pliku:")
print(pd.read_csv('pracownicy.csv').head(2))