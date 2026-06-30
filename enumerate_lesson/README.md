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

> [!NOTE]
> [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) yields a tuple containing `(index, item)`. 



## 📋 Tips

<details>
<summary>Click to expand additional hints</summary>

1.  By default, `enumerate()` starts counting at `0`. However, you can pass an optional `start` keyword argument to change this behavior:

    ```python
    for index, item in enumerate(inventory, start=1):
        print(f"Item #{index}: {item}")
    ```

</details>
