import mistune

import ipdb

with open('learn.md', 'r') as file:
	# print(file.read())

	# ipdb.set_trace()
	res = mistune.markdown(file.read())
	print(res)
# result = mistune.markdown('I am using **mistune markdown parser**')

# print(result)