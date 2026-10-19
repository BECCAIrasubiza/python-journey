You **don't absolutely have to** use `float("-inf")`. We use it because we need an initial value that is **smaller than every possible number** in the list.

Let's understand why.

### What is `float("-inf")`?

```python
float("-inf")
```

means **negative infinity**.

Think of it as:

```text
-∞
```

It's smaller than:

```text
-100000
-10
0
10
100000
```

So when we start:

```python
largest = float("-inf")
second_largest = float("-inf")
```

we are basically saying:

> "I haven't found any numbers yet, so start both values extremely low."

---

### Why is that useful?

Suppose your list is:

```python
numbers = [10, 5, 8, 20, 15]
```

At the beginning:

```text
largest = -∞
second_largest = -∞
```

Then the first number is `10`.

Python asks:

```python
10 > -∞
```

Yes! ✅

So:

```text
largest = 10
second_largest = -∞
```

Then the next numbers can gradually replace those values.

---

### What if we started with `0` instead?

You might think:

```python
largest = 0
second_largest = 0
```

But what if the list is:

```python
numbers = [-5, -10, -2, -8]
```

Now:

```text
largest = 0
```

would be wrong because **0 isn't even in the list**.

The program could fail to find the correct largest number.

But:

```python
largest = float("-inf")
```

works because:

```text
-∞ < -5 < -2
```

So the actual numbers can replace it.

---

### There is another way

If you know the list will **never be empty**, you can avoid `float("-inf")` by starting with actual items from the list:

```python
numbers = [10, 5, 8, 20, 15]

largest = numbers[0]
second_largest = numbers[1]
```

But now you have another problem: what if `numbers[1]` is actually larger than `numbers[0]`?

For example:

```python
numbers = [5, 10, 8, 20, 15]
```

You'd need to handle that first.

That's why using:

```python
largest = float("-inf")
second_largest = float("-inf")
```

is a convenient and safe starting point for a list that can contain **any positive or negative numbers**.

### 🧠 Think of it this way

```python
largest = float("-inf")
```

means:

> **"I haven't found a largest number yet."**

It isn't saying that negative infinity is actually part of your list. It's just a **starting placeholder**.

And:

```python
second_largest = float("-inf")
```

means:

> **"I haven't found a second-largest number yet."**



Yes. Let's do it **manually**, without using `sort()`, `max()`, or `sorted()`.

Suppose:

```python
numbers = [10, 5, 8, 20, 15]
```

We want:

```text
largest = 20
second largest = 15
```

### Simple manual solution

```python
numbers = [10, 5, 8, 20, 15]

largest = float("-inf")
second_largest = float("-inf")

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print("Largest:", largest)
print("Second largest:", second_largest)
```

Output:

```text
Largest: 20
Second largest: 15
```

### 🧠 How does it work?

We start with:

```python
largest = float("-inf")
second_largest = float("-inf")
```

`float("-inf")` means **negative infinity**, which is smaller than any normal number.

Then we go through the numbers one at a time.

#### Number = 10

```text
10 > largest?
```

Yes.

So:

```text
second_largest = -∞
largest = 10
```

#### Number = 5

```text
5 > largest?          No
5 > second_largest?  Yes
```

So:

```text
largest = 10
second_largest = 5
```

#### Number = 8

```text
8 > 10?  No
8 > 5?   Yes
```

So:

```text
largest = 10
second_largest = 8
```

#### Number = 20

```text
20 > 10?  YES
```

This is important. Since 20 becomes the new largest, the **old largest (10)** becomes the second largest:

```python
second_largest = largest
largest = number
```

So:

```text
largest = 20
second_largest = 10
```

#### Number = 15

```text
15 > 20?  No
15 > 10?  Yes
```

So:

```text
largest = 20
second_largest = 15
```

### The key idea

This is the part you really want to understand:

```python
if number > largest:
    second_largest = largest
    largest = number
```

Whenever we find a **new largest number**, the previous largest gets pushed down to **second largest**.

Think:

```text
Before:
largest = 10
second = 8

Find 20:

20 becomes largest
10 moves down to second

After:
largest = 20
second = 10
```

Then if we find a number that isn't the largest but is bigger than the current second largest:

```python
elif number > second_largest:
    second_largest = number
```

we update only the second largest.

**This is a very good exercise for learning loops and `if/elif` logic.**
