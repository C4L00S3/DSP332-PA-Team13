# DSP332-PA-Team13
DSP332 - Fundamentals of AI, First practical assignment

## Game description
At the beginning of the game, the generated numerical string is given. Each player has 0 points. Players perform moves sequentially. During the move, the player chooses any pair of two adjacent numbers and replaces it with a single number based on the following conditions: 
* if the sum of the numbers of the selected pair is greater than 7, then the pair of numbers is replaced by 1 and one point is added to the player's score;
* if the sum of the numbers is less than 7, then it is replaced by 3 and 1 point is deducted from the player's score;
* if the sum is equal to 7, then it is replaced by 2 and 2 points are added to the player's score.

The game ends when there are no more pairs of numbers to replace. If the players have the same number of points, the result is a draw. Otherwise, the player with the higher number of points wins.
