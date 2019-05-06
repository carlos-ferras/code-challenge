## Ormuco Code Challenge

This project has been created only for demonstration purpose.
>
> ### The challenge
>
> The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
>


### The Answer

- Run `pip3 install cf_compare_versions`

usage: 
```
from compare_versions.compare_versions import compare_versions

result = compare_versions('1.0.0.2.9', '1.0.0.3.4')

# It will return:
#     A positive number: If the first version is greater than the second  
#     A negative number: If the first version is smaller than the second
#     Zero: If the versions are equals
```
