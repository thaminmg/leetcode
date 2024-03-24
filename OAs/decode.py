def decode(message_file):
    # Dictionary to store numbers with their corresponding words
    decoded_dict = {}
    # Read the content of the file and populate the dictionary
    maxx = -1
    with open(message_file, 'r') as file:
        for line in file:
            number, word = line.split()
            num = int(number)
            maxx = max(maxx, num)
            decoded_dict[number] = word.strip()
    # Generate a list representing the end of each pyramid line
    end_of_lines = []
    current_number = 1
    for i in range(1, maxx + 1):
        end_of_lines.append(current_number)
        current_number += i + 1
        if current_number > maxx: break
    # Decode the message using the generated list and the dictionary
    decoded_message = ''
    for num in end_of_lines:
        decoded_message += decoded_dict[str(num)] + ' '

    return decoded_message.strip()


# Example usage:
message_file = "/Users/lucaszhao/Documents/Study/leetcode/OAs/coding_qual_input.txt"
decoded_message = decode(message_file)
print("Decoded message:", decoded_message)
