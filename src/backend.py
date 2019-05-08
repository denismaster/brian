def main():
    while True:
        raw_input = input();
        if raw_input == '/q':
            return
        else:
            words = raw_input.split()
            print(words)

main()