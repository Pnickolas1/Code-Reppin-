"""
Min Rewards: Hard

Given a list of integers, represents a list of scores on a exam. Return the students rewards relative to how
they performed on the exam.
 - Each student must get a reward
 -

Technique used:
 - peaks & valleys, local max/local min, highpoints and lowpoints




"""

# time O(n^2) , space O(n)
def minRewards_naive(scores):
    rewards = [1 for x in scores]
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
    return sum(rewards)



# O(n), O(n)
def getLocalMinIdxs(array):
    if len(array) == 1:
        return [0]
    localMinIdxs = []
    for i in range(len(array)):
        if i == 0 and array[i] < array[i + 1]:
            localMinIdxs.append(i)
        if i == len(array) - 1 and array[i] < array[i - 1]:
            localMinIdxs.append(i)
        if i == 0 or i == len(array) - 1:
            continue
        if array[i] < array[i + 1 and array[i] < array[i - 1]:
            localMinIdxs.append(i)
    return localMinIdxs

def minRewards_optimal2(scores):
    rewards = [1 for _ in scores]
    localMinIdxs = getLocalMinIdxs(scores)
    for localMinIdx in localMinIdxs:
        expandLocalMinIdx(localMinIdx, scores, rewards)
    return sum(rewards)

def expandLocalMinIdx(localMinIdx, scores, rewards):
    leftIdx = localMinIdx - 1
    while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
        rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
        leftIdx -= 1
    rightIdx = localMinIdx + 1
    while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
        rewards[rightIdx] = rewards[rightIdx - 1] + 1
        rightIdx += 1



def minRewardsOptimal(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)






