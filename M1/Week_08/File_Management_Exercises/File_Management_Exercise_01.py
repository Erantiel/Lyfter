def create_initial_file():
    text = 'Whispers in the Dark: A Dreadful Lullaby\nDreadful Dreams Under a Blood Moon\nShadows of Despair: The Dreadful Truth\nCursed Chords: The Soundtrack of Dread\nEchoes of Fear: A Dreadful Melody\n' 
    with open('songs.txt', 'w') as file:
        file.write(text)


def read_file():
    with open('songs.txt', 'r') as file:
        return file.readlines()


def sort_file(existing_file):
    existing_file.sort()
    return existing_file


def create_new_file(list):
    with open('output.txt', 'w') as file:
        for line in list:
            file.write(line)


def main():
    create_initial_file()
    create_new_file(sort_file(read_file()))
    
    with open('songs.txt', 'r') as file1:
        print(file1.read())

    with open('output.txt', 'r') as file2:
        print(f'\n{file2.read()}')


main()