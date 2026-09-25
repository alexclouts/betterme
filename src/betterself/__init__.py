import re

def main():
	print("Hello betterself!")

def feels_good():
	return True

def total_calories(fat, protein, carbs):
	return fat * 9 + protein * 4 + carbs * 4

def calories_per_gram(calories, food_weight):
	return calories / food_weight

def is_strong_password(password):
	return (
		len(password) >= 8
		and any(character.isupper() for character in password)
		and any(character.islower() for character in password)
		and any(character.isdigit() for character in password)
		and any(not character.isalnum() for character in password)
	)

def is_valid_email(email):
	email_pattern = r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$"
	return re.fullmatch(email_pattern, email) is not None


