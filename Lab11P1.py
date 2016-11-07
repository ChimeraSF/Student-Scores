__author__ = 'Shaylene Frank'

def main():
    #Get scores and number of students from functions
    print('Enter test scores of class 1.')
    scores1 = get_class1()
    num_students1 = len(scores1)
    print('Enter test scores of class 2.')
    scores2 = get_class2()
    num_students2 = len(scores2)

    #Display number of students and scores from both classes
    print('There are', num_students1, 'students in class 1.')
    print('Scores in class 0001:')
    print(scores1)
    print()
    print('There are', num_students2, 'students in class 2.')
    print('Scores in class 0002:')
    print(scores2)
    print()

    #Combine lists, etc
    print('There are', num_students1 + num_students2, 'students in class 1 and class 2 combined.')
    combo = scores1 + scores2
    print('Scores in combined list:')
    print(combo)
    print('The highest score in the combined list is', max(combo))
    print('The lowest score in the combined list is', min(combo))
    print('Scores in the combined list sorted in ascending order:')
    combo.sort()
    print(combo)
    print('Scores in the combined list sorted in descending order:')
    combo.reverse()
    print(combo)

def get_class1():
    again = 'y'
    scores_1 = []

    while again == 'y':
        score = int(input('Enter a score: '))
        scores_1.append(score)

        again = input('Add another score? [y/n] ').lower()
        print()

    return scores_1

def get_class2():
    again = 'y'
    scores_2 = []

    while again == 'y':
        score = int(input('Enter a score: '))
        scores_2.append(score)

        again = input('Add another score? [y/n] ').lower()
        print()

    return scores_2


main()
