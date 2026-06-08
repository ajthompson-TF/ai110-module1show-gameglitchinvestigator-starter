# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The new game button does not work after a win and the difficulty scales are illogical.



**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Pressed new game after win | Game starts over and allows new inputs | Pop-up says "You already won. Start a new game to play again.", but no new game is started | Logic error blocking new inputs |
| Difficulty attempts | Easy gives the most attempts, hard gives the least, and normal is between the two | Normal has more allowed attempts than easy | Logic error preventing expected gameplay |
| Difficulty number range | The number range for easy should be shortest, largest for hard, and in-between the two for normal | Normal has wider range than hard | Logic error preventing expected gameplay |
| Used all attempts | The attempts left count is 0 and the player recieves a game over | A game over occurs before the attempts left count says 0 | Logic error preventing expected gameplay |
| Show hint | Tells users to go higher or lower based on their input | Incorrectly guides users on when to go higher or lower | Logic error misleading players |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
