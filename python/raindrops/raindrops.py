def raindrops(number):
    answer = ''
    factors = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    for i in factors:
        if number % i == 0:
            answer += factors[i]
    if answer == '':
        return str(number)
    return answer