celebs = ("Taylor Swift", "Cristiano Ronaldo", "Trevor Noah", "Dua Lipa", "Jungkook")
ages = (36, 38, 42, 28, 27)

def build_celebrity_dict(celebs, ages):
    return {"celebs": list(celebs), "ages": list(ages)}


if __name__ == "__main__":
    celebs = ("Taylor Swift", "Christiano Ronaldo", "Trevor Noah", "Dua Lipa", "Jungkook")
    ages = (36, 38, 42, 28, 27)
    print(build_celebrity_dict(celebs, ages))
