import sys
import matplotlib.pyplot as plt
import venn as venn
from matplotlib_venn import venn3, venn2, venn3_circles
from  itertools import product

print("\t\t\t\t\tSet Theory Operations")
universal_set = set(range(1, 101))
universal_set1 = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
lst1 = []
lst2 = []
lst3 = []

print("Select which type of sets you want to Enter")
print("1.Integers")
print("2.Alphabets")
type_sets = int(input("Enter Your Choice: "))

if( type_sets ==  1):
 n=int(input("Enter number of elements for set1: "))
 for i in range(n):
     value=int(input("Enter Values: "))
     lst1.append(value)
 n1 = int(input("Enter number of elements for set2: "))
 for i in range(n1):
     value = int(input("Enter Values: "))
     lst2.append(value)
 n2 = int(input("Enter number of elements for set3: "))
 for i in range(n2):
     value = int(input("Enter Values: "))
     lst3.append(value)
 print(lst1)
 print(lst2)
 print(lst3)
 set1=set(lst1)
 set2=set(lst2)
 set3=set(lst3)
 while True:
     print("Enter 1 for Union.")
     print("Enter 2 for Intersection.")
     print("Enter 3 for Difference.")
     print("Enter 4 for Complement.")
     print("Enter 5 for Exit.")


     choice = int(input("Enter Your Choice: "))
     if (choice == 1):
         union = set1.union(set2, set3)
         print("Union of all three sets:", union)
         venn_labels = {'100': 'Set 1', '010': 'Set 2', '001': 'Set 3', '110': 'Set 1 and Set 2',
                        '101': 'Set 1 and Set 3', '011': 'Set 2 and Set 3', '111': 'Set 1, Set 2, and Set 3'}

         venn3(subsets=(len(set1 - set2 - set3), len(set2 - set1 - set3), len(set1 & set2 - set3),
                        len(set3 - set1 - set2), len(set1 & set3 - set2), len(set2 & set3 - set1),
                        len(set1 & set2 & set3)),
                        set_labels=(venn_labels['100'], venn_labels['010'], venn_labels['001']),
                         alpha=0.5)

         plt.title("Venn Diagram - Union of 3 Sets")
         plt.show()

     elif (choice == 2):
         intersection = set1.intersection(set2, set3)
         print("Intersection of all three elements are: ", intersection)
         plt.figure(figsize=(8, 8))
         venn3(subsets=(len(set1 - (set2 | set3)),
                        len(set2 - (set1 | set3)),
                        len((set1 & set2) - set3),
                        len(set3 - (set1 | set2)),
                        len((set1 & set3) - set2),
                        len((set2 & set3) - set1),
                        len(set1 & set2 & set3)),
               set_labels=('Set 1', 'Set 2', 'Set 3'))
         plt.title("Venn Diagram for intersection of 3 Sets")
         plt.show()

     elif(choice == 3):
         difference = set1.difference(set2, set3)
         print("Difference of 3 elements are: ", difference)
         venn_labels = {'100': 'Set 1', '010': 'Set 2', '001': 'Set 3',
                        '110': 'Set 1 and Set 2', '101': 'Set 1 and Set 3', '011': 'Set 2 and Set 3',
                        '111': 'Intersection of all sets', 'A': 'Exclusive to Set 1', 'B': 'Exclusive to Set 2',
                        'C': 'Exclusive to Set 3'}

         venn3(subsets=(len(set1 - set2 - set3), len(set2 - set1 - set3), len(set3 - set1 - set2),
                        len(set1 & set2 - set3), len(set1 & set3 - set2), len(set2 & set3 - set1),
                        len(set1 & set2 & set3)),
               set_labels=(venn_labels['100'], venn_labels['010'], venn_labels['001']),
               alpha=0.5)
         plt.title("Venn Diagram for Difference of Three Sets")
         plt.show()

     elif(choice == 4):
         which_set = int(input("Which set of data You want to complement: "))

         if(which_set == 1):
                 Complement = universal_set - set1
                 print("Complement of universal_set and Set 1: ", Complement)
                 venn_complement_set1 = venn2([universal_set, set1], ('universal_set', 'set1'))
                 plt.title("Complement of Universal set and Set 1 ")
                 plt.show()

         elif(which_set == 2):
                 Complement = universal_set - set2
                 print("Complement of universal_set and Set 1: ", Complement)
                 venn_complement_2 = venn2([universal_set, set2], ('universal_set', 'set2'))
                 plt.title("Complement of Universal_set and Set 1 ")
                 plt.show()

         elif(which_set == 3):
                 Complement = universal_set - set3
                 print("Complement of 3 universal_set elements are: ", Complement)
                 venn_complement_3 = venn2([universal_set, set3], ('universal_set', 'set2'))
                 plt.title("Complement of Universal set and Set 1 ")
                 plt.show()

     elif(choice == 5):
         sys.exit()

