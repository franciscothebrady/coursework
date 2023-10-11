# SI 506 Week 06

import math
import pprint

# Instantiate a custom PrettyPrinter object
pp = pprint.PrettyPrinter(indent=1, width=100, compact=True)

# fmt: off
cereals = [
    ["manufacturer", "brand", "slogan", "serving_size_gm", "sugar_gm"],
    ["Post Consumer Brands", "Honey Bunches of Oats", "Taste the joy in every spoonful.", 30, 6],
    ["General Mills", "Cocoa Puffs", "I'm cuckoo for Cocoa Puffs!", 36, 13.4],
    ["Kellogg Company", "Frosted Flakes", "They're Gr-r-reat!", 41, 14.5],
    ["General Mills", "Honey Nut Cheerios", "Have a Change of Heart", 28, 9],
    ["Post Consumer Brands", "Grape-nuts", "Ever eat a pine tree? Many parts are edible.", 29, 4.4],
    ["Kellogg Company", "Raisin Bran", "Two scoops of raisins in every box.", 59, 18],
    ["General Mills", "Cheerios", "Go with the Goodness of Cheerios.", 28, 1.3],
    ["Kellogg Company", "Fruit Loops", "Follow my nose. It always knows.", 39, 12],
    ["Post Consumer Brands", "Shredded Wheat", "Bet you can't eat three.", 50, 0.46],
    ["UMSI Kitchens", "Data morsels", "Information changes everything.", 50, 0.46],
    ["Three Wishes Foods", "Honey grain free cereal", "So Good It Should Be Forbidden.", 35, 3],
    ["General Mills", "Lucky Charms", "They're magically delicious.", 36, 13],
    ["Quaker Oats Company", "Cap'n Crunch", "It's got corn for crunch, oats for punch, and it stays crunchy, even in milk.", 27, 12],
    ["Post Consumer Brands", "Fruity Pebbles", "They're Yabba-Dabba-Delicious!", 27, 9.3],
    ["Kellogg Company", "Corn Flakes", "Wake up, up, up to Kellogg's Cornflakes!", 29, 10],
    ["Kellogg Company", "Apple Jacks", "We eat what we like.", 28, 8],
    ["General Mills", "Wheaties", "The Breakfast of Champions", 27, 4.1],
]
# fmt: on

# 1.1 DEFINING A FUNCTION

# print("\n1.1 Print slogan")

# TODO Implement function

# TODO Uncomment

# frosted_flakes = cereals[3]
# print_slogan(frosted_flakes) # Call function and pass argument


# 1.2 RETURN VALUE

# TODO Implement function


# TODO Uncomment
# raisin_bran = cereals[6]
# raisin_bran_slogan = get_slogan(raisin_bran)
# print(f"\n1.2 Slogan = {raisin_bran_slogan}")


# 1.3 MULTIPLE PARAMETERS


def format_slogan(name, slogan):
    return f"{name}: {slogan}"


# Positional arguments (order correct)
# TODO Uncomment
# wheaties_slogan = format_slogan(cereals[-1][1], cereals[-1][2])
# print(f"\n1.3 {wheaties_slogan}")


# 1.4 ARGUMENT ORDER MATTERS (PASSED POSITIONALLY)

# Postional arguments (order incorrect)
apple_jacks_slogan = format_slogan(cereals[-2][2], cereals[-2][1])  # Oops! string reversed
# TODO Uncomment
# print(f"\n1.4 {apple_jacks_slogan}")


# 1.5 CHALLENGE 01


def get_cereals_by_company(cereal_brands, company):
    brands = []
    for cereal in cereal_brands:
        pass  # TODO Add if statement
    return brands


post_cereals = None  # TODO Call function
kellogg_cereals = None  # TODO Call function

# TODO Uncomment
# print(f"\n1.5.1 Post cereals = {post_cereals}")
# print(f"\n1.5.2 Kellogg's cereals = {kellogg_cereals}")


