
import sae.kvdb

class Counter():
    def __init__(self, name):
    	self.name = name
    	self.kv_client = sae.kvdb.Client()

    def increase(self):
    	count = self.kv_client.get(self.name)
    	if count == None:
    		count = 0

    	count += 1

    	self.kv_client.set(self.name, count)

    	return count

    def get(self):
    	return self.kv_client.get(self.name)

    def reset(self):
    	self.kv_client.set(self.name, 0)