name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From:'):
        word = line.split()
# Making a list of all after 'From'
        wordy = word[1]
# Use get() to add all the email in a dict just like append
        count[wordy]=count.get(wordy,0)+1

#Here we find the largest no. of all in the dict count same logic as in finding the largest no.
counting=None
wording=None
for words,counts in count.items():
    if counts>counting:
        counting=counts
        wording=words
print(wording,counting)
