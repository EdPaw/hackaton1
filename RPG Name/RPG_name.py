import random
import requests
from PIL import Image
from io import BytesIO

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
CONSONANTS = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')
ROMAN_NUMBERS = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X")
SURNAMES = ("the Brave", "the Wise", "the Strong", "the Just", "the Noble", "the Fearless", "the Great", "the Mighty", "the Cunning", "the Merciless")
IMAGE_URLS = [
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ebc8c25d-c0c6-492e-9d51-fc7353d7dbd5/dftcno1-7584cee6-87ed-4850-91db-a0c74fbb03fa.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2ViYzhjMjVkLWMwYzYtNDkyZS05ZDUxLWZjNzM1M2Q3ZGJkNVwvZGZ0Y25vMS03NTg0Y2VlNi04N2VkLTQ4NTAtOTFkYi1hMGM3NGZiYjAzZmEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.320M12sUD-Yl9DXx2QdluwyKFhP68C_6LVpsRFdKldU",
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ebc8c25d-c0c6-492e-9d51-fc7353d7dbd5/d4prdul-e54ca05b-acac-43e8-a1a0-2ca6605fe64e.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2ViYzhjMjVkLWMwYzYtNDkyZS05ZDUxLWZjNzM1M2Q3ZGJkNVwvZDRwcmR1bC1lNTRjYTA1Yi1hY2FjLTQzZTgtYTFhMC0yY2E2NjA1ZmU2NGUuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.XTyIn158WGm_cWcCsHShAIjvFjXfvZtbm7FOsmr8EaM",
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ebc8c25d-c0c6-492e-9d51-fc7353d7dbd5/deci7ji-08f7dd30-d3b1-43d0-a073-13ad21210402.jpg/v1/fill/w_900,h_1274,q_75,strp/tomas_memeverso_by_ff69_deci7ji-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI3NCIsInBhdGgiOiJcL2ZcL2ViYzhjMjVkLWMwYzYtNDkyZS05ZDUxLWZjNzM1M2Q3ZGJkNVwvZGVjaTdqaS0wOGY3ZGQzMC1kM2IxLTQzZDAtYTA3My0xM2FkMjEyMTA0MDIuanBnIiwid2lkdGgiOiI8PTkwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.ErEA51ZRvCwBKiFZ1rLjVuJH61lopWuZ4O31TLUQz-Y",
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ebc8c25d-c0c6-492e-9d51-fc7353d7dbd5/dem005n-915a4a0c-de2d-4793-ae82-b1ea292be501.jpg/v1/fill/w_1024,h_1000,q_75,strp/female_warrior_by_ff69_dem005n-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTAwMCIsInBhdGgiOiJcL2ZcL2ViYzhjMjVkLWMwYzYtNDkyZS05ZDUxLWZjNzM1M2Q3ZGJkNVwvZGVtMDA1bi05MTVhNGEwYy1kZTJkLTQ3OTMtYWU4Mi1iMWVhMjkyYmU1MDEuanBnIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.wjECjnHmzZuaILglFfdXpPq4-kBYJmhyacky6O56fvk",
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ebc8c25d-c0c6-492e-9d51-fc7353d7dbd5/dfqzx07-7087dcac-93c8-4964-88b0-1a9529a967bb.png/v1/fill/w_900,h_1198,q_80,strp/elf_by_ff69_dfqzx07-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTE5OCIsInBhdGgiOiJcL2ZcL2ViYzhjMjVkLWMwYzYtNDkyZS05ZDUxLWZjNzM1M2Q3ZGJkNVwvZGZxengwNy03MDg3ZGNhYy05M2M4LTQ5NjQtODhiMC0xYTk1MjlhOTY3YmIucG5nIiwid2lkdGgiOiI8PTkwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.U-hwWngt8pAXoFhOtxwEp4zxQ2A45vsluUs_e1jkC9o"
]


def how_long_is_name():
    long = random.randrange(2, 6)
    return long


def generate_name(long):
    length = 0
    name = ""

    what_first = random.choice(["V", "C"])

    while length != long:
        vowel = random.choice(VOWELS)
        consonant = random.choice(CONSONANTS)

        if what_first == "V":
            pair = vowel + consonant
        else:
            pair = consonant + vowel
        name += pair
        length += 1

    return name.capitalize()


def generate_num():
    num = random.choice(ROMAN_NUMBERS)
    return num


def generate_surname():
    surname = random.choice(SURNAMES)
    return surname


def connect_name_parts(how_long):
    hero_name = f"{generate_name(how_long)} {generate_num()} {generate_surname()}"
    return hero_name


def display_random_image():
    random_url = random.choice(IMAGE_URLS)
    response = requests.get(random_url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    image.show()


def main():

    long = how_long_is_name()
    name = connect_name_parts(long)
    print(name)
    display_random_image()


main()
