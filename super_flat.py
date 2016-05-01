def flatten(d, parent_key='', sep='.'):
	"""
	TODO
	"""
	items = []
	for k, v in d.items():
		new_key = parent_key + sep + k if parent_key else k
		if isinstance(v, collections.MutableMapping):
			items.extend(flatten(v, new_key, sep=sep).items())
		elif isinstance(v, list):
			for elem in v:
				if isinstance(elem, (collections.MutableMapping, list)):
					items.extend(flatten(elem, new_key, sep=sep).items())
				else:
					list_key = new_key + sep + str(v.index(elem))
					items.append((list_key, elem))
		else:
			items.append((new_key, v))
	return dict(items)
