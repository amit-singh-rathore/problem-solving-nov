def get_prime_pos(number):
    is_prime_seq = [0]*(number+1)
    is_prime_seq[0] = -1
    is_prime_seq[1] = -1
    
    pos_in_pseries = 0
    for i in range(2, number+1):
        if is_prime_seq[i]==0:
            pos_in_pseries += 1
            is_prime_seq[i] = pos_in_pseries
            for j in range(i*2, number+1, i):
                if is_prime_seq[j] != -1:
                    is_prime_seq[j] = -1
                
    return is_prime_seq[number]

        
for number in [2,3,5,7,11,13,17,19,23,29,31,37,41,47, 53]:
    print(get_prime_pos(number))