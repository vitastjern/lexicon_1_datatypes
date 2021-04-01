# As a young adventurer, you travel with your party around the world, seeking for 
# gold and glory. But you need to split the profit among your companions. 
#
# You will receive a party size. After that you receive the days of the adventure. 
#
# Every day, you are earning 50 coins, but you also spent 2 coin per companion for food. 
#
# Every 3rd (third) day, you have a motivational party, spending 3 coins per companion for 
# drinking water. 
# 
# Every 5th (fifth) day you slay a boss monster and you gain 20 coins per companion. 
# But if you have a motivational party the same day, you spent additional 2 coins per 
# companion. 
# 
# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, but 
# every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
# You have to calculate how much coins gets each companion at the end of the adventure.

party_size = int(input())
days = int(input())

coin_purse = 0

for day in range(1, days+1):
    # party size changes during the morning
    if divmod(day, 10)[1] == 0: # every 10 days, 2 leaves
        party_size -= 2
    
    if divmod(day, 15)[1] == 0: # every 15 days, 5 joins
        party_size += 5

    coin_purse += 50  # every day earning
    coin_purse -= 2 * party_size # every day spending

    if divmod(day, 3)[1] == 0: # motivational party every 3 days! 
        coin_purse -= (3 * party_size)  # buy water

    if divmod(day, 5)[1] == 0: # slay a boss! 
        coin_purse += 20 * party_size  # 20 coins per party member!
        if divmod(day, 3)[1] == 0: # since it is motivation day, party harder!
            coin_purse -= 2 * party_size
    

print(str(party_size) + " companions received " + str(divmod(coin_purse, party_size)[0]) + " coins each.")
