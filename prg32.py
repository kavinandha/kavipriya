def word_count(str):
    counts=dict()
    words=str.split()
    for word in words:
        if word in counts:
          count[words]+=1
        else:
          counts[words]=1
    return counts
 print(word_count('the quick brown fox jumps.'))
