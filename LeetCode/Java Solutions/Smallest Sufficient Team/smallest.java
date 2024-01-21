class Solution {
    int totalPeople; // Total number of people
    int[] skillsMaskOfPerson; // Binary representation of each person's skills
    long[] memoizationArray; // Store results for reuse

    // Function to find the smallest sufficient team for the required skills
    private Long findSmallestTeam(int skillsMask) {
        if (skillsMask == 0) {
            return 0L; // If no skills are required, return 0
        }
        // Check memoization array for previously calculated results
        if (memoizationArray[skillsMask] != -1) {
            return memoizationArray[skillsMask];
        }
        // Go through each person
        for (int i = 0; i < totalPeople; i++) {
            int smallerSkillsMask = skillsMask & ~skillsMaskOfPerson[i]; // Remaining skills after removing current person's skills
            if (smallerSkillsMask != skillsMask) { // If current person has any required skills
                long peopleMask = findSmallestTeam(smallerSkillsMask) | (1L << i); // Find team with current person included
                // If the new team is smaller, update memoization array
                if (memoizationArray[skillsMask] == -1 || Long.bitCount(peopleMask) < Long.bitCount(memoizationArray[skillsMask])) {
                    memoizationArray[skillsMask] = peopleMask;
                }
            }
        }
        // Return the smallest team for current required skills
        return memoizationArray[skillsMask];
    }

    public int[] smallestSufficientTeam(String[] requiredSkills, List<List<String>> peopleSkills) {
        totalPeople = peopleSkills.size(); // Total number of people
        int totalSkills = requiredSkills.length; // Total number of skills

        // Map each skill to a unique index
        HashMap<String, Integer> skillIndexMap = new HashMap<String, Integer>();
        for (int i = 0; i < totalSkills; i++) {
            skillIndexMap.put(requiredSkills[i], i);
        }

        // Binary representation of each person's skills
        skillsMaskOfPerson = new int[totalPeople];
        for (int i = 0; i < totalPeople; i++) {
            for (String skill : peopleSkills.get(i)) {
                skillsMaskOfPerson[i] |= 1 << skillIndexMap.get(skill);
            }
        }

        // Initialize memoization array
        memoizationArray = new long [1 << totalSkills];
        Arrays.fill(memoizationArray, -1);

        // Find the smallest sufficient team for all skills
        long smallestTeamMask = findSmallestTeam((1 << totalSkills) - 1);

        // Convert binary representation of the smallest team to indices array
        int[] teamIndices = new int [Long.bitCount(smallestTeamMask)];
        int index = 0;
        for (int i = 0; i < totalPeople; i++) {
            if (((smallestTeamMask >> i) & 1) == 1) {
                teamIndices[index++] = i;
            }
        }
        return teamIndices;
    }
}

