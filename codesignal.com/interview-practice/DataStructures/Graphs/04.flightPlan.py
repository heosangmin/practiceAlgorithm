'''
2022/06/16

https://app.codesignal.com/interview-practice/task/s7E6FdhGKCdaCMNoL

Note: Try to solve this task in O(m log n) time, where n is a number of cities and m is a number of flights, since this is what you'll be asked to do during an interview.

Elle is trying to arrange a flight from source to dest. She doesn't mind taking multiple connecting flights, but wants to get to her destination dest as soon as possible. She has a timetable of flights, times, where:

times[i][0] is the starting location of flight i,
times[i][1] is the destination for flight i,
times[i][2] is the time flight i departs,
times[i][3] is the time flight i arrives.
The earliest Elle can leave is midnight (00:00). All times have been encoded as HH:MM. All times are referenced in the timezone of the source, where the hours HH are bigger than 23 if the time is on a subsequent day.

Given the timetable times, source, and dest, return the time when Elle will arrive at dest, if she wants to get here as soon as possible, or "-1" if it's impossible. For her flights:

Assume they all leave and arrive on time.
She needs 60 minutes between flights.
Example

For

times = [["Chicago", "Denver","03:00", "06:00"],
         ["Chicago", "Denver","03:30", "07:00"],
         ["Chicago", "Los Angeles", "01:00", "05:00"],
         ["Denver", "Austin", "06:30", "08:30"],
         ["Denver", "Austin", "07:30", "09:30"],
         ["Austin", "Denver", "06:30", "08:30"],
         ["Los Angeles", "Phoenix", "06:00", "07:00"],
         ["Los Angeles", "Phoenix", "05:30", "06:50"],
         ["Phoenix", "Austin", "08:00", "08:40"]]
source = "Chicago", and dest = "Austin", the output should be
solution(times, source, dest) = "08:40".

The earliest Elle can get from Chicago to Austin is 08:40, by leaving at 01:00 for a trip duration of 7 hours and 40 minutes: Chicago (leaving at 01:00) --> Los Angeles (arrive at 05:00, leave at 06:00) --> Phoenix (arrive at 07:00, leave at 08:00) --> Austin (arrive at 08:40).

Note that there is a quicker path: Chicago (leaving at 03:00) --> Denver (arrive at 06:00, leave at 07:30) --> Austin (arrive at 09:30), which is only 6 hours and 30 minutes. But this isn't the answer we're looking for because it arrives later.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.string times

A timetable of flights, where:

times[i][0] is the starting location of flight i,
times[i][1] is the destination for flight i,
times[i][2] is the time flight i departs,
times[i][3] is the time flight i arrives.
All times have been encoded as HH:MM. All times are referenced in the timezone of the source, where the hours HH are bigger than 23 if the time is on a subsequent day.
Guaranteed constraints:
1 ≤ times.length ≤ 104,
1 ≤ times[i][0].length, times[i][1].length ≤ 15.

[input] string source

The city where Elle starts.

Guaranteed constraints:
1 ≤ source.length ≤ 15,
source ≠ dest.

[input] string dest

The city where Elle wants to travel to.

Guaranteed constraints:
1 ≤ dest.length ≤ 15,
source ≠ dest.

[output] string

Return the time, encoded as HH:MM, when Elle will arrive at dest, if she wants to get here as soon as possible, or "-1" if it's impossible. Hours HH can be bigger than 23 if the time is on a subsequent day.

'''
# ecnerwala's solution
def solution(times, source, dest):
    if source == dest:
        return 0
    def to_minutes(s):
        h, m = map(int, s.split(":"))
        return (h * 60) + m
    dist = {source: 0}
    times = [(src, dst, to_minutes(dep), to_minutes(arr)) for src, dst, dep, arr in times]
    times.sort(key=lambda x: x[3]) # sort by arrival
    # print(times)
    # print(dist)
    for src, dst, dep, arr in times:
        if src in dist and dist[src] <= dep:
            if dst == dest: # arrived
                h, m = arr // 60, arr % 60
                return "%02d:%02d" % (h, m)
            if dst not in dist:
                dist[dst] = arr + 60
    else:
        return "-1"



times = [["Chicago", "Denver","03:00", "06:00"],
         ["Chicago", "Denver","03:30", "07:00"],
         ["Chicago", "Los Angeles", "01:00", "05:00"],
         ["Denver", "Austin", "06:30", "08:30"],
         ["Denver", "Austin", "07:30", "09:30"],
         ["Austin", "Denver", "06:30", "08:30"],
         ["Los Angeles", "Phoenix", "06:00", "07:00"],
         ["Los Angeles", "Phoenix", "05:30", "06:50"],
         ["Phoenix", "Austin", "08:00", "08:40"]]
source = "Chicago"
dest = "Austin"
print(solution(times, source, dest)) # "08:40"

