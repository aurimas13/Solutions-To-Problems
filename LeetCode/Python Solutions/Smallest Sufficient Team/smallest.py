class Solution:
    def smallestSufficientTeam(self, required_skills: List[str], people_skills: List[List[str]]) -> List[int]:

        skill_to_index_map = {skill : i for i, skill in enumerate(required_skills)} # Map each skill to a unique index
        
        people_skill_bits = []
        for skills in people_skills: 
            skill_bits = 0
            for skill in skills: 
                skill_bits |= 1 << skill_to_index_map[skill] # Convert the skill set to a bit representation
            people_skill_bits.append(skill_bits)
        
        @cache
        def find_min_team(start_index: int, required_skill_bits: int): 
            """
            Returns the smallest sufficient team starting from the person at 
            `start_index` for the skills represented in `required_skill_bits`.
            """
            if required_skill_bits == 0: 
                return [] # No more skills are required

            if start_index == len(people_skills): 
                return [0]*100 # Impossible case, no more people available but skills are still required

            # If the current person does not have any required skill
            if not (required_skill_bits & people_skill_bits[start_index]): 
                return find_min_team(start_index+1, required_skill_bits)

            # Minimum team either by including the current person or by excluding them
            return min(
                find_min_team(start_index+1, required_skill_bits),
                [start_index] + find_min_team(start_index+1, required_skill_bits & ~people_skill_bits[start_index]), 
                key=len
            )
        
        total_skills = len(required_skills)
        return find_min_team(0, (1 << total_skills) - 1) # Start from the first person and all skills are required
