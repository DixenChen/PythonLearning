import io

try:
    with open('sample.txt', 'r') as file1:
        content = file1.read()
        print(content)

        buffer = io.StringIO(content)
        topic = buffer.readline().strip()
        print(f"subject: '{topic}'")
        buffer.close()

        file1.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")