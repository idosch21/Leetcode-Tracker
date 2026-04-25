class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force for each day go over the array and search for a hotter day
        #getting TLE
        #size = len(temperatures)
        #result = [0]*size
        #counter = 1
        #for i in range(len(temperatures)):
        #    j=i+1
        #    while j<len(temperatures):
        #        if temperatures[i]<temperatures[j]:#meaning there is a warmer weather
        #            #assign the amount of days we calced
        #            result[i] = counter
        #            #and finish move to the next i
        #            break
        #        else:#not warmer or the same
        #            counter+=1
        #        j+=1
        #    counter = 1
        #return result


        #now we can solve it with stack..

        size = len(temperatures)
        result = [0]*size
        stack = []


        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                result[stackInd] = i-stackInd
            stack.append([t,i])

        return result


