# Enumerate

Sometimes when looping through a list, you don't just need the item itself—you also need to know its **index** (its position in the list).

You *could* track this manually with a counter variable, but it's ugly:

```python
i = 0
for item in inventory:
    print(f"{i}: {item}")
    i += 1
```
