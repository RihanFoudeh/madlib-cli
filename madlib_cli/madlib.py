import re


def read_template(Filepath):
    try:
        with open(Filepath)as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("file not found")


def parse_template(text: str):
    items = []
    Striped_word = re.sub(r'\{.*?\}', '{}', text)
    reslt = re.findall(r'\{.*?\}', text)
    for i in reslt:
        items.append(i.strip("{ }"))
    items = tuple(items)
    return Striped_word, items


def merge(text: str, items: tuple):
    mergedText = text.format(*items)
    return mergedText


def write_new_file(content: str):
    with open('assets/make_me_a_video_game_result.txt', 'w') as potato:
        potato.write(content)


if __name__ == "__main__":
    print("Welcome to Madlib Game")
    print("lets start the game with adding some words:")
    wordLst = []
    text = read_template("assets/make_me_a_video_game_template.txt")
    Striped_word, items = parse_template(text)
    for i in range(0, len(items)):
        inp = input(f'type a {items[i]}  ')
        wordLst.append(inp)
    wordLst = tuple(wordLst)
    mergedText = merge(Striped_word, wordLst)
    print(mergedText)
    write_new_file(mergedText)
