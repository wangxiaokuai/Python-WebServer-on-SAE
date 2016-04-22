

import os
import json

# A LocalStorage Object saves data in a json file
# It get data from the file and set data to the file
# The data format is in json, and the value of an item is string or number
# It's a little key-value database
# 
# localStorage.json format:
# {
#	  "xxx.github.com": 300
# }
class LocalStorage():
	def __init__(self):
		filename = "localStorage.json"

		path = os.getcwd()
		self.filename = os.path.join(path, filename)

		def is_json_like(filename):
			with open(filename) as fp:
				data = fp.read()
				try:
					json.loads(data)
				except:					
					return False

				return True

		if os.path.exists(self.filename) and not is_json_like(self.filename):
			print "remove %s." % self.filename
			os.remove(self.filename)

		if not os.path.exists(self.filename):			# create the initial file; the file is always be a json file
			data = "{}"
			with open(self.filename, "wb") as fp:
				fp.write(data)

			os.chmod(self.filename, stat.S_IRWXU|stat.S_IRGRP|stat.S_IROTH) # mode:777

	def get(self, key, default = None):
		with open(self.filename, "rb") as fp:			# read, increase and write back
			str_data = fp.read()
			self.data = json.loads(str_data)

			if key in self.data:
				return self.data[key]
			else:
				return default

	def getNumber(self, key, default = None):
		value = self.get(key, default)
		return int(value)

	# add or update the key into the json file
	def set(self, key, value):							
		with open(self.filename, "rb+") as fp:
			str_data = fp.read()
			self.data = json.loads(str_data)
			self.data[key] = value
			new_str = json.dumps(self.data)
			fp.seek(0)
			fp.write(new_str)

	def setNumber(self, key, value):
		self.set(key, str(value))


# A Counter object will record the data in the global file
# It can be created many times
# The name is the key of the data
# If the name is already existed, the Counter wile read the value,
# else the name is created and the value is initially 0.
class Counter():
    def __init__(self, name):
    	self.name = name
    	self.value = LocalStorage()

    def increase(self):
    	count = self.value.getNumber(self.name, 0)
    	count += 1

    	self.value.setNumber(self.name, count)

    	return count

    def get(self):
    	return self.value.getNumber(self.name)

    def reset(self):
    	self.value.setNumber(self.name, 0)



def testLocalStorage():
	ls = LocalStorage()
	value = ls.get("wangxiaokuai.github.io", 0)
	print value								# 0, 1

	ls.set("wangxiaokuai.github.io", value + 1)
	print ls.get("wangxiaokuai.github.io")	# 1, 2


	print ls.data							# {"wangxiaokuai.github.io": run times}


def testCounter():
	my_counter = Counter("wangxiaokuai.github.io")    	

	my_counter.increase()
	print my_counter.get()

if __name__ == "__main__":

	testCounter()	