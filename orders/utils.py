import string
import random

def unique_order_id_generator(size=10,char=string.ascii_lowercase+string.digits):
	return "".join(random.choice(char) for _ in range(size))