# 2.1 KEYWORD ARGUMENTS (ANY ORDER ACCEPTABLE)

# TODO Uncomment and replace NoneType instances with keyword arguments
# general_mills_cereals = get_cereals_by_company(None, None)

# TODO Uncomment
# print(f"\n2.1 General Mills cereals = {general_mills_cereals}")


# 2.2 OPTIONAL PARAMETERS


def calculate_sugar_content(cereal_brand, precision=2):
    return round(cereal_brand[-1] / cereal_brand[-2], precision)


def get_cereal(cereal_brands, cereal_name):
    for cereal in cereal_brands:
        if cereal_name.lower() in cereal[1].lower():
            return cereal  # match, exit loop immediately


# Retrieve cereal
cocoa_puffs = get_cereal(cereals[1:], "Cocoa Puffs")

# Accept precision default value
cocoa_puffs_sugar = None  # TODO call function
# print(f"\n2.2.1 Cocoa Puffs sugar content = {cocoa_puffs_sugar}")

# Override precision default value
cocoa_puffs_sugar = None  # TODO call function
# print(f"\n2.2.2 Cocoa Puffs sugar content = {cocoa_puffs_sugar}")


# 2.3 Skipping optional parameters


def calculate_sugar_content_v2(cereal_brand, precision=2, format_pct=False):
    if format_pct:
        return f"{cereal_brand[-1] / cereal_brand[-2] * 100:.{precision}f}%"  # trailing % sign
    else:
        return round(cereal_brand[-1] / cereal_brand[-2], precision)


# TODO Uncomment
# raisin_bran = get_cereal(cereals[1:], "raisin bran")

# The boolean True (numerical value 1) binds to wrong parameter; returns string
# TODO Uncomment
# raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, True)

# print(f"\n2.3.1 Raisin Bran sugar content (type={type(raisin_bran_sugar)}) = {raisin_bran_sugar}")

# Keyword argument binds 3 correctly, returns float
# TODO Uncomment
# raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, precision=3)
# print(f"\n2.3.2 Raisin Bran sugar content (type={type(raisin_bran_sugar)}) = {raisin_bran_sugar}")

# Returns formatted string
# TODO Uncomment
# raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, format_pct=True, precision=3)

# raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, True, 3) # Alternative
# print(f"\n2.3.3 Raisin Bran sugar content (type={type(raisin_bran_sugar)}) = {raisin_bran_sugar}")


# 2.4 CHALLENGE 02


def get_cereal_attribute(cereal, headers, header="brand"):
    pass  # TODO Implement


headers = cereals[0]  # extract headers
corn_flakes = None  # TODO Call function
corn_flakes_serving_size_gm = None  # TODO Call function
# print(f"\n2.4 Corn Flakes serving size = {corn_flakes_serving_size_gm} gm")


# 3.0 PASSING FUNCTIONS CALLS AS ARGUMENTS


def calculate_sugar_content_v3(serving_size_gm, sugar_gm, precision=2, format_pct=False):
    if format_pct:
        return f"{sugar_gm / serving_size_gm * 100:.{precision}f}%"  # trailing % sign
    else:
        return round(sugar_gm / serving_size_gm, precision)


# TODO Uncomment
# cereal = get_cereal(cereals[1:], "Grape-nuts")
# serve_size_gm = get_cereal_attribute(cereal, headers, "serving_size_gm")
# sugar_gm = get_cereal_attribute(cereal, headers, "sugar_gm")
# sugar_content = calculate_sugar_content_v3(serve_size_gm, sugar_gm, precision=3, format_pct=True)
# print(f"\n3.0.1 Sugar content = {sugar_content}")

# Alternative (nested function calls)
# cereal = get_cereal(cereals[1:], "Grape-nuts")
# sugar_content = calculate_sugar_content_v3(
#     get_cereal_attribute(cereal, headers, "serving_size_gm"),
#     get_cereal_attribute(cereal, headers, "sugar_gm"),
#     precision=3,
#     format_pct=True
# )
# print(f"\n3.0.2 Sugar content = {sugar_content}")

