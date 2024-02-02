#Exercise 2#

    

####1. Mention at least two aspects that make interpolation search better than binary search.

Interpolation search differs from regular binary search only in the way it divides the the array. While binary search simply divides the array into two halves down the middle, interpolation makes better use of the assumption. That is, if the value of the key is closer to the last element, interpolation will start searching closer towards the end of the array due to the implementation of its pos formula. In addition, Being able to "hone in" on the target value means that interpolation search generally has to go through reduced iterations/calls than binary search; and thus is faster. 

####2. Interpolation search assumes that data is uniformly distributed. What happens this data follows a different distribution? Will the performance be affected? Why?

Interpolation search's functionality heavily depends on its assumption that the array is uniformly distributed. As such, the performance of the algorithm becomes unpredictable, even having the possibility to fail. For example, consider a situation where the key is 8 (10 values total), interpolation search will then start searching near the top of the array, and if the unsorted list has 8 near the beginning of the list, it could end up dismissing it when dividing the array into sub-arrays.

####3. If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected?

To modify interpolation search to follow a different distribution, we would need to modify to pos formula. The pos formula here was constructed using the assumption of linear (uniform) distribution as its formula is derived from the slope equation of a straight line. Thus to account for say Gaussian distribution, you would have to change the pos formula accordingly.

####4. When is linear search your only option for searching data as binary and interpolation search may fail?

Linear search being the **only** option for searching data would occur when the data is randomly sorted in a way that would fail binary and interpolation search. That is to say if both binary and interpolation would end up dismissing the wrong sides of the array due to the random sort.

####5 In which case will linear search outperform both binary and interpolation search, and why?

Linear search outperforms both binary and interpolation search for its best case scenario when the key is the first value in the array. The complexity for linear search in this case is O(1) whereas binary and interpolation would continue to go through multiple iterations/calls before landing on the first element.

####6 Is there a way to improve binary and interpolation search to solve this issue?

Binary always divides the array into halves, so even if it is known that the key is on the first position, binary would keep dividing until it ends up on the first element. For interpolation it is much the same as it relies on probability. The **only** way to account for this is the trivial solution of adding a check on the first element before proceeding with the binary/interpolation algorithm; which isn't very useful as if the target value is on the second position then the problem still persists.