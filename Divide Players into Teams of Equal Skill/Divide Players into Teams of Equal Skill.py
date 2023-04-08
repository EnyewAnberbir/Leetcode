class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skills = sorted(skill)
        i = 0
        j = len(skills) -1
        total_skills = skills[i] + skills[j]
        total = 0
        while i<=j:
            
            if skills[i] + skills[j] == total_skills:
                a= skills[i]* skills[j]
                total+=a
                i+=1
                j-=1
            else:
                return -1
        return total
