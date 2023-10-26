# Algorithms-Tim-Sort
<div align="center">
  <br>
  <img src="https://github.com/BabyKangaroo117/Frugl-APP/assets/13011373/b5efcc9f-946b-44ee-88cb-0036170282ff">
  <br>
  <a href="https://github.com/justyden/Algorithms-Tim-Sort/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/badge/Contributors-1-blue" /></a>
  <br>
  <br>
 </div>

The Tim sort algorithm combines insertion sort as well as merge sort and for this reasoning, it is considered a hybrid sorting algorithm. The usefulness of this algorithm spans deeply across the coding industry, as this algorithm has been widely used in recent years. Python for example, uses this algorithm for the sorted() method, as well as the list.sort() method. In the process of picking this algorithm, I found it would be necessary to understand an algorithm that has such a practical use case in the real world. Seeing how many different languages alone incorporate this algorithm, I thought it would be fitting to chose and implement it.
## Project Goals

### Understand Tim Sort
This algorithm is strong in the fact that it handles real world data rather well. Understanding this allows the programmer to see the reasoning of picking such an algorithm, all while being enticed to explore the parts that make the algorithm unique. It is a hybrid sorting algorithm, as was already mentioned, and it also as stable algorithm. Using both insertion sort and merge sort, the goal of the algorithm is to try and limit the number swaps and comparisons that are needed. It takes an array and breaks it down into sub arrays, which can also be called runs. In order to for these sub arrays to run as efficiently as possible, there size should be around 32 to 64 for the optimal results. The sub arrays are then pieced back together with the upgraded merge sort algorithm. There are various different methods that can be used to piece the arrays back together, and these methods can get quite complex. To keep it simple the arrys are simply merged back together using the classic approach for this algorithm. Advanced methods include checking the last index in one array is less then the intial index in the other array. This would indicate that each array can be merged together without the need of inserting each index one at a time.

#### Time Complexities
- Best Case Time Complexity is Ω(n)
- Average Case Time Complexity θ(n(log(n)))
- Worst Case Time Complexity is O(n(log(n)))

### Gain an Understanding in Algorithm Design & Implementation
- Picking an algorithm to solve a given problem is an easy task. Picking the __best__ algorithm to solve a required task takes knowledge and experience. The study of this algorithm highlights the areas that it is best at.
- There are plenty of ways to implement the same algorithm. Taking the time to plan it's implementation is important. This project had a planning phase, which allowed me to get a true understanding on the most effiecent way to implement this algorithm.

### Gain Experience in Performance Analysis & Benchmarking
- Testing is one of the most important skill a programmer can have. Anybody can test, but the key to a good tester is to have an open mind that anything can go wrong. By running this algorithm through rigorous amounts of testing not only allows for most bugs to be handled, but also will show how it handles various amounts of inputs.
- The performance of this algorithm is important. Keeping note and testing the performance analysis will demonstrate the importance of this project. This is essentially explaining why choose this algorithm compared to others.
- With both benchmarking and performance analysis combined, a true understanding on the strengths of this algorithm are achieved.

### Gain Problem Solving & Critical Thinking Skills
- Coding is never easy, especially when doing something for the first time. This means there is bound to be bugs somewhere within an application. Thinking logically, and planning the creation of this algorithm out, gives great insight on how it is done in the real world.
- Taking the time to analyize an algorithm and understand which scenarios it would perform best in, is a strong skill to have. While in the testing phase, knowledge will be gained on which applications can utalize this algorithm to the best potential.

## Testing the Alogrithm
### Pytest
- Using poetry, which is a virtual environment handler in python, a pytest script is created to verify the accuracy of this algorithm.
- In order to understand the complexity and speed of this algorithm it is compared with merge sort, which is one of the most standard sorting algorithms.
- Testing includes generating inputs for both algorithms, and checking to make sure it actually sorted the list.
- __Image of the testing__ <img src="Images/Sorting_Algorithms_Testing.png">
- The testing module can be found in test directory. Simply run the command "poetry run pytest" while in the correct directory to verify.

## Performance of the Algorithm
### Testing Tim Sort
#### Input Size of 1000
#### Input Size of 10000
#### Input Size of 50000
#### Input Size of 100000
#### Input Size of 500000
### Testing Merge Sort
#### Input Size of 1000
#### Input Size of 10000
#### Input Size of 50000
#### Input Size of 100000
#### Input Size of 500000
### Comparing the Algorithms
