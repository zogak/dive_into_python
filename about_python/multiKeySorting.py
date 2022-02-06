school = [
	[1, 1, 51],
	[2, 1, 53],
	[1, 2, 56],
	[1, 2, 52],
	[2, 1, 52],
	[2, 1, 51],
	[1, 2, 53]
]

a = sorted(school, key = lambda x : x[0]) #학년 정렬
b = sorted(school, key = lambda x : (x[0], x[1], x[2]))