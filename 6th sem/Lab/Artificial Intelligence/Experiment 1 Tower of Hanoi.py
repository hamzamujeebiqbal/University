def TowerOfHanoi(n,from_rod,to_rod,aux_rod):
    if n==1:
        print('Move disk 1 from rod',from_rod,'to rod',to_rod)
        return
    TowerOfHanoi(n-1,from_rod,aux_rod,to_rod)
    print('Move disk',n,'from rod',from_rod,'to rod',to_rod)
    TowerOfHanoi(n-1,aux_rod,to_rod,from_rod)

n=2
TowerOfHanoi(n,'A','C','B')
'''
we move the n-1 disk from A to B 
then last disk A  to C 
then n-1 disk from B to C 
'''
