"""
ItemShops configurator for BossShopPro
by workonfire
"""

from colors import color_text

print(color_text('green', 'back', "ItemShops configurator for BossShopPro"))
print(color_text('green', 'none', "by workonfire"))
print("\n")

category = input("Category: ")
with open(category.lower() + '.yml', 'a') as category_file:
    category_file.write('ShopName: ' + category + "\n" +
                        'DisplayName: ' + category + " (%page%/%maxpage%)" + "\n" +
                        'Command: ' + category.lower() + "\n" +
                        'itemshop:' + "\n"
                        )

while True:
    item = input(color_text('cyan', 'none', "Item: "))
    price_buy = input(color_text('red', 'bright', "Buy ($): "))
    reward_sell = input(color_text('green', 'bright', "Sell ($): "))
    try:
        with open(category.lower() + '.yml', 'a') as category_file:
            category_file.write('  ' + item + ':' + "\n" +
                                '    ' + 'PriceBuy: ' + str(float(price_buy)) + "\n" +
                                '    ' + 'RewardSell: ' + str(float(reward_sell)) + "\n" +
                                '    ' + 'AllowBuyAll: false' + "\n" +
                                '    ' + 'AllowSellAll: true' + "\n" +
                                '    ' + 'Item: ' + "\n" +
                                '    ' + '- type:' + item.upper() + "\n" +
                                '    ' + '- amount:64' + "\n"
                                )
    except ValueError:
        print(color_text('red', 'none', "Please enter the correct values."))
    print("\n>>> NEXT\n")