# sugar_content = calculate_sugar_content_v3(
#     get_cereal_attribute(get_cereal(cereals[1:], "Grape-nuts"), headers, "serving_size_gm"),
#     get_cereal_attribute(get_cereal(cereals[1:], "Grape-nuts"), headers, "sugar_gm"),
#     precision=3,
#     format_pct=True
# )
# print(f"\n3.0.3 Sugar content = {sugar_content}")


# 4.0 VARIABLE SCOPE

# TODO Uncomment
# print(f"\n4.0.1 Globally-scoped variable cereals = {cereals[:2]}")

# TODO Uncomment. Triggers a NameError runtime exception.
# print(f"\n4.0.2 Locally-scoped variable brands = {brands}")


# 5.0 FUNCTIONS CAN CALL OTHER FUNCTIONS

# fmt: off
cereal_ingredients = [
    ["manufacturer", "brand", "ingredients"],
    ["Kellogg Company", "Frosted Flakes", ("Milled Corn", "Sugar", "Malt Flavoring", "High Fructose Corn Syrup", "Salt")],
    ["Kellogg Company", "Raisin Bran", ("Whole Grain Wheat", "Raisins", "Wheat Bran", "Sugar", "High Fructose Corn Syrup")],
    ["General Mills", "Cheerios", ("Whole Grain Oats", "Modified Corn Starch", "Sugar", "Salt")],
    ["General Mills", "Cocoa Puffs", ("Whole Grain Corn", "Sugar", "Corn Syrup", "Cornmeal", "Canola and or Rice Bran Oil")],
    ["General Mills", "Lucky Charms", ("Oats", "Marshmallows", "Sugar", "Corn Syrup", "Corn Starch")],
    ["Post Consumer Brands", "Shredded Wheat (original spoon size)", ("Whole Grain Wheat",)],
    ["Post Consumer Brands", "Grape-nuts", ("Whole Grain Wheat", "Flour", "Malted Barley Flour", "Salt", "Dried Yeast")]
    ]
# fmt: on


def has_ingredient(ingredients, ingredient):
    for item in ingredients:
        if ingredient.lower() in item.lower():
            return True  # exit function; terminates loop
    return False


def get_cereals_by_ingredient(cereals, ingredient):
    results = []
    for cereal in cereals:
        pass  # TODO Add if statement
    return results


# TODO Uncomment
# corn_syrup = get_cereals_by_ingredient(cereal_ingredients[1:], "corn syrup")
# print(f"\n5.0 Cereals w/corn syrup = {corn_syrup}")


# 5.1 CHALLENGE 03


def get_lowest_sugar_content(cereals, headers):
    min_sugar_content = []
    min_sugar_gm = None  # Add start value
    for cereal in cereals:
        brand = None # TODO Call function
        serving_size_gm = None # TODO Call function
        sugar_gm = None # TODO Call function
        sugar_content = None  # TODO call function (return number not percent)

        # TODO Uncomment and fix
        # if sugar_content ??? min_sugar_gm:
        #     min_sugar_gm = None # Assign value
        #     min_sugar_content.clear() # reset
        #     min_sugar_content.append(brand) # cereal name only
        # elif sugar_content ??? min_sugar_gm:
        #     min_sugar_content.append(brand) # cereal name only

    return min_sugar_content


min_sugar_cereals = get_lowest_sugar_content(cereals[1:], headers)
# TODO Uncomment
# print(f"\n5.1 Cereal min sugar content = {min_sugar_cereals}")


# 6.0 TRUTH VALUES


def get_truth_value(val):
    return bool(val)  # check's the object's truth value


fruity_pebbles = None
truth_value = get_truth_value(fruity_pebbles)  # falsy

# TODO Uncomment
# print(f"\n6.0.1 None truth value = {truth_value}")

