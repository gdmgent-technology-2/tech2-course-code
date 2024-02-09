'''
Your task is to create a system that checks all the clocks in the town and synchronizes them with the Grand Clock Tower. You'll be given a list of times from various clocks around the town, and you must determine how many minutes each clock is ahead or behind the Grand Clock Tower's time.
'''

# create a variable with 4 times
grand_clock_time = '15:00'
times = ['14:45', '15:05', '15:00', '14:40']

# calculate the difference between two times
def time_difference(time1, time2):
    time1 = time1.split(':')
    time2 = time2.split(':')
    time1 = int(time1[0])*60 + int(time1[1])
    time2 = int(time2[0])*60 + int(time2[1])
    return time2 - time1

# loop through the times and calculate the difference between the time in the list and grand clock time
differences = [time_difference(grand_clock_time, time) for time in times]

# print the differences
print(differences)