tph = False
t = 285
p = 165
h = 143
num = 40755

def hex_calc(hc):
	return hc * (2 * hc - 1)
	
def pent_calc(pc):
	return (pc * (3 * pc - 1)) / 2
	
def tri_calc(tc):
	return (tc * (tc + 1)) / 2

while tph == False:
	h += 1
	while pent_calc(p) < hex_calc(h):
		p += 1
	while tri_calc(t) < hex_calc(h):
		t += 1
	if tri_calc(t) == pent_calc(p) == hex_calc(h):
		tph = True
	print hex_calc(h)
	print pent_calc(p)
	print tri_calc(t)
		
print tri_calc(t)