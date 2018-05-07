#!/bin/python

__author__ = "Adam Karl"
"""Count the number of Sundays that land on the 1st of the month between two dates"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler019/problem
#First line T the number of test cases
#y1 m1 d1 for start date
#y2 m2 d2 for end date
#Constraints: 1 <= T <= 100; 1900 <= y1 <= 10**16; y1 <= y2 <= (y1+1000); dates are valid

def findFirstOfMonth(date):
    """change date to the first of the following month.
    If the date already is the first of the month, no change"""
    if date[2] == 1:
        return date
    
    date[2] = 1
    date[1] += 1
    if date[1] > 12:
        date[1] = 1
        date[0] += 1
    return date
            
def isBefore(dateA, dateB):
    """returns true if date a is before date b or if a and b are the same day"""
    if dateA[0] < dateB[0]: #year
        return True
    elif dateA[0] > dateB[0]:
        return False
    elif dateA[1] < dateB[1]: #month
        return True
    elif dateA[1] > dateB[1]:
        return False
    elif dateA[2] <= dateB[2]: #day
        return True
    return False

def ZellerDayOfWeek(input_date):
    """Uses Zeller's congruence (Gregorian) to return the day of week.
    Returns 0 for Saturday, 1 for Sunday, .... 6 for Friday"""
    date = [0,0,0]
    date[0] = input_date[0]
    date[1] = input_date[1]
    date[2] = input_date[2]
    if date[1] == 1 or date[1] == 2:
        date[1] += 12
        date[0] -= 1
    q = date[2] #day of month
    m = date[1] #month
    K = date[0] % 100 #year of century (year % 100)
    J = date[0] // 100 #century (19 for 19xx, etc)
    my_sum = q
    my_sum += ((13 * (m + 1)) // 5)
    my_sum += K
    my_sum += (K // 4)
    my_sum += (J // 4)
    my_sum += 5 * J
    return my_sum % 7
    

def main():
    t = int(input())
    for a0 in range(t):
        startDate = list(map(int, input().split()))
        endDate = list(map(int, input().split()))
        
        
        num1stSundays = 0
        startDate = findFirstOfMonth(startDate)
        while isBefore(startDate, endDate):
            if ZellerDayOfWeek(startDate) == 1:
                #print(startDate)
                num1stSundays += 1
            startDate[1] += 1
            if startDate[1] > 12:
                startDate[1] = 1
                startDate[0] += 1
        print(num1stSundays)

if __name__ == "__main__":
    main()
