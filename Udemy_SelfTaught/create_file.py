with open('st.txt', 'w') as f:
    f.write('Sup suka!')
    
    
my_list=list()

with open('st.txt', 'r') as f:
    my_list.append(f.read())
    
print(my_list)

#write to CSV file

import csv

with open("st.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["one",
                    "two",
                    "three"])
    write.writerow(["four",
                    "five",
                    "six"])
    
    
import csv

with open('st.csv', 'r') as f:
    r= csv.reader(f, delimiter=",")
    for row in r:
        print(','.join(row))
        
        
import csv

with open('movies.csv', 'w', newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(['Top Gun',
                    'Risky Business',
                    'Minority Report'])
    write.writerow(['Titanic',
                    'The Revenant',
                    'Inception'])
    write.writerow(['Training Day',
                    'Man on Fire',
                    'Flight'])
