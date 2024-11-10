chars = ["a", "a", "b", "b", "c", "c", "c"]
write_index = 0
count = 1
for i in range(1, len(chars)):
    if chars[i] == chars[i-1]:
        count += 1
    else:
        chars[write_index] = chars[i - 1]
        write_index += 1
        if count > 1:
            for digit in str(count):
                chars[write_index] = digit
                write_index += 1
        count = 1
chars[write_index] = chars[-1]
write_index += 1
if count > 1:
    for digit in str(count):
        chars[write_index] = digit
        write_index += 1

print("Compressed array:", chars[:write_index])
        



