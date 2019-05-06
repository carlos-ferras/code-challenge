## Ormuco Code Challenge

This project has been created only for demonstration purpose.
>
> ### The challenge
>
> Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
>

### The Answer

usage: 

- Run `pip3 install cf_lines_overlap`

```
from overlap.overlap import overlap

result = overlap((1,5), (4,25))

# It will return True if the lines overlap, False otherwise
```
