import re

query = "from property1=value1 and property2=value2 update value'
# want to parse expression into
# property1
# value1
# if we are using and
# property2
# value2
# update value
