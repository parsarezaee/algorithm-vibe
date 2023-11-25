# Palindrome Number Checker

## Table of Contents
- [Introduction](#introduction)
- [How It Works](#how-it-works)

## Introduction
This Python script checks whether an integer is a palindrome, meaning it reads the same backward as forward. It's a solution to the [Palindrome Number problem](https://leetcode.com/problems/palindrome-number/description/) on LeetCode.
<br></br>
## How It Works
- If the input integer is negative, it returns False because negative numbers are not palindromes.

- It converts the integer to a string.

- It reverses the string using slicing.

- It checks if the original string and the reversed string are the same. If they are, it returns True, indicating that the integer is a palindrome; otherwise, it returns False.
