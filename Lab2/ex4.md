# Lab 2: Exercise 4:

## Question 1: Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan. [0.5 pts]

#### Answer: Since we do not know how many rooms are between 100 - 130, we cannot do binary or interpolation search. Thus, the best searching algorithm for this hallway would be linear search, but we will start our linear search from the room 130 and work backwards towards 128. 

## Question 2: How many ”steps” it will take to find room EY128? And what is a “step” in this case? [0.25 pts]

#### Answer: It will take 2 steps to find room EY128. This is because we will start at room EY130 and search that first. Then we would continue backwards onto our next room and search that room which would be EY128. A "step" in this case is the processing of looking inside a room and confirming what its room number is. 

## Question 3: Is this a best-case scenario, worst-case scenario, or neither? [0.25 pts]

#### Answer: It is neither since the best case scenario would have been if we were looking for room EY130. It is also not a worse case scenarion since we did not have to look inside all the room; we only had to look inside 2 rooms. 

## Question 4: With this particular sign and floor layout, explain what a worst-case or best-case scenario would look like [0.5 pts]

#### Answer: Considering we know the layout and the floor plan, the worst case scenarion is when we start searching for room EY128 by going left towards room EY100 first. This is because we would have to go around three corners of the building to finally find our room. And the best case scenario would be if we started our search by going right first towards room EY138. This way we would be closest to our desired room and thus we could find it fastest.

## Question 5: Suppose after a few weeks in the term you memorize the layout of the floor. How would you improve the algorithm to make it more efficient? [0.5 pts]

#### Answer: I would make the linear search to start at the room right before room EY130. Since I would know, the room before EY130 has to be a smaller number such as EY129. I would start the search right before EY130. This way, the linear search method would mean immediately checking inside the room EY128 to confirm whether it was EY128 or some other number. And because it is EY128, the linear search would yield a time complexity of O(1) since the very first element is what we are looking for. 