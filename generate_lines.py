with open(".\\new_file.txt", "w") as f:
    a = 1
    while True:
        f.write(f'Line {a}\n')
        a += 1
