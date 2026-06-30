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
> Notice that `enumerate()` yields a tuple containing `(index, item)`. We unpack those right inside the `for` loop declaration.
