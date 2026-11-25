import os

LINE = ("My fridge hums all night like it's guarding a fortune, but open the door and the only treasure inside is a ketchup bottle older than my last relationship.")

def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
