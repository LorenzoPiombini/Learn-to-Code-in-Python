# Enumerate

Sometimes when looping through a list, you don't just need the item itself—you also need to know its **index** (its position in the list).

You *could* track this manually with a counter variable, but it's ugly:

```python
i = 0
for item in inventory:
    print(f"{i}: {item}")
    i += 1
```

python gives us the built-in enumerate() function. It wraps around any iterable and hands you both the index and the item on every single iteration.

```python
for index, item in enumerate(inventory):
    print(f"Slot {index} contains: {item}")
```

> [!NOTE]
> [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) yields a tuple containing `(index, item)`. 

# Assignment

We are building a leaderboard display for our PvP Arena. We have an ordered list of player names representing their rank (index 0 is 1st place, index 1 is 2nd place, etc.).

Complete the *format_leaderboard()* function. It accepts a list of strings (_player_names_). 
loop through the players and return a new list of formatted strings that look like this:

"1. PlayerName"


<details>
<summary>## 📋 Tips</summary>

1.  By default, `enumerate()` starts counting at `0`. However, you can pass an optional `start` keyword argument to change this behavior:

    ```python
    for index, item in enumerate(inventory, start=1):
        print(f"Item #{index}: {item}")
    ```

</details>
