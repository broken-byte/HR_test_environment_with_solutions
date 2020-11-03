def whatFlavors(cost: list, money: int, ) -> list:
    hash_table: dict = {}
    optimal_flavor_choices: list = []
    for index, ice_cream_price in enumerate(cost):
        difference: int = money - ice_cream_price
        if difference in hash_table:
            optimal_flavor_choices.append(hash_table[difference])
            optimal_flavor_choices.append(index + 1)
            optimal_flavor_choices.sort()
            print(optimal_flavor_choices[0], optimal_flavor_choices[1])
        hash_table[ice_cream_price] = index + 1
