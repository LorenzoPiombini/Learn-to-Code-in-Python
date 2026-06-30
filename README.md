# List Comprehension

---

When your party clears a dungeon, you often need to modify an entire list of data. For example, doubling the gold found, or filtering out junk loot.
Up until now, you've probably used a standard `for` loop to build a new list:

```python
    doubles = []
    for value in range(0,10):
        doubles.append(value * 2)

    print(doubles) #[0,2,4,6,8,10,12,14,16,18]
```

Python provides a cleaner, highly optimized syntax for this exact pattern called a list comprehension.  
It allows you to declare a new list and populate it in a single line.

## The Syntax

```python
    your_list = [ value * 2 for value in range(0,10)]
```


# Assignment
Assignment
Our players just drank an XP Potion. For the next few minutes, all experience points gained from defeating monsters are doubled!

Complete the double_xp function. It accepts a list of integers (base_xp_rewards) and should return a new list with all the values doubled using a list comprehension. Do not use a traditional for loop.  

