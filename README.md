
# mathematical-modeling

Leslie模型人口预测

Leslie Model Population Forecast.
<!-- ****
	
|Author|winkemoji|
|---|---
|E-mail|1321807986@qq.com


**** -->
需引入的包
```python
import numpy as np
import matplotlib.pyplot as plt
import csv
```



* 输入
    * woman_population      当年各个年龄女性人数
    * birth_rate            当年各个年龄女性生育率
    * survival_rate         当年各个年龄女性存活率
    * year                  迭代年数
    * begin_year            初始年份
    * sex_ratio             性别比


* 输出
    * total_population      历年人口总数
    * aging_rate            老龄化比率