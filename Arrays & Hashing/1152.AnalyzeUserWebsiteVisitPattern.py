import itertools
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        by_user = defaultdict(list)
        
        for user, time, web in zip(username,timestamp,website):#create the hashtable where user:(time,website)
            
            by_user[user].append((time,web))
            
        pattern_counts = defaultdict(set)
        
        for user in by_user:
            #for every user we have, 
            #we will find all of its patterns and add his name to the pattern_counts if he has that pattern
            by_user[user].sort()
            
            websites = [website for time,website in by_user[user]]
            
            user_patterns = set(itertools.combinations(websites,3))
            #to create the patterns out of all the combinations we can
            
            for pattern in user_patterns:
                pattern_counts[pattern].add(user)
                #for each pattern that the user has, we will add its name in the pattern_counts we made
            
        max_score = 0
        best_pattern = None
        
        for pattern, user in pattern_counts.items():
            score = len(user)
            
            if ((score > max_score) or (max_score == score and (best_pattern is None or pattern < best_pattern))):
                max_score = score
                best_pattern = pattern
        return list(best_pattern)
                
                