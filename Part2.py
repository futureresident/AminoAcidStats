

import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
from sklearn import svm
svc = svm.SVC(kernel='linear')

###############

def load_data(filename='./amino.csv'):
    reader = csv.reader(open(filename, 'r', encoding='utf-8', errors='ignore'))
    data = []
    for line in reader:
        data.append(line)
    return data

data = load_data()


import matplotlib.pyplot as plt

################

def viz1(data):
    """
    This function will create a pie chart of the proportion of codons that code for the same amino acid
    :param data: Takes a list of amino acids containing their 3-letter codes, 1-letter codes, and full name, as well as their codons
    :return:
    """
    # Initializing a list of amino acids
    aminos = []
    # Loop iterating over the data in order to create a list of 3-letter codes for amino acids that show up in the data set
    for n in data:
        aminos.append(n[1])
    # This list ensures each 3-letter code appears only once.
    amino_list = sorted(set(aminos))
    # Initiates a list of averages for the proportion of codons that code for the same amino acid.
    averages = []
    # Iterates over every amino acid in list created above
    for aa in amino_list:
        # Count of how many times an amino acid shows up in the data set
        x=0
        # Iterates over every row in the data set and checks how many times an amino acid shows up
        for n in data:
            if aa == n[1]:
                x +=1
            average = x/64 * 100
        # Appends the frequency in percent to a list of averages.
        averages.append(average)


    # Pie chart, where the slices will be ordered and plotted counter-clockwise:


    # This is code from the matplotlib gallery that plots a pie chart of the frequency of each base
    fig1, ax1 = plt.subplots()
    ax1.pie(averages, labels=amino_list, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Proportion Of Codons Coding For A Single Amino Acid.")

    plt.show()

viz1 = viz1(data)

#################

def viz2(data):
    """
    This function will create a pie chart of the frequency of each base in the codons of the amino acids
    :param data: Takes a list of lists, each list is of amino acid, its codon, its 3-letter code, and 1-letter code.
    :return:
    """
    # List of bases the comprise what the codons are representing
    bases = ['A', 'T', 'C', 'G']
    # Empty list of the frequency of each base
    frequency = []
    # The total number of bases in the 64 codons
    total_bases = 64*3
    # This loop will iterate over every base in the list above
    for i in bases:
        # Count of frequency of each base
        x = 0
        # This for loop will iterate over each amino acid with its associated information (each row in the data set)
        for a in data:
            # This for loop will iterate over every base in the codon of every amino acid in the list, and checks if the base comes up in each codon and how many times
            for c in a[0]:
                if i == c:
                    x += 1
        proportion = x/total_bases *100
        frequency.append(proportion)

    # This is code from the matplotlib gallery that plots a pie chart of the frequency of each base
    fig1, ax1 = plt.subplots()
    ax1.pie(frequency, labels=bases, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Proportion Of Bases Used In Codons.")

    plt.show()

viz2 = viz2(data)

###################
###################



# The following lines of code are used to organize the 1-letter codes of amino acids into a list of numbers, each number
# refers to each letter specifically.
# Initiate a list of 1-letter codes of amino acids
sub_labels = []
# This for loop will append the third element of each row in the data set to the sub_labels
for r in data:
    sub_labels.append(r[2])

    # Initiate the actual list of labels, containing numbers that refer to each 1-letter code.
labels = []
for i in sub_labels:
    sub_label = []
    sub_label2 = []
    # This if statement is here because there are three codons that do not code for an amino acid, but rather they code
    # for a stop codon. Since the function "ord()" (see below) only takes 1 letter string to convert them to numbers,
    # I have created my own number code for "Stop", ensuring that it doesn't match any of the other number codes.
    if i == 'Stop':
        i = 50
        n = i
        labels.append(n)
        # This will ensure that the for loop skips "Stop" so the program doesn't crash.
        continue
    # This function will create a unique number for each 1-letter code in the list sub_labels
    ord(i)
    # Adds to the final list, labels
    labels.append(ord(i))


   #################

# This will load the first column of the dataset in a list of codons
sub_data = []
for n in data:
    sub_data.append(n[0])



# This will load the list of codons into a list of lists. Each internal list will hold the codons in the form of
# comma separated numbers that uniquely identify each letter of the codon.
sub_data2 = []
# Iterates over every codon in the list sub_data
for c in sub_data:
    list = []
    # Iterates over every letter in each codon in the lit sub_data
    for b in c:
        # appends the unique number of each letter of each codon to a list initialized earlier
        list.append(ord(b))
    # Finally appends the list of unique numbers identifying each codons
    sub_data2.append(list)


# Converting the
final_data = np.array(sub_data2)
final_labels = np.array(labels)