fruity_pebbles = []
truth_value = get_truth_value(fruity_pebbles)  # falsy

# TODO Uncomment
# print(f"\n6.0.2 Empty list truth value (length={len(fruity_pebbles)}) = {truth_value}")

fruity_pebbles = ["Post Consumer Brands", "Fruity Pebbles", 27, 9.3]
truth_value = get_truth_value(fruity_pebbles)  # truthy

# TODO Uncomment
# print(f"\n6.0.3 List truth value (length={len(fruity_pebbles)}) = {truth_value}")


# Test a function call's truth value
def has_cereal(cereals, cereal_brand):
    if get_cereal(cereals, cereal_brand):
        return True
    else:
        return False


# Alternative
def has_cereal(cereals, cereal_brand):
    if get_cereal(cereals, cereal_brand):
        return True
    return False


# TODO Uncomment
# has_golden_grahams = has_cereal(cereals, "Golden Grahams")
# print(f"\n6.0.4 Has Golden Grahams = {has_golden_grahams}")


# 7.0 ITERABLE PACKING AND UNPACKING

# Packing
shredded_wheat = ["Post Consumer Brands", "Shredded Wheat", "Bet you can’t eat three.", 49, 0.4]
# Equivalent
# shredded_wheat = get_cereal(cereals[1:], "shredded wheat")

# Unpacking
manufacturer, cereal_brand, slogan, serving_size_gm, sugar_gm = shredded_wheat

# TODO Uncomment
# print(f"\n7.0 Shredded Wheat unpacked:",
#     f"\nmanufacturer = {manufacturer}",
#     f"\ncereal_brand = {cereal_brand}",
#     f"\nslogan = {slogan}",
#     f"\nserving_size_gm = {serving_size_gm}",
#     f"\nsugar_gm = {sugar_gm}")

# ValueError runtime exceptions triggered

# Triggers ValueError: too many values to unpack (expected 4)
# TODO Uncomment
# manufacturer, cereal_brand, slogan, sugar_gm = shredded_wheat

# Triggers ValueError: not enough values to unpack (expected 6, got 5)
# TODO Uncomment
# manufacturer, cereal_brand, slogan, serving_size_gm, sugar_gm, rating = shredded_wheat

# Variables ordered incorrectly
# TODO Uncomment
# slogan, cereal_brand, manufacturer, sugar_gm, serving_size_gm = shredded_wheat

# print(f"\n7.1 Shredded Wheat unpacked into wrong variables:",
#     f"\nmanufacturer = {manufacturer}",
#     f"\ncereal_brand = {cereal_brand}",
#     f"\nslogan = {slogan}",
#     f"\nserving_size_gm = {serving_size_gm}",
#     f"\nsugar_gm = {sugar_gm}")


# 7.2 UNPACKING IN A FOR LOOP

# Conventional unpacking
# TODO Uncomment
# print("\n7.2.1 for loop unpacking")
# for cereal in cereals[1:5]:
#     manufacturer, brand, slogan, serving_size_gm, sugar_gm = cereal
#     print(
#         f"\nmanufacturer: {manufacturer}",
#         f"\nBrand: {brand}",
#         f"\nSlogan: {slogan}",
#         f"\nSugar content: {calculate_sugar_content_v3(serving_size_gm, sugar_gm)}"
#     )

# Also an option
# TODO Uncomment
# print("\n7.2.2 for loop unpacking")
# for manufacturer, brand, slogan, serving_size_gm, sugar_gm in cereals[-4:]:
#     print(
#         f"\nmanufacturer: {manufacturer}",
#         f"\nBrand: {brand}",
#         f"\nSlogan: {slogan}",
#         f"\nSugar content: {calculate_sugar_content_v3(serving_size_gm, sugar_gm)}"
#     )


# 8.0 CHALLENGES

