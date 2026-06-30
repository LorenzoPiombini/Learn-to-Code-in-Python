# List Comprehension

---

Now that we are familiar with **list** in python, we can introduce a very handy way of 'declairing' a List -> LIST COMPREHENSION !

## The Syntax

```python
    your_list = [ value * 2 for value in range(0,10)]
```
this will generate the same output as writing:

```python
    doubles = []
    for value in range(0,10):
        doubles.append(value * 2)

    print(doubles) #[0,2,4,6,8,10,12,14,16,18]
```

# Assignment

When our players gets a XP potion all the experience points they gain from defeating monsters are doubled
complete the function **double_xp** function, it accept a list of int and it will return a list, with the values doubled.
    
