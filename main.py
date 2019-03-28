import mistune

import ipdb
# ipdb.set_trace()

with open('learn.md', 'r') as file:
	# print(file.read())
	print(mistune.markdown(file.read()))
# result = mistune.markdown('I am using **mistune markdown parser**')

# print(result)