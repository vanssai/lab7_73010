import pandas as pd

dane = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imie': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
}
df = pd.DataFrame(dane)

print("Oceny > 4:")
print(df[df['Ocena'] > 4])

print("\nSortowanie wiekiem:")
print(df.sort_values(by='Wiek'))

print("\nŚredni wiek dla oceny:")
print(df.groupby('Ocena')['Wiek'].mean())

poprawa = pd.DataFrame({'Nr_albumu': [5], 'Ocena_Poprawa': [3.0]})
df = pd.merge(df, poprawa, on='Nr_albumu', how='left')

df.to_csv('studenci.csv', index=False)

nowy = pd.DataFrame([{'Nr_albumu': 6, 'Imie': 'Olek', 'Nazwisko': 'B', 'Ocena': 4.0, 'Wiek': 20}])
df = pd.concat([df, nowy], ignore_index=True)

print("\nPo dodaniu studenta:")
print(df.tail(2))

print("\nUnikalne oceny:", df['Ocena'].unique())
print("Ilość piątek:", len(df[df['Ocena'] == 5.0]))