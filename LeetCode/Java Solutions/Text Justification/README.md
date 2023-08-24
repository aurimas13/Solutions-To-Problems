The problem of description of "Text Justification" is found [here](https://leetcode.com/problems/text-justification/description/) while the solution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Text%20Justification/text.java).

**Explanation**:

1. `Initialize Variables`:

- `res`: The final list to store all the justified lines.
- `cur`: A list to keep track of words for the current line.
- `num_of_letters`: A counter to keep track of the length of all words in cur (excluding spaces).

2. `Iterate through Each Word`:

- For every word, check if adding the current word to the current line (cur) would exceed maxWidth.
- If it would, then justify the current line.

3. `Space Distribution`:

- Distribute the spaces between the words in cur to make the total length equal to maxWidth.
- Use modulo arithmetic to wrap around the spaces in case there are more spaces than gaps between words. This ensures extra spaces are placed from the leftmost gap between words.

4. `Handle Last Line`:

- Once all words are processed, the words remaining in cur form the last line. This line should be left-justified.

**Practical Implementation**:

Imagine you're building a simple text editor or a publishing software where the content needs to be justified to provide a polished and structured look, especially for print or formal presentations.

- `Scenario`:
You work at a publishing house. An author submits a manuscript, and your job is to format the content for printing. The content should be justified to align with both the left and right margins.

- `Input`:
Words from a paragraph in the manuscript:
`["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]`
`MaxWidth = 16`

- `Application of Solution`:

Start with the first word "The". This word by itself won't exceed the maxWidth.
Add the next word, "quick". Now, your line looks like "The quick", which is still within the limit.

Add the next word, "brown". Your line is "The quick brown", which is still okay.

Try adding "fox". It exceeds the maxWidth. So, "The quick brown" is one line. You need to add spaces to fully justify it.
"The quick brown" becomes "The quick brown". This line is added to res.

Start the next line with "fox".

Repeat this process until all words are processed.