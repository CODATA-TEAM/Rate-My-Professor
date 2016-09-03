# Rate-My-Professor
COde for Rate My Professor contest


# The vector use for Dataset
| id| tid| dept| forcredit| attendance| textbookuse| interest| helpcount| nothelpcount|
| ------| ------ | ------ |
| 0| 1| 2| 3| 4| 5| 6| 7| 8|

|online| profgender| profhotness| tags| grade| helpfulness| clarity |
| ------| ------ | ------ |
| 9| 10| 11| 12-31| 32| 33| 34|





暂时comment这列没有

# helpfulness predict model
| helpcount| nothelpcount| online| profgender| profhotness| tags| grade| comments| 34|
| ------| ------ | ------ |
| 7| 8| 10| 10| 11| 12-31| 32| None|

# clarity predict model
 | forcredit | attendance | textbookuse | interest | online | profgender | profhotness | tags | grade | comments
| ------| ------ | ------ |
| 3| 4| 5| 6| 9| 10| 11| 12-31|32 |None|

# 后面用的
|online| profgender| profhotness| tags| grade| comments(notused)| helpfulness| clarity |
| ------| ------ | ------ |
| 9| 10| 11| 12-31| 32| 33| 34| 35
