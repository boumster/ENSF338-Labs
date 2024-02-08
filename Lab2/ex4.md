# Lab 2: Exercise 4:

## Question 1: Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan. [0.5 pts]

Answer: Since we do not know how many rooms are between 100 - 130, we cannot do binary or interpolation search. Thus, the best searching algorithm for this hallway would be linear search, but we will start our linear search from the room 130 and work backwards towards 128 since 128 is much closer to 130 than it is to 100.  

## Question 2: How many ”steps” it will take to find room EY128? And what is a “step” in this case? [0.25 pts]

Answer: It will take 2 steps to find room EY128. This is because we will start at room EY130 and search that first. Then we would continue backwards onto our next room and search that room which would be EY128. A "step" in this case is the processing of looking inside a room and confirming what its room number is. 

## Question 3: Is this a best-case scenario, worst-case scenario, or neither? [0.25 pts]

Answer: It is neither since the best case scenario would have been if we were looking for room EY130. It is also not a worse case scenarion since we did not have to look inside all the rooms; we only had to look inside 2 rooms. 

## Question 4: With this particular sign and floor layout, explain what a worst-case or best-case scenario would look like [0.5 pts]

Answer: Considering we know the layout and the floor plan, the worst case scenarion is when we start searching for room EY128 by going left towards room EY100 first. This is because we would have to go around three corners of the building to finally find our room. And the best case scenario would be if we started our search by going right first towards room EY138. This way we would be closest to our desired room and thus we could find it fastest.

## Question 5: Suppose after a few weeks in the term you memorize the layout of the floor. How would you improve the algorithm to make it more efficient? [0.5 pts]

Answer: I would change the algorithm to an interpolation search. This is because I know how many rooms are between EY100 and EY130, so I know the upper and lower index. Through these variables I could estimate an accurate guess as to where room EY128 is since I also know the rooms' numbers increase by an even number each time. Through interpolation search, I could accurately find the correct element where romm EY128 would be and this would result in a time complexity of O(1) since I would only have to search inside 1 room to confirm that the room is EY128. 