elif (type_sets == 2):
 n = int(input("Enter number of elements for set1: "))
 for i in range(n):
     value = input("Enter Values: ")
     lst1.append(value)
 n1 = int(input("Enter number of elements for set2: "))
 for i in range(n1):
     value = input("Enter Values: ")
     lst2.append(value)
 n2 = int(input("Enter number of elements for set3: "))
 for i in range(n2):
     value = input("Enter Values: ")
     lst3.append(value)
 print(lst1)
 print(lst2)
 print(lst3)
 set1 = set(lst1)
 set2 = set(lst2)
 set3 = set(lst3)
 while True:
     print("Enter 1 for Union.")
     print("Enter 2 for Intersection.")
     print("Enter 3 for Difference.")
     print("Enter 4 for Complement.")
     print("Enter 5 for Exit.")

     choice = int(input("Enter Your Choice: "))
     if (choice == 1):
         union = set1.union(set2, set3)
         print("Union of all three sets:", union)
         venn_labels = {'100': 'Set 1', '010': 'Set 2', '001': 'Set 3', '110': 'Set 1 and Set 2',
                        '101': 'Set 1 and Set 3', '011': 'Set 2 and Set 3', '111': 'Set 1, Set 2, and Set 3'}

         venn3(subsets=(len(set1 - set2 - set3), len(set2 - set1 - set3), len(set1 & set2 - set3),
                        len(set3 - set1 - set2), len(set1 & set3 - set2), len(set2 & set3 - set1),
                        len(set1 & set2 & set3)),
               set_labels=(venn_labels['100'], venn_labels['010'], venn_labels['001']),
               alpha=0.5)

         plt.title("Venn Diagram - Union of 3 Sets")
         plt.show()

     elif (choice == 2):
         intersection = set1.intersection(set2, set3)
         print("Intersection of all three elements are: ", intersection)
         plt.figure(figsize=(8, 8))
         venn3(subsets=(len(set1 - (set2 | set3)),  # Size of the region in set1 but not in set2 or set3
                        len(set2 - (set1 | set3)),  # Size of the region in set2 but not in set1 or set3
                        len((set1 & set2) - set3),  # Size of the intersection of set1 and set2 but not in set3
                        len(set3 - (set1 | set2)),  # Size of the region in set3 but not in set1 or set2
                        len((set1 & set3) - set2),  # Size of the intersection of set1 and set3 but not in set2
                        len((set2 & set3) - set1),  # Size of the intersection of set2 and set3 but not in set1
                        len(set1 & set2 & set3)),
               set_labels=('Set 1', 'Set 2', 'Set 3'))
         plt.title("Venn Diagram for intersection of 3 Sets")
         plt.show()

     elif (choice == 3):
         difference = set1.difference(set2, set3)
         print("Difference of 3 elements are: ", difference)
         venn_labels = {'100': 'Set 1', '010': 'Set 2', '001': 'Set 3',
                        '110': 'Set 1 and Set 2', '101': 'Set 1 and Set 3', '011': 'Set 2 and Set 3',
                        '111': 'Intersection of all sets', 'A': 'Exclusive to Set 1', 'B': 'Exclusive to Set 2',
                        'C': 'Exclusive to Set 3'}

         venn3(subsets=(len(set1 - set2 - set3), len(set2 - set1 - set3), len(set3 - set1 - set2),
                        len(set1 & set2 - set3), len(set1 & set3 - set2), len(set2 & set3 - set1),
                        len(set1 & set2 & set3)),
               set_labels=(venn_labels['100'], venn_labels['010'], venn_labels['001']),
               alpha=0.5)
         plt.title("Venn Diagram for Difference of Three Sets")
         plt.show()

     elif (choice == 4):
            which_set = int(input("Which set of data You want to complement: "))
            if(which_set == 1):
                Complement = universal_set1 - set1
                print("Complement of universal_set and Set 1: ", Complement)
                venn_complement_set1 = venn2([universal_set, set1], ('universal_set', 'set1'))
                plt.title("Complement of Universal set and Set 1 ")
                plt.show()

            elif(which_set == 2):
                Complement = universal_set1 - set2
                print("Complement of universal_set and Set 1: ", Complement)
                venn_complement_2 = venn2([universal_set, set2], ('universal_set', 'set2'))
                plt.title("Complement of Universal_set and Set 1 ")
                plt.show()

            elif (which_set == 3):
                Complement = universal_set1 - set3
                print("Complement of 3 universal_set elements are: ", Complement)
                venn_complement_3 = venn2([universal_set, set3], ('universal_set', 'set2'))
                plt.title("Complement of Universal set and Set 1 ")
                plt.show()

     elif (choice == 5):
         sys.exit()
