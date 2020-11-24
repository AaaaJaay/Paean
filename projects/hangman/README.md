# Hangman

### About hangman

Hangman is a word guessing game, popular among school children who are finding the class
very boring and want to play somthing with their friend. In the game, one player will
think of a word, and draw dashes for each letter in the word. The other player has to
guess the word by telling some letter. If the letter is there in the word, then the first
player will put the letter in the correct positions in the word. If the letter is not
there in the word, the the second player gets a miss. The second player has to guess all
the letters correct before getting 8 missis to win. If the second player cannot guess all
the letters, then the first player is the winner. 

### The project

In this project, the computer will play the role of the first player, and will randomly
guess a word. In order to do this, a file `words.txt` is provided. The computer should
choose one word from that file.

Then, the player tries to guess the word by inputting one letter at a time.

Here is a sample output from one game

```
WELCOME TO HANGMAN

I have thought of a word, shown with dashes below
--------
You have got 0 misses
Enter a letter: e
--------
You have got 1 misses
Enter a letter: r
--------
You have got 2 misses
Enter a letter: a
--a-----
You have got 2 misses
Enter a letter: i
--a--i--
You have got 2 misses
Enter a letter: l
--a--i--
You have got 3 misses
Enter a letter: o
--a--i--
You have got 4 misses
Enter a letter: s
s-a--i--
You have got 4 misses
Enter a letter: u
s-a--i--
You have got 5 misses
Enter a letter: m
s-a--i--
You have got 6 misses
Enter a letter: n
s-an-in-
You have got 6 misses
Enter a letter: t
stan-in-
You have got 6 misses
Enter a letter: d
standin-
You have got 6 misses
Enter a letter: g
You got it. It was standing
```
