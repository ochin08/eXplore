





# 1. 'w' – Write mode (create or overwrite)
with open("sample.txt", "w") as f:
    f.write("Ito ay mula sa 'w' mode.\n")

# 2. 'r' – Read mode
with open("sample.txt", "r") as f:
    content = f.read()
    print("r mode content:\n", content)

# 3. 'a' – Append mode
with open("sample.txt", "a") as f:
    f.write("Idinagdag ito gamit ang 'a' mode.\n")

# 4. 'r' again to show appended content
with open("sample.txt", "r") as f:
    content = f.read()
    print("After append:\n", content)

# 5. 'x' – Create mode (will raise error if file exists)
try:
    with open("created_by_x.txt", "x") as f:
        f.write("Bagong file gamit ang 'x' mode.\n")
    print("File 'created_by_x.txt' successfully created.")
except FileExistsError:
    print("File 'created_by_x.txt' already exists. (x mode failed)")

# 6. 'wb' – Write binary mode
with open("sample.bin", "wb") as f:
    f.write(b"This is binary data.\n")

# 7. 'rb' – Read binary mode
with open("sample.bin", "rb") as f:
    binary_content = f.read()
    print("Binary content (rb mode):\n", binary_content)

# 8. 'wt' – Write text mode (same as 'w', explicit text)
with open("textfile.txt", "wt") as f:
    f.write("Hello from 'wt' mode.\n")

# 9. 'rt' – Read text mode (same as 'r', explicit text)
with open("textfile.txt", "rt") as f:
    text_content = f.read()
    print("Text content (rt mode):\n", text_content)
