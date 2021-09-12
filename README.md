# Bulls-and-cows-game-
Tutorial (Decomposition) SC1003 

1A2B (Bulls & Cows) Game Design/Development
We are about to develop the game, called 1A2B (aka. Bulls & Cows) in Python. The game is played as follows:
1.	In the beginning, the game will randomly pick four different digits as the target number (e.g., 2468) to be guessed by the player.

2.	In each round of the game, the player can guess four digits, e.g., 1234. If an user-guessed digit hits the target number and its position is the same as that in the target number, it is considered as 1A (or 1 bull). If an user-guessed digit hits the target number but its position is different from that in the target number, it is considered as 1B (or 1 cow).

For example, if the target number is 2468 and the user guessing is 1234, the result of this round is 2B because both digits 2 and 4 hit the target but their positions are wrong. If the user guessing is 2478, the result of this round is 3A because both digits 2, 4, and 8 hit the target number, and their positions are all correct.

3.	The player wins the game if his/her guessing results in 4A (or 4 bulls), i.e., all the digits appear in the target number, and their positions are correct.

The screen shot of the game could be as follows:

            