# fmt: off
cereal_ratings_data = [
    ["manufacturer", "brand", "five_stars", "four_stars", "three_stars", "two_stars", "one_star"],
    ["Kellogg Company", "Apple Jacks", 185, 21, 10, 4, 2],
    ["Quaker Oats Company", "Cap'n Crunch", 49, 5, 3, 1, 1],
    ["Quaker Oats Company", "Cap'n Crunch's Crunch Berries", 196, 15, 6, 2, 4],
    ["General Mills", "Cheerios", 1310, 95, 14, 11, 28],
    ["General Mills", "Cinnamon Toast Crunch", 577, 46, 10, 5, 19],
    ["General Mills", "Cocoa Puffs", 147, 9, 1, 2, 5],
    ["Kellogg Company", "Corn Flakes", 467, 45, 9, 3, 10],
    ["Kellog Company", "Frosted Flakes", 1465, 116, 37, 11, 35],
    ["Kellogg Company", "Frosted Mini-Wheats", 883, 95, 18, 6, 26],
    ["Kellogg Company", "Fruit Loops", 750, 84, 14, 6, 8],
    ["Post Consumer Brands", "Fruity Pebbles", 170, 23, 8, 2, 7],
    ["Post Consumer Brands", "Grape-Nuts", 322, 25, 3, 1, 15],
    ["Post Consumer Brands", "Honey Bunches of Oats", 95, 7, 3, 1, 2],
    ["General Mills", "Honey Nut Cheerios", 814, 64, 22, 8, 22],
    ["General Mills", "Lucky Charms", 388, 38, 12, 3, 7],
    ["Kellogg Company", "Raisin Bran", 946, 79, 21, 14, 30],
    ["General Mills", "Reese's Puffs", 184, 14, 10, 4, 3],
    ["Kellogg Company", "Rice Krispies", 429, 31, 11, 5, 13],
    ["Post Consumer Brands", "Shredded Wheat", 208, 13, 6, 5, 11],
    ["General Mills", "Wheaties", 215, 18, 5, 2, 12],
]
# fmt: on

cereal_ratings_headers = cereal_ratings_data[0]
cereal_ratings = cereal_ratings_data[1:]


# 8.1 CHALLENGE 04


def get_ratings(cereal):
    pass  # TODO return rating numbers as a list


raisin_bran = None  # TODO Call get_cereal(), pass keyword arguments in reverse order
raisin_bran_ratings = None  # TODO call function

# Print
# TODO Uncomment
# brand = {get_cereal_attribute(raisin_bran, cereal_ratings_headers, 'brand')}
# print(f"\n8.1 {brand} ratings = {raisin_bran_ratings}")


# 8.2 CHALLENGE 05

rating_groups = []
for cereal in cereal_ratings:
    # TODO Unpack ratings into five variables

    # Group ratings
    favorable = None  # TODO Add rating values
    neutral = None  # TODO Add rating value
    unfavorable = None  # TODO Add rating values

    # Build string
    brand = get_cereal_attribute(cereal, cereal_ratings_headers, "brand")
    # TODO Add variables
    string = f"{None} ratings: favorable={None}, neutral={None}, unfavorable={None}"
    rating_groups.append(string)

# TODO Uncomment
# print(f"\n8.2 Rating groups (n={len(rating_groups)})")
# pp.pprint(rating_groups)


# 8.3 CHALLENGE 06


# Part of setup
def count_ratings(ratings):
    count = 0
    for rating in ratings:
        pass  # TODO Increment
    return count


def calculate_favorable_rating_pct(cereal):
    ratings = None  # Call get_ratings()
    fav_pct = (0 / 1) * 100  # TODO Fix arithmetic equation
    return fav_pct


honey_nut_cheerios = get_cereal(cereal_ratings, "honey nut cheerios")
honey_nut_cheerios_fav_pct = None  # Call function

# Print
# TODO Uncomment
# brand = get_cereal_attribute(honey_nut_cheerios, cereal_ratings_headers, 'brand')
# print(f"\n8.3 {brand} favorability rating = {honey_nut_cheerios_fav_pct:.2f}%")
