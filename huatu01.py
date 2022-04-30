import numpy as np
import matplotlib.pyplot as plt

# this sets up the Matplotlib interactive windows:
%matplotlib widget

# this changes the default date converter for better interactive plotting of dates:
plt.rcParams['date.converter'] = 'concise'


import matplotlib.pyplot as plt
import numpy as np
data = np.arange(10)
data
plt.plot(data)