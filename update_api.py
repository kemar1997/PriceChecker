def _to_ascii(s):
	if isinstance(s, str):
		return s.encode('ascii')
	else:
		return s
