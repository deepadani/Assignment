#implementing circular queue using dictionary

from circular_dict import CircularDict

# max len of queue is 5
circularQ = circular_dict(len=5)

circularQ[0] = 10
circularQ[1] = 20
circularQ[2] = 30
circularQ[3] = 40
circularQ[4] = 50

print(f"queue items now: {circular_dict}")

# adding element beyond len limit
circularQ[5] = 60

print(f"overflow: {circular_dict}")