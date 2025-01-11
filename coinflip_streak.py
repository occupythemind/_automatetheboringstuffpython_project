from rich import print
import random
import sys

# Streak: Doesn't essentially mean the number of 
# occurancies of that item, rather it checks for how long
# an items was able to go in a list before another replace
# ment. For example: [1,2,3,3,3,4,4,5,6]
#           1 has a streak of 0
#           2 has  0 also
#           3 has 3 (caused it showed up 3 times in a roll)
#           4 has 2
#           5 has 0
#           6 has 0
# Humans are bad at guessing and are less likely to give up to 
# 6 streak. 
# Number of streak: Will check how many times this streak occ-
# -ured.

def toss_coin(num_toss):
    '''Toss tha coin'''
    outcome = []
    for i in range(num_toss):
        flip = random.randint(0, 1)
        if flip == 0:
            outcome.append('H')
        elif flip == 1:
            outcome.append('T')
    consent =  get_streak(outcome, num_toss)
    if not consent:
        sys.exit()
        




def get_streak(outcome, num_toss):
    '''Lets get the streak, returns true or False indicating
    if the main loop should continue or not.'''
    streak = [] # capture streak values
    nos = 0 # Number of strings
    sk_num = 3
    for i in outcome:
        '''capture total streak'''
        if not streak:
            streak.append(i)
        elif streak[-1] == i:
            streak.append(i)
        elif streak[-1] != i:
            if len(streak) >= sk_num:
                nos += 1
            streak = []
            streak.append(i)
    
    hstrk = []
    hstreaks = []
    for i in outcome:
        '''capture either H or T face'''
        if not hstreaks:
            hstreaks.append('H')
        if hstreaks[-1] == i:
            hstreaks.append(i)
        elif hstreaks[-1] != i:
            del(hstreaks[0]) #To remove the 'H' appended to it by default for accuracy.
            if len(hstreaks) >= sk_num:
                hstrk.append(hstreaks)
            hstreaks = []
    print(f"\n{hstrk}")  #You use this to monitor the code
    print(f"H streak: {len(hstrk)}")
    
    tstrk = []
    tstreaks = []
    for i in outcome:
        '''capture T face'''
        if not tstreaks:
            tstreaks.append('T')
        elif tstreaks[-1] == i:
            tstreaks.append(i)
        elif tstreaks[-1] != i:
            del(tstreaks[0]) #To remove the 'T' appended to it by default for accuracy.
            if len(tstreaks) >= sk_num:
                tstrk.append(tstreaks)
            tstreaks = []
    print(f"\n{tstrk}")  #You use this to monitor the code
    print(f"T streak: {len(tstrk)}")
    
    print(f"\n{outcome}\n\
          [u][b]STREAK DETAILS OF >= {sk_num}[/b][/u]\n\
          Total Number of Streaks: {nos}\n\
          Total Number of Steaks(%): {round((nos/num_toss)*100, 3)}%\n\
          DONE.\n\nDo you still wanna toss?\n")
    while True:
        try:
            ans = input('Ans[y/n]: ').lower()
            if ans == 'y' or ans == 'yes' or ans == 'yeah':
                return True
                break
            elif ans == 'n' or ans == 'no' or ans == 'nah':
                return False
                break
            elif ans == '':
                return True
                break
            else:
                print(f"Response should be yes(y) or no(n)")
        except KeyboardInterrupt:
            print('\nBye')
            break
        except EOFError:
            print('\nBye')
            break


if __name__ == '__main__':
    print(f"[b]WELCOMe  to ECoin Toss \n\
          NOTE(should be red color): Streaks may not always match but their percentages\n\
          are good enough[/b]\n")
    while True:
        try:
            num_toss = ''
            num_toss = int(input('How many times should we toss? '))

            if num_toss == None:
                continue
            elif num_toss == 0:
                print("\tSorry can't toss 0 times.")
                continue
            elif str(num_toss).split('-')[0] == '':
                print("\tSorry, can't toss for Negative Value.")
                continue

            toss_coin(num_toss)
        except ValueError:
            print(f"{num_toss} is not a number.")
            continue
        except KeyboardInterrupt:
            break
        except EOFError:
            break
            