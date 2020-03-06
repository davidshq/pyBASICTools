# The Learning Process

## Introduction

As one composes an application one goes through numerous iterations. With each progressive iteration old code is removed and new code replaces it.

When the project is complete one has a beautiful (hopefully) application. But how did one get there? While it is possible to dig through the git repositories commit history to find earlier versions of the software illustrating its various states, this is a time intensive and haphazard approach.

I've decided to take "snapshots" of important points in the code development process. These will be useful for the following reasons:

1. If I find myself hopelessly stuck, it may help to look at earlier conceptual models or simpler implementations.
1. When I find myself working on a similar project I can be easily refreshed on how I accomplished the same task, especially the intermediate steps.
1. For others who are looking to develop a similar application and can use the snapshots as resources in their own development.

## The Snapshots
1. [pybasictools-03-05-20.py] - Reads a BASIC code file into a Python list. Iterates through the list and outputs the line number of a specified string when it is found within the code.